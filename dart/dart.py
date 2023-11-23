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
from typing import Literal, NoReturn

import dateparser
from pick import pick
import requests

from .generated import Client
from .generated.models import (
    DartboardKind,
    Operation,
    OperationKind,
    OperationModelKind,
    Priority,
    PropertyKind,
    RequestBody,
    SpaceKind,
    StatusKind,
    Task,
    TaskCreate,
    TaskSourceType,
    TaskUpdate,
    Transaction,
    TransactionKind,
)
from .generated.api.transactions import transactions_create
from .order_manager import get_orders_between

_PROG = "dart"

_PROD_HOST = "https://app.itsdart.com"
_DEV_HOST = "http://localhost:5173"
_HOST_MAP = {"prod": _PROD_HOST, "dev": _DEV_HOST}

_VERSION_CMD = "--version"
_SET_HOST_CMD = "sethost"
_LOGIN_CMD = "login"
_CREATE_TASK_CMD = "createtask"
_UPDATE_TASK_CMD = "updatetask"
_BEGIN_TASK_CMD = "begintask"

_ROOT_API_URL_FRAG = "/api/v0"
_CSRF_URL_FRAG = _ROOT_API_URL_FRAG + "/csrf-token"
_LOGIN_URL_FRAG = _ROOT_API_URL_FRAG + "/login"
_CURRENT_USER_URL_FRAG = _ROOT_API_URL_FRAG + "/user-data?mode=auto"
_COPY_BRANCH_URL_FRAG = _ROOT_API_URL_FRAG + "/vcs/copy-branch-link"

_CONFIG_FPATH = os.path.expanduser("~/.dart-tools")
_CSRF_TOKEN_COOKIE = "csrftoken"
_SESSION_ID_COOKIE = "sessionid"
_CLIENT_DUID_KEY = "clientDuid"
_HOST_KEY = "host"
_HOSTS_KEY = "hosts"
_CSRF_TOKEN_KEY = "csrfToken"
_SESSION_ID_KEY = "sessionId"

_DUID_CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits
_PRIORITY_MAP = {
    0: Priority.CRITICAL,
    1: Priority.HIGH,
    2: Priority.MEDIUM,
    3: Priority.LOW,
}
_SIZES = {1, 2, 3, 5, 8}
_COMPLETED_STATUS_KINDS = {"Finished", "Canceled"}

_VERSION = version("dart-tools")

_is_cli = False


# TODO dedupe these functions with other usages elsewhere
def _make_duid():
    return "".join(random.choices(_DUID_CHARS, k=12))


def _run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True).decode()


def _get_task_url(host, duid):
    return f"{host}/t/{duid}"


