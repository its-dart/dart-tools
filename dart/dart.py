#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A CLI to interact with the Dart web app."""

import argparse
from functools import wraps
import json
import os
import random
import re
import signal
import string
import subprocess
import sys
from collections import defaultdict
from datetime import timezone
from getpass import getpass
from importlib.metadata import version

import dateparser
import requests
from pick import pick

from .order_manager import get_orders_between

_PROG = "dart"

_PROD_HOST = "https://app.itsdart.com"
_DEV_HOST = "http://localhost:5173"
_HOST_MAP = {"prod": _PROD_HOST, "dev": _DEV_HOST}

_VERSION_CMD = "--version"
_SET_HOST_CMD = "sethost"
_LOGIN_CMD = "login"
_CREATE_TASK_CMD = "createtask"
_BEGIN_TASK_CMD = "begintask"

_ROOT_API_URL_FRAG = "/api/v0"
_CSRF_URL_FRAG = _ROOT_API_URL_FRAG + "/csrf-token"
_LOGIN_URL_FRAG = _ROOT_API_URL_FRAG + "/login"
_CURRENT_USER_URL_FRAG = _ROOT_API_URL_FRAG + "/current-user"
_CREATE_TASK_URL_FRAG = _ROOT_API_URL_FRAG + "/tasks/create"
_COPY_BRANCH_URL_FRAG = _ROOT_API_URL_FRAG + "/vcs/copy-branch-link"

_CONFIG_FPATH = os.path.expanduser("~/.dart-tools")
_CSRF_TOKEN_COOKIE = "csrftoken"
_SESSION_ID_COOKIE = "sessionid"
_CLIENT_DUID_KEY = "clientDuid"
_HOST_KEY = "host"
_HOSTS_KEY = "hosts"
_CSRF_TOKEN_KEY = "csrfToken"
_SESSION_ID_KEY = "sessionId"

_DUID_CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits + "-_"
_PRIORITY_MAP = {0: "Critical", 1: "High", 2: "Medium", 3: "Low"}
_SIZES = {1, 2, 3, 5, 8}
_COMPLETED_STATUS_KINDS = {"Finished", "Canceled"}
_DEFAULT_DESCRIPTION = {
    "root": {
        "direction": None,
        "format": "",
        "indent": 0,
        "type": "root",
        "version": 1,
        "children": [
            {
                "direction": None,
                "format": "",
                "indent": 0,
                "type": "paragraph",
                "version": 1,
                "children": [],
            }
        ],
    }
}

_VERSION = version("dart-tools")


# TODO dedupe these functions with other usages elsewhere
def _make_duid():
    return "".join(random.choices(_DUID_CHARS, k=12))


def _run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True).decode()


def _get_task_url(host, duid):
    return f"{host}/search?t={duid}"


