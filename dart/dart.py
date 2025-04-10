#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A CLI to interact with the Dart web app."""

# Required for type hinting compatibility when using Python 3.9
from __future__ import annotations

import json
import os
import random
import re
import signal
import string
import subprocess
import sys
from argparse import ArgumentParser
from collections import defaultdict
from datetime import timezone
from functools import wraps
from importlib.metadata import version
from typing import Callable, NoReturn
from webbrowser import open_new_tab

import dateparser
import httpx
import platformdirs
from pick import pick

from .exception import DartException
from .generated import Client
from .generated.api.config import get_config as get_config_api
from .generated.api.task import create_task as create_task_api
from .generated.api.task import delete_task as delete_task_api
from .generated.api.task import list_tasks as list_tasks_api
from .generated.api.task import retrieve_task as retrieve_task_api
from .generated.api.task import update_task as update_task_api
from .generated.errors import UnexpectedStatus
from .generated.models import (
    ConciseTask,
    PaginatedConciseTaskList,
    Task,
    TaskCreate,
    TaskUpdate,
    UserSpaceConfiguration,
    WrappedTask,
    WrappedTaskCreate,
    WrappedTaskUpdate,
)
from .generated.types import UNSET, Unset

_APP = "dart-tools"
_PROG = "dart"

_PROD_HOST = "https://app.itsdart.com"
_STAG_HOST = "https://stag.itsdart.com"
_DEV_HOST = "http://localhost:5173"
_HOST_MAP = {"prod": _PROD_HOST, "stag": _STAG_HOST, "dev": _DEV_HOST}

_VERSION_CMD = "--version"
_SET_HOST_CMD = "sethost"
_LOGIN_CMD = "login"
_CREATE_TASK_CMD = "createtask"
_UPDATE_TASK_CMD = "updatetask"
_BEGIN_TASK_CMD = "begintask"

_PROFILE_SETTINGS_URL_FRAG = "/?settings=account"
_ROOT_PRIVATE_API_URL_FRAG = "/api/v0"
_ROOT_PUBLIC_API_URL_FRAG = "/api/v0/public"
_COPY_BRANCH_URL_FRAG = "/vcs/copy-branch-link"

_AUTH_TOKEN_ENVVAR_KEY = "DART_TOKEN"
_CONFIG_FPATH = platformdirs.user_config_path(_APP)
_CLIENT_DUID_KEY = "clientDuid"
_HOST_KEY = "host"
_HOSTS_KEY = "hosts"
_AUTH_TOKEN_KEY = "authToken"

_DUID_CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits
_NON_ALPHANUM_RE = re.compile(r"[^a-zA-Z0-9-]+")
_REPEATED_DASH_RE = re.compile(r"-{2,}")
_PRIORITY_MAP: dict[int, str] = {
    0: "critical",
    1: "high",
    2: "medium",
    3: "low",
}
_SIZES = {1, 2, 3, 5, 8}

_VERSION = version(_APP)
_AUTH_TOKEN_ENVVAR = os.environ.get(_AUTH_TOKEN_ENVVAR_KEY)

_is_cli = False


# TODO dedupe these functions with other usages elsewhere
def _make_duid() -> str:
    return "".join(random.choices(_DUID_CHARS, k=12))


def trim_slug_str(s: str, length: int, max_under: int | None = None) -> str:
    max_under = max_under if max_under is not None else length // 6
    if len(s) <= length:
        return s
    for i in range(1, max_under + 1):
        if s[length - i] == "-":
            return s[: length - i]
    return s[:length]


def slugify_str(s: str, lower: bool = False, trim_kwargs: dict | None = None) -> str:
    lowered = s.lower() if lower else s
    formatted = _NON_ALPHANUM_RE.sub("-", lowered.replace("'", ""))
    formatted = _REPEATED_DASH_RE.sub("-", formatted).strip("-")
    return (
        trim_slug_str(formatted, **trim_kwargs)
        if trim_kwargs is not None
        else formatted
    )


def _run_cmd(cmd: str) -> str:
    return subprocess.check_output(cmd, shell=True).decode()


def _get_space_url(host: str, duid: str) -> str:
    return f"{host}/s/{duid}"


def _get_dartboard_url(host: str, duid: str) -> str:
    return f"{host}/d/{duid}"


def _get_task_url(host: str, duid: str) -> str:
    return f"{host}/t/{duid}"


def _get_folder_url(host: str, duid: str) -> str:
    return f"{host}/f/{duid}"


def _suppress_exception(fn: Callable) -> Callable:
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception:  # pylint: disable=broad-except
            return None

    return wrapper


