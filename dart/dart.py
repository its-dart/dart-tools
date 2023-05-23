#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A CLI to interact with the Dart web app."""

import argparse
from collections import defaultdict
from getpass import getpass
from importlib.metadata import version
import json
import os
import random
import re
import string
import subprocess
import sys

from pick import pick
import requests

from .order_manager import get_orders_between


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

_CONFIG_FPATH = os.path.expanduser("~/.dart")
_CSRF_TOKEN_COOKIE = "csrftoken"
_SESSION_ID_COOKIE = "sessionid"
_CLIENT_DUID_KEY = "clientDuid"
_HOST_KEY = "host"
_HOSTS_KEY = "hosts"
_CSRF_TOKEN_KEY = "csrfToken"
_SESSION_ID_KEY = "sessionId"

_DUID_CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits + "-_"
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


# TODO dedupe these functions with other usages elsewhere
def _make_duid():
    return "".join(random.choices(_DUID_CHARS, k=12))


def _run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True).decode()


def _get_task_url(host, duid):
    return f"{host}/search?t={duid}"


class _Config:
    def __init__(self):
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
    def _format_for_branch(s):
        return re.sub("[^A-Za-z0-9_]+", "-", s.lower())

    @staticmethod
    def make_task_name(email, task):
        username = _Git._format_for_branch(email.split("@")[0])
        title = _Git._format_for_branch(task["title"])
        return f"{username}/{task['duid']}-{title}"[:60]

    @staticmethod
    def get_current_branch():
        return _run_cmd("git rev-parse --abbrev-ref HEAD").strip()

    @staticmethod
    def ensure_no_unstaged_changes():
        if _run_cmd("git status --porcelain"):
            print("You have uncommitted changes. Please commit or stash them.")
            sys.exit(1)

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
        try:
            _run_cmd(f"git rev-parse --verify {branch} 2>&1")
        except subprocess.CalledProcessError as ex:
            if "128" in str(ex):
                return False
            raise ex
        return True

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

    config.host = _HOST_MAP.get(host, host)

    print("Done.")


def _print_login_failure_message_and_exit():
    print(f"Not logged in, run\n\n{sys.argv[0]} {_LOGIN_CMD}\n\nto log in.")
    sys.exit(1)


def _check_response_and_maybe_exit(response):
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        if response.status_code in {401, 403}:
            _print_login_failure_message_and_exit()
        print("Unknown failure, please email support@itsdart.com.")
        sys.exit(1)


def print_version():
    print(f"dart-tools version {version('dart-tools')}")


def login():
    config = _Config()
    session = _Session(config)

    print("Dart login information")
    email = input("Email: ")
    password = getpass()

    result = session.post(_LOGIN_URL_FRAG, json={"email": email, "password": password})
    if result.status_code in {401, 403}:
        print("Invalid login information.")
        sys.exit(1)
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


def begin_task():
    _Git.ensure_no_unstaged_changes()
    _Git.ensure_on_main_or_intended()

    config = _Config()
    session = _Session(config)

    user_bundle = _get_full_user_bundle(session)

    user = user_bundle["user"]
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

    chosen_task = filtered_tasks[
        pick(
            [e["title"] for e in filtered_tasks],
            "Which of your active, unfinalized tasks are you beginning work on?",
            "→",
        )[1]
    ]

    response = session.post(_COPY_BRANCH_URL_FRAG, json={"duid": chosen_task["duid"]})
    _check_response_and_maybe_exit(response)

    branch_name = _Git.make_task_name(user["email"], chosen_task)
    _Git.checkout_branch(branch_name)

    print(
        f"Started work on [{chosen_task['title']}]({_get_task_url(config.host, chosen_task['duid'])}) on branch {branch_name}"
    )
    print("Done.")


def create_task(title):
    config = _Config()
    session = _Session(config)

    user_bundle = _get_full_user_bundle(session)

    user_duid = user_bundle["user"]["duid"]
    active_duid = next(
        e["duid"] for e in user_bundle["dartboards"] if e["kind"] == "Active"
    )
    first_order = min(
        e["order"] for e in user_bundle["tasks"] if e["dartboardDuid"] == active_duid
    )
    order = get_orders_between(None, first_order, 1)[0]
    status_duid = next(
        e["duid"]
        for e in user_bundle["statuses"]
        if e["kind"] == "Unstarted" and e["locked"]
    )

    task = {
        "duid": _make_duid(),
        "drafterDuid": None,
        "dartboardDuid": active_duid,
        "order": order,
        "title": title,
        "description": _DEFAULT_DESCRIPTION,
        "statusDuid": status_duid,
        "assigneeDuids": [user_duid],
        "subscriberDuids": [user_duid],
        "tagDuids": [],
        "priority": None,
        "size": None,
        "dueAt": None,
    }
    response = session.post(_CREATE_TASK_URL_FRAG, json={"item": task})
    _check_response_and_maybe_exit(response)

    print(f"Created task [{task['title']}]({_get_task_url(config.host, task['duid'])})")
    print("Done.")


def cli():
    if _VERSION_CMD in sys.argv:
        print_version()
        sys.exit(0)

    parser = argparse.ArgumentParser(
        prog="dart", description="A CLI to interact with Dart"
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