def suppress_exception(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception:  # pylint: disable=broad-except
            return None

    return wrapper


def _exit_gracefully(_signal_received, _frame) -> None:
    sys.exit("Quitting.")


class _Config:
    def __init__(self):
        self._content = {}
        if os.path.isfile(_CONFIG_FPATH):
            with open(_CONFIG_FPATH, "r", encoding="UTF-8") as fin:
                self._content = json.load(fin)
        self._content = {
            _CLIENT_DUID_KEY: _make_duid(),
            _HOST_KEY: _PROD_HOST,
            _HOSTS_KEY: {},
        } | self._content
        self._content[_HOSTS_KEY] = defaultdict(dict, self._content[_HOSTS_KEY])
        self._write()

    def _write(self):
        with open(_CONFIG_FPATH, "w+", encoding="UTF-8") as fout:
            json.dump(self._content, fout, indent=2)

    @property
    def client_duid(self):
        return self._content[_CLIENT_DUID_KEY]

    @property
    def host(self):
        return self._content[_HOST_KEY]

    @host.setter
    def host(self, v):
        self._content[_HOST_KEY] = v
        self._write()

    def get(self, k):
        return self._content[_HOSTS_KEY][self.host].get(k)

    def set(self, k, v):
        self._content[_HOSTS_KEY][self.host][k] = v
        self._write()


class _Session:
    def __init__(self, config):
        self._config = config
        self._session = requests.Session()
        if (csrf_token := self._config.get(_CSRF_TOKEN_KEY)) is not None:
            self._session.cookies.set(_CSRF_TOKEN_COOKIE, csrf_token)
        if (session_id := self._config.get(_SESSION_ID_KEY)) is not None:
            self._session.cookies.set(_SESSION_ID_COOKIE, session_id)

    def _refresh_csrf(self):
        response = self._session.get(self._config.host + _CSRF_URL_FRAG)
        response.raise_for_status()
        csrf_token = response.cookies.get_dict().get(_CSRF_TOKEN_COOKIE)
        self._config.set(_CSRF_TOKEN_KEY, csrf_token)
        return csrf_token

    def _get_csrf_token(self):
        csrf_token = self._config.get(_CSRF_TOKEN_KEY)
        if csrf_token is None:
            csrf_token = self._refresh_csrf()
        return csrf_token

    def _make_headers(self, headers):
        headers["client-duid"] = self._config.client_duid
        headers["x-csrftoken"] = self._get_csrf_token()
        headers["Origin"] = self._config.host
        return headers

    def get(self, url_frag, *args, **kwargs):
        kwargs["headers"] = self._make_headers(kwargs.get("headers", {}))
        return self._session.get(self._config.host + url_frag, *args, **kwargs)

    def post(self, url_frag, *args, **kwargs):
        kwargs["headers"] = self._make_headers(kwargs.get("headers", {}))
        result = self._session.post(self._config.host + url_frag, *args, **kwargs)
        if result.status_code != 403:
            return result
        self._refresh_csrf()
        kwargs["headers"] = self._make_headers(kwargs.get("headers", {}))
        return self._session.post(self._config.host + url_frag, *args, **kwargs)


class _Git:
    @staticmethod
    def _cmd_succeeds(cmd):
        try:
            _run_cmd(f"{cmd} 2>&1")
        except subprocess.CalledProcessError as ex:
            if "128" in str(ex):
                return False
            raise ex
        return True

    @staticmethod
    def _format_for_branch(s):
        return re.sub(
            r"-{2,}", "-", re.sub(r"[^a-z0-9-]+", "-", s.lower().replace("'", ""))
        ).strip("-")

    @staticmethod
    def make_task_name(email, task):
        username = _Git._format_for_branch(email.split("@")[0])
        title = _Git._format_for_branch(task["title"])
        long = f"{username}/{task['duid']}-{title}"
        if len(long) <= 60:
            return long
        for i in range(1, 11):
            if long[60 - i] == "-":
                return long[: 60 - i]
        return long[:60]

    @staticmethod
    def get_current_branch():
        return _run_cmd("git rev-parse --abbrev-ref HEAD").strip()

    @staticmethod
    def ensure_in_repo():
        if _Git._cmd_succeeds("git rev-parse --is-inside-work-tree"):
            return
        sys.exit("You are not in a git repo.")

    @staticmethod
    def ensure_no_unstaged_changes():
        if _run_cmd("git status --porcelain") == "":
            return
        sys.exit("You have uncommitted changes. Please commit or stash them.")

    @staticmethod
    def ensure_on_main_or_intended():
        branch = _Git.get_current_branch()
        if branch == "main":
            return
        if (
            pick(
                ["Yes", "No"],
                "You're not on the 'main' branch. Is this intentional?",
                "→",
            )[0]
            == "Yes"
        ):
            return
        _run_cmd("git checkout main")

    @staticmethod
    def branch_exists(branch):
        return _Git._cmd_succeeds(f"git rev-parse --verify {branch}")

    @staticmethod
    def checkout_branch(branch):
        if _Git.branch_exists(branch):
            _run_cmd(f"git checkout {branch}")
            return

        if _Git.branch_exists(f"origin/{branch}"):
            _run_cmd(f"git checkout --track origin/{branch}")
            return

        _run_cmd(f"git checkout -b {branch}")


def set_host(host):
    config = _Config()

    new_host = _HOST_MAP.get(host, host)
    print(f"Setting host to {new_host}")
    config.host = new_host

    print("Done.")


def _print_login_failure_message_and_exit():
    sys.exit(f"Not logged in, run\n\n{_PROG} {_LOGIN_CMD}\n\nto log in.")


def _check_response_and_maybe_exit(response):
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        if response.status_code in {401, 403}:
            _print_login_failure_message_and_exit()
        sys.exit("Unknown failure, please email support@itsdart.com.")


def print_version():
    print(f"dart-tools version {_VERSION}")


@suppress_exception
def print_version_update_message_maybe():
    latest = (
        _run_cmd("pip --disable-pip-version-check index versions dart-tools 2>&1")
        .rsplit("LATEST:", maxsplit=1)[-1]
        .split("\n", maxsplit=1)[0]
        .strip()
    )
    if latest == _VERSION or [int(e) for e in latest.split(".")] <= [
        int(e) for e in _VERSION.split(".")
    ]:
        return

    print(
        f"A new version of dart-tools is available. Upgrade from {_VERSION} to {latest} with\n\n  pip install --upgrade dart-tools\n"
    )


def login():
    config = _Config()
    session = _Session(config)

    print("Dart login information")
    email = input("Email: ")
    password = getpass()

    result = session.post(_LOGIN_URL_FRAG, json={"email": email, "password": password})
    if result.status_code in {401, 403}:
        sys.exit("Invalid login information.")
    _check_response_and_maybe_exit(result)

    cookies = result.cookies.get_dict()
    config.set(_SESSION_ID_KEY, cookies.get(_SESSION_ID_COOKIE))

    print("Logged in.")


def _get_full_user_bundle(session):
    print("Loading active tasks")
    response = session.get(_CURRENT_USER_URL_FRAG)
    _check_response_and_maybe_exit(response)
    res = response.json()
    if not res["isLoggedIn"]:
        _print_login_failure_message_and_exit()
    return res


def _begin_task(config, session, user_email, get_task):
    _Git.ensure_in_repo()
    _Git.ensure_no_unstaged_changes()
    _Git.ensure_on_main_or_intended()

    task = get_task()

    response = session.post(_COPY_BRANCH_URL_FRAG, json={"duid": task["duid"]})
    _check_response_and_maybe_exit(response)

    branch_name = _Git.make_task_name(user_email, task)
    _Git.checkout_branch(branch_name)

    print(
        f"Started work on\n\n  {task['title']}\n  {_get_task_url(config.host, task['duid'])}\n"
    )


def begin_task():
    config = _Config()
    session = _Session(config)

    user_bundle = _get_full_user_bundle(session)
    user = user_bundle["user"]

    def _get_task():
        user_duid = user["duid"]
        active_duid = next(
            e["duid"] for e in user_bundle["dartboards"] if e["kind"] == "Active"
        )
        unterm_status_duids = {
            e["duid"]
            for e in user_bundle["statuses"]
            if e["kind"] not in _COMPLETED_STATUS_KINDS
        }
        filtered_tasks = [
            e
            for e in user_bundle["tasks"]
            if not e["inTrash"]
            and e["dartboardDuid"] == active_duid
            and user_duid in e["assigneeDuids"]
            and e["statusDuid"] in unterm_status_duids
            and e["drafterDuid"] is None
        ]
        filtered_tasks.sort(key=lambda e: e["order"])

        if len(filtered_tasks) == 0:
            sys.exit("No active, incomplete tasks found.")

        return filtered_tasks[
            pick(
                [e["title"] for e in filtered_tasks],
                "Which of your active, incomplete tasks are you beginning work on?",
                "→",
            )[1]
        ]

    _begin_task(config, session, user["email"], _get_task)

    print("Done.")


def create_task(
    title,
    should_begin=False,
    dartboard_title=None,
    status_title=None,
    assignee_emails=None,
    tag_titles=None,
    priority_int=None,
    size_int=None,
    due_at_str=None,
):
    config = _Config()
    session = _Session(config)

    user_bundle = _get_full_user_bundle(session)

    user = user_bundle["user"]
    user_duid = user["duid"]

    dartboards = user_bundle["dartboards"]
    if dartboard_title is not None:
        dartboard_title_norm = dartboard_title.strip().lower()
        dartboard = next(
            (
                e
                for e in dartboards
                if dartboard_title_norm in {e["title"].lower(), e["kind"].lower()}
            ),
            None,
        )
        if dartboard is None:
            sys.exit(f"No dartboard found with title '{dartboard_title}'.")
    else:
        dartboard = next(e for e in dartboards if e["kind"] == "Active")
    dartboard_duid = dartboard["duid"]

    orders = [
        e["order"] for e in user_bundle["tasks"] if e["dartboardDuid"] == dartboard_duid
    ]
    first_order = min(orders) if len(orders) > 0 else None
    order = get_orders_between(None, first_order, 1)[0]

    statuses = user_bundle["statuses"]
    if status_title is not None:
        status_title_norm = status_title.strip().lower()
        status = next(
            (e for e in statuses if e["title"].lower() == status_title_norm), None
        )
        if status is None:
            sys.exit(f"No status found with title '{status_title}'.")
    else:
        status = next(e for e in statuses if e["kind"] == "Unstarted" and e["locked"])
    status_duid = status["duid"]

    users = user_bundle["users"]
    user_emails_to_duids = {e["email"]: e["duid"] for e in users}
    assignee_duids = []
    subscriber_duids = []
    if assignee_emails is not None:
        for assignee_email in assignee_emails:
            assignee_email_norm = assignee_email.strip().lower()
            if assignee_email_norm not in user_emails_to_duids:
                sys.exit(f"No user found with email '{assignee_email}'.")
            assignee_duids.append(user_emails_to_duids[assignee_email_norm])
            subscriber_duids.append(user_emails_to_duids[assignee_email_norm])
    else:
        assignee_duids.append(user_duid)
    assignee_duids = list(set(assignee_duids))
    subscriber_duids.append(user_duid)
    subscriber_duids = list(set(subscriber_duids))

    tags = user_bundle["tags"]
    tag_titles_to_duids = {e["title"]: e["duid"] for e in tags}
    tag_duids = []
    if tag_titles is not None:
        for tag_title in tag_titles:
            tag_title_norm = tag_title.strip().lower()
            if tag_title_norm not in tag_titles_to_duids:
                sys.exit(f"No tag found with title '{tag_title}'.")
            tag_duids.append(tag_titles_to_duids[tag_title_norm])

    priority = None
    if priority_int is not None:
        priority = _PRIORITY_MAP[priority_int]

    due_at = None
    if due_at_str is not None:
        due_at = dateparser.parse(due_at_str)
        if due_at is None:
            sys.exit(f"Could not parse due date '{due_at_str}'.")
        due_at = due_at.replace(
            hour=9, minute=0, second=0, microsecond=0, tzinfo=timezone.utc
        )
        due_at = due_at.isoformat()[:-6] + ".000Z"

    task = {
        "duid": _make_duid(),
        "sourceType": "CLI",
        "drafterDuid": None,
        "dartboardDuid": dartboard_duid,
        "order": order,
        "title": title,
        "description": _DEFAULT_DESCRIPTION,
        "statusDuid": status_duid,
        "assigneeDuids": assignee_duids,
        "subscriberDuids": subscriber_duids,
        "tagDuids": tag_duids,
        "priority": priority,
        "size": size_int,
        "dueAt": due_at,
    }
    response = session.post(_CREATE_TASK_URL_FRAG, json={"item": task})
    _check_response_and_maybe_exit(response)

    print(f"Created task {task['title']} at {_get_task_url(config.host, task['duid'])}")

    if should_begin:
        _begin_task(config, session, user["email"], lambda: task)

    print("Done.")


def cli():
    signal.signal(signal.SIGINT, _exit_gracefully)

    print_version_update_message_maybe()

    if _VERSION_CMD in sys.argv[1:]:
        print_version()
        return

    parser = argparse.ArgumentParser(
        prog=_PROG, description="A CLI to interact with Dart"
    )
    subparsers = parser.add_subparsers(
        title="command",
        required=True,
        metavar=f"{{{_LOGIN_CMD},{_CREATE_TASK_CMD},{_BEGIN_TASK_CMD}}}",
    )

    set_host_parser = subparsers.add_parser(_SET_HOST_CMD, aliases="s")
    set_host_parser.add_argument("host", help="the new host: {prod|dev|[URL]}")
    set_host_parser.set_defaults(func=set_host)

    login_parser = subparsers.add_parser(_LOGIN_CMD, aliases="l", help="login")
    login_parser.set_defaults(func=login)

    create_task_parser = subparsers.add_parser(
        _CREATE_TASK_CMD, aliases="c", help="create a new task"
    )
    create_task_parser.add_argument("title", help="the title of the task")
    create_task_parser.add_argument(
        "-b",
        "--begin",
        dest="should_begin",
        action="store_true",
        help="begin work on the task after creation",
    )
    create_task_parser.add_argument(
        "-d", "--dartboard", dest="dartboard_title", help="dartboard title"
    )
    create_task_parser.add_argument(
        "-s", "--status", dest="status_title", help="status title"
    )
    create_task_parser.add_argument(
        "-a",
        "--assignee",
        dest="assignee_emails",
        nargs="*",
        action="extend",
        help="assignee email(s)",
    )
    create_task_parser.add_argument(
        "-t",
        "--tag",
        dest="tag_titles",
        nargs="*",
        action="extend",
        help="tag title(s)",
    )
    create_task_parser.add_argument(
        "-p",
        "--priority",
        dest="priority_int",
        type=int,
        choices=_PRIORITY_MAP.keys(),
        help="priority",
    )
    create_task_parser.add_argument(
        "-i", "--size", dest="size_int", type=int, choices=_SIZES, help="size"
    )
    create_task_parser.add_argument(
        "-r", "--duedate", dest="due_at_str", help="due date"
    )
    create_task_parser.set_defaults(func=create_task)

    begin_task_parser = subparsers.add_parser(
        _BEGIN_TASK_CMD, aliases="b", help="begin work on a task"
    )
    begin_task_parser.set_defaults(func=begin_task)

    args = vars(parser.parse_args())
    func = args.pop("func")
    func(**args)


if __name__ == "__main__":
    cli()