def _dart_exit(message: str) -> NoReturn:
    if _is_cli:
        sys.exit(message)
    raise DartException(message)


def _exit_gracefully(_signal_received, _frame) -> None:
    _dart_exit("Quitting.")


def _log(s: str) -> None:
    if not _is_cli:
        return
    print(s)


def _handle_api_errors(fn: Callable) -> Callable:
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except DartException as ex:
            _dart_exit(f"Failed to execute API call. {ex}")
        except UnexpectedStatus as ex:
            if ex.status_code in {401, 403}:
                _auth_failure_exit()

            try:
                content = json.loads(ex.content)
                error_message = content.get("detail") or " ".join(
                    content.get("errors", [])
                )
                _dart_exit(error_message)
            except (json.JSONDecodeError, AttributeError):
                _unknown_failure_exit()
        except httpx.TimeoutException:
            _dart_exit("Failed to execute API call. The request timed out.")

    return wrapper


class _Config:
    def __init__(self):
        self._content = {}
        if os.path.isfile(_CONFIG_FPATH):
            try:
                with open(_CONFIG_FPATH, "r", encoding="UTF-8") as fin:
                    self._content = json.load(fin)
            except OSError:
                pass
        self._content = {
            _CLIENT_DUID_KEY: _make_duid(),
            _HOST_KEY: _PROD_HOST,
            _HOSTS_KEY: {},
        } | self._content
        self._content[_HOSTS_KEY] = defaultdict(dict, self._content[_HOSTS_KEY])
        self._write()

    def _write(self):
        try:
            with open(_CONFIG_FPATH, "w+", encoding="UTF-8") as fout:
                json.dump(self._content, fout, indent=2)
        except OSError:
            pass

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


class Dart:
    def __init__(self, config=None):
        self._config = config or _Config()
        self._init_clients()

    def _init_clients(self):
        self._private_api = Client(
            base_url=self.get_base_url() + _ROOT_PRIVATE_API_URL_FRAG,
            headers=self.get_headers(),
            raise_on_unexpected_status=True,
        )
        self._public_api = Client(
            base_url=self.get_base_url() + _ROOT_PUBLIC_API_URL_FRAG,
            headers=self.get_headers(),
            raise_on_unexpected_status=True,
        )

    def get_base_url(self):
        return self._config.host

    def get_client_duid(self):
        return self._config.client_duid

    def get_auth_token(self):
        result = self._config.get(_AUTH_TOKEN_KEY)
        if result is not None:
            return result
        return _AUTH_TOKEN_ENVVAR

    def get_headers(self):
        result = {
            "Origin": self._config.host,
            "client-duid": self.get_client_duid(),
        }
        if (auth_token := self.get_auth_token()) is not None:
            result["Authorization"] = f"Bearer {auth_token}"
        return result

    def is_logged_in(self) -> bool:
        self._init_clients()
        try:
            config = get_config_api.sync(client=self._public_api)
            if config is None:
                return False
        except (httpx.TimeoutException, UnexpectedStatus) as ex:
            return False
        return True

    @_handle_api_errors
    def get_config(self) -> UserSpaceConfiguration:
        config = get_config_api.sync(client=self._public_api)
        if config is None:
            raise DartException(
                "Failed to fetch user space configuration: API returned None."
            )
        return config

    @_handle_api_errors
    def create_task(self, body: WrappedTaskCreate) -> WrappedTask:
        task = create_task_api.sync(client=self._public_api, body=body)
        if task is None:
            raise DartException("Failed to create task: API returned None.")
        return task

    @_handle_api_errors
    def retrieve_task(self, duid: str) -> WrappedTask:
        task = retrieve_task_api.sync(duid, client=self._public_api)
        if task is None:
            raise DartException("Failed to retrieve task: API returned None.")
        return task

    @_handle_api_errors
    def update_task(self, duid: str, body: WrappedTaskUpdate) -> WrappedTask:
        task = update_task_api.sync(duid, client=self._public_api, body=body)
        if task is None:
            raise DartException("Failed to update task: API returned None.")
        return task

    @_handle_api_errors
    def delete_task(self, duid: str) -> WrappedTask:
        task = delete_task_api.sync(duid, client=self._public_api)
        if task is None:
            raise DartException("Failed to delete task: API returned None.")
        return task

    @_handle_api_errors
    def list_tasks(self, **kwargs) -> PaginatedConciseTaskList:
        filtered_tasks = list_tasks_api.sync(client=self._public_api, **kwargs)
        if filtered_tasks is None:
            raise DartException("Failed to filter tasks: API returned None.")
        return filtered_tasks

    @_handle_api_errors
    def copy_branch_link(self, duid: str) -> None:
        self._private_api.get_httpx_client().post(
            _COPY_BRANCH_URL_FRAG, json={"duid": duid}
        )


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
    def make_task_name(email, task):
        username = slugify_str(email.split("@")[0], lower=True)
        title = slugify_str(task.title, lower=True)
        return trim_slug_str(f"{username}/{task.duid}-{title}", length=60)

    @staticmethod
    def get_current_branch():
        return _run_cmd("git rev-parse --abbrev-ref HEAD").strip()

    @staticmethod
    def ensure_in_repo():
        if _Git._cmd_succeeds("git rev-parse --is-inside-work-tree"):
            return
        _dart_exit("You are not in a git repo.")

    @staticmethod
    def ensure_no_unstaged_changes():
        if _run_cmd("git status --porcelain") == "":
            return
        _dart_exit("You have uncommitted changes. Please commit or stash them.")

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