def _suppress_exception(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception:  # pylint: disable=broad-except
            return None

    return wrapper


def _exit_gracefully(_signal_received, _frame) -> None:
    sys.exit("Quitting.")


def _log(s):
    if not _is_cli:
        return
    print(s)


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
    def __init__(self, config=None):
        self._config = config or _Config()
        self._session = requests.Session()
        if (csrf_token := self._config.get(_CSRF_TOKEN_KEY)) is not None:
            self._session.cookies.set(_CSRF_TOKEN_COOKIE, csrf_token)
        if (session_id := self._config.get(_SESSION_ID_KEY)) is not None:
            self._session.cookies.set(_SESSION_ID_COOKIE, session_id)

    def get_base_url(self):
        return self._config.host

    def get_client_duid(self):
        return self._config.client_duid

    def get_is_logged_in(self):
        return self._config.get(_SESSION_ID_KEY) is not None

    def _refresh_csrf(self):
        response = self._session.get(self._config.host + _CSRF_URL_FRAG)
        response.raise_for_status()
        csrf_token = response.cookies.get_dict().get(_CSRF_TOKEN_COOKIE)
        self._config.set(_CSRF_TOKEN_KEY, csrf_token)
        return csrf_token

    def get_csrf_token(self):
        csrf_token = self._config.get(_CSRF_TOKEN_KEY)
        if csrf_token is None:
            csrf_token = self._refresh_csrf()
        return csrf_token

    def get_headers(self):
        return {
            "client-duid": self._config.client_duid,
            "Origin": self._config.host,
            "x-csrftoken": self.get_csrf_token(),
        }

    def get_cookies(self):
        return {
            _SESSION_ID_COOKIE: self._config.get(_SESSION_ID_KEY),
            _CSRF_TOKEN_COOKIE: self.get_csrf_token(),
        }

    def get(self, url_frag, *args, **kwargs):
        kwargs["headers"] = self.get_headers() | kwargs.get("headers", {})
        return self._session.get(self._config.host + url_frag, *args, **kwargs)

    def post(self, url_frag, *args, **kwargs):
        kwargs["headers"] = self.get_headers() | kwargs.get("headers", {})
        result = self._session.post(self._config.host + url_frag, *args, **kwargs)
        if result.status_code != 403:
            return result
        self._refresh_csrf()
        kwargs["headers"] = self.get_headers() | kwargs.get("headers", {})
        return self._session.post(self._config.host + url_frag, *args, **kwargs)


class Dart(Client):
    def __init__(self, session=None):
        self._session = session or _Session()
        super().__init__(
            base_url=self._session.get_base_url(),
            cookies=self._session.get_cookies(),
            headers=self._session.get_headers(),
        )

    def transact(self, operations: list[Operation], kind: TransactionKind):
        transaction = Transaction(
            duid=_make_duid(),
            kind=kind,
            operations=operations,
        )
        request_body = RequestBody(
            client_duid=self._session.get_client_duid(),
            items=[transaction],
        )
        return transactions_create.sync(
            client=self,
            x_csrftoken=self._session.get_csrf_token(),
            json_body=request_body,
        )


class UserBundle:
    def __init__(self, session):
        _log("Loading active tasks")
        response = session.get(_CURRENT_USER_URL_FRAG)
        _check_request_response_and_maybe_exit(response)
        self._raw = response.json()
        if not self.is_logged_in:
            _auth_failure_exit()

    @property
    def is_logged_in(self):
        return self._raw["isLoggedIn"]

    @property
    def user(self):
        return self._raw["user"]

    @property
    def users(self):
        return self._raw["users"]

    @property
    def properties(self):
        return self._raw["properties"]

    @property
    def default_statuses(self):
        default_status_property_duid = next(
            e["duid"]
            for e in self.properties
            if e["kind"] == PropertyKind.DEFAULT_STATUS
        )
        return [
            e
            for e in self._raw["statuses"]
            if e["propertyDuid"] == default_status_property_duid
        ]

    @property
    def default_tags(self):
        default_tags_property_duid = next(
            e["duid"] for e in self.properties if e["kind"] == PropertyKind.DEFAULT_TAGS
        )
        return [
            e
            for e in self._raw["options"]
            if e["propertyDuid"] == default_tags_property_duid
        ]

    @property
    def spaces(self):
        return self._raw["spaces"]

    @property
    def dartboards(self):
        return self._raw["dartboards"]

    @property
    def tasks(self):
        return self._raw["tasks"]


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
        title = _Git._format_for_branch(task.title)
        long = f"{username}/{task.duid}-{title}"
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
    _log(f"Setting host to {new_host}")
    config.host = new_host

    _log("Done.")
    return True


def _auth_failure_exit():
    sys.exit(f"Not logged in, run\n\n{_PROG} {_LOGIN_CMD}\n\nto log in.")


def _unknown_failure_exit() -> NoReturn:
    sys.exit(f"Not logged in, run\n\n{_PROG} {_LOGIN_CMD}\n\nto log in.")


def _check_request_response_and_maybe_exit(response):
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        if response.status_code in {401, 403}:
            _auth_failure_exit()
        _unknown_failure_exit()


# TODO remove temporary task-only typing
def _parse_transaction_response_and_maybe_exit(
    response, model_kind: Literal[OperationModelKind.TASK], duid
) -> Task:
    if (
        response is None
        or not hasattr(response, "results")
        or len(response.results) == 0
        or not response.results[0].success
    ):
        _unknown_failure_exit()
    models = getattr(response.results[0].models, f"{model_kind}s")
    model = next((e for e in models if e.duid == duid), None)
    if model is None:
        _unknown_failure_exit()
    return model


def print_version():
    result = f"dart-tools version {_VERSION}"
    _log(result)
    return result


@_suppress_exception
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

    _log(
        f"A new version of dart-tools is available. Upgrade from {_VERSION} to {latest} with\n\n  pip install --upgrade dart-tools\n"
    )


def is_logged_in():
    config = _Config()
    session = _Session(config)

    result = session.get_is_logged_in()
    _log(f"You are {'' if result else 'not '}logged in")
    return result


def login(*, email=None, password=None):
    config = _Config()
    session = _Session(config)

    _log("Log in to Dart")
    if email is None:
        email = input("Email: ")
    if password is None:
        password = getpass()

    result = session.post(_LOGIN_URL_FRAG, json={"email": email, "password": password})
    if result.status_code in {401, 403}:
        sys.exit("Invalid login information.")
    _check_request_response_and_maybe_exit(result)

    cookies = result.cookies.get_dict()
    config.set(_SESSION_ID_KEY, cookies.get(_SESSION_ID_COOKIE))

    _log("Logged in.")
    return True


def _begin_task(config, session, user_email, get_task):
    _Git.ensure_in_repo()
    _Git.ensure_no_unstaged_changes()
    _Git.ensure_on_main_or_intended()

    task = get_task()

    response = session.post(_COPY_BRANCH_URL_FRAG, json={"duid": task.duid})
    _check_request_response_and_maybe_exit(response)

    branch_name = _Git.make_task_name(user_email, task)
    _Git.checkout_branch(branch_name)

    _log(
        f"Started work on\n\n  {task.title}\n  {_get_task_url(config.host, task.duid)}\n"
    )
    return True


def begin_task():
    config = _Config()
    session = _Session(config)

    user_bundle = UserBundle(session)
    user = user_bundle.user

    def _get_task():
        user_duid = user["duid"]
        team_space_duid = next(
            e["duid"] for e in user_bundle.spaces if e["kind"] == SpaceKind.WORKSPACE
        )
        active_duid = next(
            e["duid"]
            for e in user_bundle.dartboards
            if e["spaceDuid"] == team_space_duid and e["kind"] == DartboardKind.ACTIVE
        )
        unterm_status_duids = {
            e["duid"]
            for e in user_bundle.default_statuses
            if e["kind"] not in _COMPLETED_STATUS_KINDS
        }
        filtered_tasks = [
            e
            for e in user_bundle.tasks
            if not e["inTrash"]
            and e["dartboardDuid"] == active_duid
            and user_duid in e["assigneeDuids"]
            and e["statusDuid"] in unterm_status_duids
            and e["drafterDuid"] is None
        ]
        filtered_tasks.sort(key=lambda e: e["order"])

        if len(filtered_tasks) == 0:
            sys.exit("No active, incomplete tasks found.")

        picked_idx = pick(
            [e["title"] for e in filtered_tasks],
            "Which of your active, incomplete tasks are you beginning work on?",
            "→",
        )[1]
        assert isinstance(picked_idx, int)
        return TaskCreate.from_dict(filtered_tasks[picked_idx])

    _begin_task(config, session, user["email"], _get_task)

    _log("Done.")
    return True


def create_task(
    title,
    *,
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
    dart = Dart(session)

    user_bundle = UserBundle(session)

    user = user_bundle.user
    user_duid = user["duid"]

    dartboards = user_bundle.dartboards
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
        dartboard = next(e for e in dartboards if e["kind"] == DartboardKind.ACTIVE)
    dartboard_duid = dartboard["duid"]

    orders = [
        e["order"] for e in user_bundle.tasks if e["dartboardDuid"] == dartboard_duid
    ]
    first_order = min(orders) if len(orders) > 0 else None
    order = get_orders_between(None, first_order, 1)[0]

    statuses = user_bundle.default_statuses
    if status_title is not None:
        status_title_norm = status_title.strip().lower()
        status = next(
            (e for e in statuses if e["title"].lower() == status_title_norm), None
        )
        if status is None:
            sys.exit(f"No status found with title '{status_title}'.")
    else:
        status = next(
            e for e in statuses if e["kind"] == StatusKind.UNSTARTED and e["locked"]
        )
    status_duid = status["duid"]

    users = user_bundle.users
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

    tags = user_bundle.default_tags
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

    size = size_int

    due_at = None
    if due_at_str is not None:
        due_at = dateparser.parse(due_at_str)
        if due_at is None:
            sys.exit(f"Could not parse due date '{due_at_str}'.")
        due_at = due_at.replace(
            hour=9, minute=0, second=0, microsecond=0, tzinfo=timezone.utc
        )

    task_create = TaskCreate(
        duid=_make_duid(),
        source_type=TaskSourceType.CLI,
        drafter_duid=None,
        dartboard_duid=dartboard_duid,
        order=order,
        title=title,
        status_duid=status_duid,
        assignee_duids=assignee_duids,
        subscriber_duids=subscriber_duids,
        tag_duids=tag_duids,
        priority=priority,
        size=size,
        due_at=due_at,
    )
    task_create_op = Operation(
        model=OperationModelKind.TASK,
        kind=OperationKind.CREATE,
        data=task_create,
    )
    response = dart.transact([task_create_op], TransactionKind.TASK_CREATE)
    task = _parse_transaction_response_and_maybe_exit(
        response, OperationModelKind.TASK, task_create.duid
    )

    _log(f"Created task {task.title} at {_get_task_url(config.host, task.duid)}")

    if should_begin:
        _begin_task(config, session, user["email"], lambda: task_create)

    _log("Done.")
    return task


def update_task(
    duid,
    *,
    title=None,
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
    dart = Dart(session)

    user_bundle = UserBundle(session)

    user = user_bundle.user
    user_duid = user["duid"]

    tasks = user_bundle.tasks
    old_task = next((e for e in tasks if e["duid"] == duid), None)
    if old_task is None:
        sys.exit(f"No task found with DUID '{duid}'.")

    task_update_kwargs = {"duid": duid}

    if title is not None:
        task_update_kwargs["title"] = title

    dartboards = user_bundle.dartboards
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
        dartboard_duid = dartboard["duid"]
        if dartboard_duid != old_task["dartboardDuid"]:
            task_update_kwargs["dartboard_duid"] = dartboard_duid

    statuses = user_bundle.default_statuses
    if status_title is not None:
        status_title_norm = status_title.strip().lower()
        status = next(
            (e for e in statuses if e["title"].lower() == status_title_norm), None
        )
        if status is None:
            sys.exit(f"No status found with title '{status_title}'.")
        status_duid = status["duid"]
        if status_duid != old_task["statusDuid"]:
            task_update_kwargs["status_duid"] = status_duid

    users = user_bundle.users
    user_emails_to_duids = {e["email"]: e["duid"] for e in users}
    subscriber_duids = []
    if assignee_emails is not None:
        assignee_duids = []
        for assignee_email in assignee_emails:
            assignee_email_norm = assignee_email.strip().lower()
            if assignee_email_norm not in user_emails_to_duids:
                sys.exit(f"No user found with email '{assignee_email}'.")
            assignee_duids.append(user_emails_to_duids[assignee_email_norm])
            subscriber_duids.append(user_emails_to_duids[assignee_email_norm])
        assignee_duids = sorted(set(assignee_duids))
        if assignee_duids != old_task["assigneeDuids"]:
            task_update_kwargs["assignee_duids"] = assignee_duids

    # TODO do add to list operation rather than replace
    subscriber_duids = list(
        set(old_task["subscriberDuids"]) | set(subscriber_duids) | {user_duid}
    )
    if subscriber_duids != old_task["subscriberDuids"]:
        task_update_kwargs["subscriber_duids"] = subscriber_duids

    tags = user_bundle.default_tags
    tag_titles_to_duids = {e["title"]: e["duid"] for e in tags}
    if tag_titles is not None:
        tag_duids = []
        for tag_title in tag_titles:
            tag_title_norm = tag_title.strip().lower()
            if tag_title_norm not in tag_titles_to_duids:
                sys.exit(f"No tag found with title '{tag_title}'.")
            tag_duids.append(tag_titles_to_duids[tag_title_norm])
        task_update_kwargs["tag_duids"] = tag_duids

    # TODO add a way for optional stuff to be removed
    if priority_int is not None:
        priority = _PRIORITY_MAP[priority_int]
        if priority != old_task["priority"]:
            task_update_kwargs["priority"] = priority

    if size_int is not None:
        size = size_int
        if size != old_task["size"]:
            task_update_kwargs["size"] = size

    if due_at_str is not None:
        due_at = dateparser.parse(due_at_str)
        if due_at is None:
            sys.exit(f"Could not parse due date '{due_at_str}'.")
        due_at = due_at.replace(
            hour=9, minute=0, second=0, microsecond=0, tzinfo=timezone.utc
        )
        due_at = due_at.isoformat()[:-6] + ".000Z"
        if due_at != old_task["dueAt"]:
            task_update_kwargs["due_at"] = due_at

    task_update = TaskUpdate(**task_update_kwargs)
    task_update_op = Operation(
        model=OperationModelKind.TASK,
        kind=OperationKind.UPDATE,
        data=task_update,
    )
    response = dart.transact([task_update_op], TransactionKind.TASK_UPDATE)
    task = _parse_transaction_response_and_maybe_exit(
        response, OperationModelKind.TASK, task_update.duid
    )

    _log(f"Updated task {task.title} at {_get_task_url(config.host, task.duid)}")
    _log("Done.")
    return task


def _add_standard_task_arguments(parser):
    parser.add_argument(
        "-d", "--dartboard", dest="dartboard_title", help="dartboard title"
    )
    parser.add_argument("-s", "--status", dest="status_title", help="status title")
    parser.add_argument(
        "-a",
        "--assignee",
        dest="assignee_emails",
        nargs="*",
        action="extend",
        help="assignee email(s)",
    )
    parser.add_argument(
        "-t",
        "--tag",
        dest="tag_titles",
        nargs="*",
        action="extend",
        help="tag title(s)",
    )
    parser.add_argument(
        "-p",
        "--priority",
        dest="priority_int",
        type=int,
        choices=_PRIORITY_MAP.keys(),
        help="priority",
    )
    parser.add_argument(
        "-i", "--size", dest="size_int", type=int, choices=_SIZES, help="size"
    )
    parser.add_argument("-r", "--duedate", dest="due_at_str", help="due date")


def cli():
    signal.signal(signal.SIGINT, _exit_gracefully)
    global _is_cli
    _is_cli = True

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
    login_parser.add_argument(
        "-e", "--email", dest="email", help="email to log in with"
    )
    login_parser.add_argument(
        "-p", "--password", dest="password", help="password to log in with"
    )
    login_parser.set_defaults(func=login)

    create_task_parser = subparsers.add_parser(
        _CREATE_TASK_CMD, aliases="c", help="create a new task"
    )
    create_task_parser.add_argument("title", help="title of the task")
    create_task_parser.add_argument(
        "-b",
        "--begin",
        dest="should_begin",
        action="store_true",
        help="begin work on the task after creation",
    )
    _add_standard_task_arguments(create_task_parser)
    create_task_parser.set_defaults(func=create_task)

    update_task_parser = subparsers.add_parser(
        _UPDATE_TASK_CMD, aliases="u", help="update an existing task"
    )
    update_task_parser.add_argument("duid", help="Dart ID (DUID) of the task")
    update_task_parser.add_argument("-e", "--title", dest="title", help="task title")
    _add_standard_task_arguments(update_task_parser)
    update_task_parser.set_defaults(func=update_task)

    begin_task_parser = subparsers.add_parser(
        _BEGIN_TASK_CMD, aliases="b", help="begin work on a task"
    )
    begin_task_parser.set_defaults(func=begin_task)

    args = vars(parser.parse_args())
    func = args.pop("func")
    func(**args)