def get_host() -> str:
    config = _Config()

    host = config.host
    _log(f"Host is {host}")
    _log("Done.")
    return host


def set_host(host: str) -> bool:
    config = _Config()

    new_host = _HOST_MAP.get(host, host)
    config.host = new_host

    _log(f"Set host to {new_host}")
    _log("Done.")
    return True


def _auth_failure_exit() -> NoReturn:
    if _is_cli:
        sys.exit(f"Not logged in, run\n\n  {_PROG} {_LOGIN_CMD}\n\nto log in.")
    raise DartException(
        f"Not logged in, either run dart.login(token) or save the token into the DART_TOKEN environment variable."
    )


def _unknown_failure_exit() -> NoReturn:
    _dart_exit("Unknown failure, email\n\n  support@itsdart.com\n\nfor help.")


def print_version() -> str:
    result = f"dart-tools version {_VERSION}"
    _log(result)
    return result


@_suppress_exception
def print_version_update_message_maybe() -> None:
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


def is_logged_in(should_raise: bool = False) -> bool:
    dart = Dart()
    result = dart.is_logged_in()

    if not result and should_raise:
        _auth_failure_exit()
    _log(f"You are {'' if result else 'not '}logged in")
    return result


def login(token: str | None = None) -> bool:
    config = _Config()
    dart = Dart(config=config)

    _log("Log in to Dart")
    if token is None:
        if not _is_cli:
            _dart_exit("Login failed, token is required.")
        _log(
            "Dart is opening in your browser, log in if needed and copy your authentication token from the page"
        )
        open_new_tab(config.host + _PROFILE_SETTINGS_URL_FRAG)
        token = input("Token: ")

    config.set(_AUTH_TOKEN_KEY, token)

    worked = dart.is_logged_in()
    if not worked:
        _dart_exit("Invalid token.")

    _log("Logged in.")
    return True


def _begin_task(dart: Dart, email: str, task: ConciseTask | Task) -> bool:
    _Git.ensure_in_repo()
    _Git.ensure_no_unstaged_changes()
    _Git.ensure_on_main_or_intended()

    dart = Dart()
    dart.copy_branch_link(task.id)

    branch_name = _Git.make_task_name(email, task)
    _Git.checkout_branch(branch_name)

    _log(
        f"Started work on\n\n  {task.title}\n  {_get_task_url(dart.get_base_url(), task.id)}\n"
    )
    return True


def begin_task() -> bool:
    dart = Dart()
    user_space_config = dart.get_config()
    user = user_space_config.user
    # TODO: Find a way to more accurately determine the incomplete task status
    incomplete_task_status = user_space_config.statuses[0]
    filtered_tasks = dart.list_tasks(
        assignee=user.email, status=incomplete_task_status
    ).results

    if not filtered_tasks:
        _dart_exit("No active, incomplete tasks found.")

    picked_idx = pick(
        [e.title for e in filtered_tasks],
        "Which of your active, incomplete tasks are you beginning work on?",
        "→",
    )[1]
    assert isinstance(picked_idx, int)

    _begin_task(dart, user.email, filtered_tasks[picked_idx])

    _log("Done.")
    return True


def _get_priority_from_int_arg(priority_int: int | None | Unset) -> str | None | Unset:
    if priority_int in (None, UNSET):
        return priority_int

    if priority_int not in _PRIORITY_MAP:
        _dart_exit(
            f"Invalid priority {priority_int}. Valid values are {list(_PRIORITY_MAP.keys())}."
        )

    return _PRIORITY_MAP[priority_int]


def _get_due_at_from_str_arg(due_at_str: str | None | Unset) -> str | None | Unset:
    if due_at_str in (None, UNSET):
        return due_at_str

    due_at = dateparser.parse(due_at_str)
    if not due_at:
        _dart_exit(f"Could not parse due date '{due_at_str}'.")
    due_at = due_at.replace(
        hour=0, minute=0, second=0, microsecond=0, tzinfo=timezone.utc
    ).isoformat()

    return due_at


def create_task(
    title: str,
    *,
    dartboard_title: str | Unset = UNSET,
    status_title: str | Unset = UNSET,
    assignee_emails: list[str] | Unset = UNSET,
    tag_titles: list[str] | Unset = UNSET,
    priority_int: int | None | Unset = UNSET,
    size_int: int | None | Unset = UNSET,
    due_at_str: str | None | Unset = UNSET,
    should_begin: bool = False,
) -> Task:
    dart = Dart()
    task_create = WrappedTaskCreate(
        item=TaskCreate(
            title,
            dartboard=dartboard_title,
            status=status_title,
            assignees=assignee_emails if assignee_emails is not None else UNSET,
            tags=tag_titles if tag_titles is not None else UNSET,
            priority=_get_priority_from_int_arg(priority_int),
            size=size_int,
            due_at=_get_due_at_from_str_arg(due_at_str),
        )
    )
    task = dart.create_task(task_create).item
    _log(f"Created task {task.title} at {_get_task_url(dart.get_base_url(), task.id)}")

    if should_begin:
        user = dart.get_config().user
        _begin_task(dart, user.email, task)

    _log("Done.")
    return task


def update_task(
    duid: str,
    *,
    title: Unset | str = UNSET,
    dartboard_title: str | Unset = UNSET,
    status_title: str | Unset = UNSET,
    assignee_emails: list[str] | Unset = UNSET,
    tag_titles: list[str] | Unset = UNSET,
    priority_int: int | None | Unset = UNSET,
    size_int: int | None | Unset = UNSET,
    due_at_str: str | None | Unset = UNSET,
) -> Task:
    dart = Dart()
    task_update = WrappedTaskUpdate(
        item=TaskUpdate(
            duid,
            title=title,
            dartboard=dartboard_title,
            status=status_title,
            assignees=assignee_emails if assignee_emails is not None else UNSET,
            tags=tag_titles if tag_titles is not None else UNSET,
            priority=_get_priority_from_int_arg(priority_int),
            size=size_int,
            due_at=_get_due_at_from_str_arg(due_at_str),
        )
    )
    task = dart.update_task(duid, task_update).item

    _log(f"Updated task {task.title} at {_get_task_url(dart.get_base_url(), task.id)}")
    _log("Done.")
    return task


def _add_standard_task_arguments(parser: ArgumentParser) -> None:
    parser.add_argument(
        "-d",
        "--dartboard",
        dest="dartboard_title",
        help="dartboard title",
        default=UNSET,
    )
    parser.add_argument(
        "-s",
        "--status",
        dest="status_title",
        help="status title",
        default=UNSET,
    )
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
        default=UNSET,
    )
    parser.add_argument(
        "-i",
        "--size",
        dest="size_int",
        type=int,
        choices=_SIZES,
        help="size",
        default=UNSET,
    )
    parser.add_argument(
        "-r",
        "--duedate",
        dest="due_at_str",
        help="due date",
        default=UNSET,
    )


def cli() -> None:
    signal.signal(signal.SIGINT, _exit_gracefully)
    global _is_cli
    _is_cli = True

    print_version_update_message_maybe()

    if _VERSION_CMD in sys.argv[1:]:
        print_version()
        return

    parser = ArgumentParser(prog=_PROG, description="A CLI to interact with Dart")
    subparsers = parser.add_subparsers(
        title="command",
        required=True,
        metavar=f"{{{_LOGIN_CMD},{_CREATE_TASK_CMD},{_UPDATE_TASK_CMD},{_BEGIN_TASK_CMD}}}",
    )

    set_host_parser = subparsers.add_parser(_SET_HOST_CMD, aliases="s")
    set_host_parser.add_argument("host", help="the new host: {prod|stag|dev|[URL]}")
    set_host_parser.set_defaults(func=set_host)

    login_parser = subparsers.add_parser(_LOGIN_CMD, aliases="l", help="login")
    login_parser.add_argument(
        "-t", "--token", dest="token", help="your authentication token"
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
    update_task_parser.add_argument(
        "-e", "--title", dest="title", help="task title", default=UNSET
    )
    _add_standard_task_arguments(update_task_parser)
    update_task_parser.set_defaults(func=update_task)

    begin_task_parser = subparsers.add_parser(
        _BEGIN_TASK_CMD, aliases="b", help="begin work on a task"
    )
    begin_task_parser.set_defaults(func=begin_task)

    args = vars(parser.parse_args())
    func = args.pop("func")
    func(**args)
