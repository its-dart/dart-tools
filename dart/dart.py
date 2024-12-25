#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A CLI to interact with the Dart web app."""

# Required for type hinting compatibility when using Python 3.9
from __future__ import annotations
from argparse import ArgumentParser
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
from importlib.metadata import version
from typing import Any, Callable, NoReturn
from webbrowser import open_new_tab

import dateparser
from pick import pick
import requests
import platformdirs

from .exception import DartException
from .generated import Client
from .generated.models import (
    Dartboard,
    DartboardKind,
    DartboardUpdate,
    Folder,
    FolderKind,
    FolderUpdate,
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
from .generated.api.dartboards import dartboards_list
from .generated.api.folders import folders_list
from .generated.api.transactions import transactions_create
from .order_manager import get_orders_between

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
_ROOT_API_URL_FRAG = "/api/v0"
_USER_STATUS_URL_FRAG = _ROOT_API_URL_FRAG + "/user-status"
_USER_DATA_URL_FRAG = _ROOT_API_URL_FRAG + "/user-data?mode=auto"
_COPY_BRANCH_URL_FRAG = _ROOT_API_URL_FRAG + "/vcs/copy-branch-link"
_REPLICATE_SPACE_URL_FRAG_FMT = _ROOT_API_URL_FRAG + "/spaces/replicate/{duid}"
_REPLICATE_DARTBOARD_URL_FRAG_FMT = _ROOT_API_URL_FRAG + "/dartboards/replicate/{duid}"

_AUTH_TOKEN_ENVVAR_KEY = "DART_TOKEN"
_CONFIG_FPATH = platformdirs.user_config_path(_APP)
_CLIENT_DUID_KEY = "clientDuid"
_HOST_KEY = "host"
_HOSTS_KEY = "hosts"
_AUTH_TOKEN_KEY = "authToken"

_DUID_CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits
_NON_ALPHANUM_RE = re.compile(r"[^a-zA-Z0-9-]+")
_REPEATED_DASH_RE = re.compile(r"-{2,}")
_PRIORITY_MAP = {
    0: Priority.CRITICAL,
    1: Priority.HIGH,
    2: Priority.MEDIUM,
    3: Priority.LOW,
}
_SIZES = {1, 2, 3, 5, 8}
_COMPLETED_STATUS_KINDS = {"Finished", "Canceled"}

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


class _Session:
    def __init__(self, config=None):
        self._config = config or _Config()
        self._session = requests.Session()

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

    def get(self, url_frag, *args, **kwargs):
        kwargs["headers"] = self.get_headers() | kwargs.get("headers", {})
        return self._session.get(self._config.host + url_frag, *args, **kwargs)

    def post(self, url_frag, *args, **kwargs):
        kwargs["headers"] = self.get_headers() | kwargs.get("headers", {})
        result = self._session.post(self._config.host + url_frag, *args, **kwargs)
        if result.status_code != 403:
            return result
        kwargs["headers"] = self.get_headers() | kwargs.get("headers", {})
        return self._session.post(self._config.host + url_frag, *args, **kwargs)


class Dart(Client):
    def __init__(self, session=None):
        self._session = session or _Session()
        super().__init__(
            base_url=self._session.get_base_url(),
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
            body=request_body,
        )


class UserBundle:
    def __init__(self, session):
        _log("Loading active tasks")
        response = session.get(_USER_DATA_URL_FRAG)
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
    def task_kinds(self):
        return self._raw["taskKinds"]

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
    _dart_exit(f"Not logged in, run\n\n  {_PROG} {_LOGIN_CMD}\n\nto log in.")


def _unknown_failure_exit() -> NoReturn:
    _dart_exit("Unknown failure, email\n\n  support@itsdart.com\n\nfor help.")


def _check_request_response_and_maybe_exit(response) -> None:
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        if response.status_code in {401, 403}:
            _auth_failure_exit()
        _unknown_failure_exit()


def _parse_transaction_response_and_maybe_exit(
    response, model_kind: str, duid: str
) -> Any:
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


def _get_is_logged_in(session: _Session) -> bool:
    response = session.get(_USER_STATUS_URL_FRAG)
    return response.json().get("isLoggedIn", False)


def is_logged_in(should_raise: bool = False) -> bool:
    session = _Session()

    result = _get_is_logged_in(session)

    if not result and should_raise:
        _auth_failure_exit()
    _log(f"You are {'' if result else 'not '}logged in")
    return result


def login(token: str | None = None) -> bool:
    config = _Config()
    session = _Session(config)

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

    worked = _get_is_logged_in(session)
    if not worked:
        _dart_exit("Invalid token.")

    _log("Logged in.")
    return True


def _begin_task(
    config: _Config, session: _Session, user_email: str, get_task: Callable
) -> bool:
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


def begin_task() -> bool:
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
            _dart_exit("No active, incomplete tasks found.")

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
    title: str,
    *,
    dartboard_duid: str | None = None,
    dartboard_title: str | None = None,
    kind_title: str | None = None,
    status_title: str | None = None,
    assignee_emails: list[str] | None = None,
    tag_titles: list[str] | None = None,
    priority_int: int | None = None,
    size_int: int | None = None,
    due_at_str: str | None = None,
    should_begin: bool = False,
) -> Task:
    config = _Config()
    session = _Session(config)
    dart = Dart(session)

    user_bundle = UserBundle(session)

    user = user_bundle.user
    user_duid = user["duid"]

    dartboards = user_bundle.dartboards
    if dartboard_duid is None:
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
                _dart_exit(f"No dartboard found with title '{dartboard_title}'.")
        else:
            team_space_duid = next(
                e["duid"]
                for e in user_bundle.spaces
                if e["kind"] == SpaceKind.WORKSPACE
            )
            dartboard = next(
                e
                for e in dartboards
                if e["spaceDuid"] == team_space_duid
                and e["kind"] == DartboardKind.ACTIVE
            )
        dartboard_duid = dartboard["duid"]

    orders = [
        e["order"] for e in user_bundle.tasks if e["dartboardDuid"] == dartboard_duid
    ]
    first_order = min(orders) if len(orders) > 0 else None
    order = get_orders_between(None, first_order, 1)[0]

    kinds = user_bundle.task_kinds
    if kind_title is not None:
        kind_title_norm = kind_title.strip().lower()
        kind = next((e for e in kinds if e["title"].lower() == kind_title_norm), None)
        if kind is None:
            _dart_exit(f"No status found with title '{status_title}'.")
    else:
        kind = next(e for e in kinds if e["locked"])
    kind_duid = kind["duid"]

    statuses = user_bundle.default_statuses
    if status_title is not None:
        status_title_norm = status_title.strip().lower()
        status = next(
            (e for e in statuses if e["title"].lower() == status_title_norm), None
        )
        if status is None:
            _dart_exit(f"No status found with title '{status_title}'.")
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
                _dart_exit(f"No user found with email '{assignee_email}'.")
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
                _dart_exit(f"No tag found with title '{tag_title}'.")
            tag_duids.append(tag_titles_to_duids[tag_title_norm])

    priority = None
    if priority_int is not None:
        priority = _PRIORITY_MAP[priority_int]

    size = size_int

    due_at = None
    if due_at_str is not None:
        due_at = dateparser.parse(due_at_str)
        if due_at is None:
            _dart_exit(f"Could not parse due date '{due_at_str}'.")
        due_at = due_at.replace(
            hour=9, minute=0, second=0, microsecond=0, tzinfo=timezone.utc
        )

    task_create = TaskCreate(
        duid=_make_duid(),
        source_type=TaskSourceType.CLI,
        drafter_duid=None,
        dartboard_duid=dartboard_duid,
        order=order,
        kind_duid=kind_duid,
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
    duid: str,
    *,
    title: str | None = None,
    dartboard_duid: str | None = None,
    dartboard_title: str | None = None,
    status_title: str | None = None,
    assignee_emails: list[str] | None = None,
    tag_titles: list[str] | None = None,
    priority_int: int | None = None,
    size_int: int | None = None,
    due_at_str: str | None = None,
) -> Task:
    config = _Config()
    session = _Session(config)
    dart = Dart(session)

    user_bundle = UserBundle(session)

    user = user_bundle.user
    user_duid = user["duid"]

    tasks = user_bundle.tasks
    old_task = next((e for e in tasks if e["duid"] == duid), None)
    if old_task is None:
        _dart_exit(f"No task found with DUID '{duid}'.")

    task_update_kwargs = {"duid": duid}

    if title is not None:
        task_update_kwargs["title"] = title

    dartboards = user_bundle.dartboards
    if dartboard_duid is not None:
        task_update_kwargs["dartboard_duid"] = dartboard_duid
    elif dartboard_title is not None:
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
            _dart_exit(f"No dartboard found with title '{dartboard_title}'.")
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
            _dart_exit(f"No status found with title '{status_title}'.")
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
                _dart_exit(f"No user found with email '{assignee_email}'.")
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
                _dart_exit(f"No tag found with title '{tag_title}'.")
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
            _dart_exit(f"Could not parse due date '{due_at_str}'.")
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


def replicate_space(
    duid: str,
    *,
    title: str | None = None,
    abrev: str | None = None,
    color_hex: str | None = None,
    accessible_by_team: bool | None = None,
    accessor_duids: list[str] | None = None,
) -> str:
    config = _Config()
    session = _Session(config)

    content = {}
    if title is not None:
        content["title"] = title
    if abrev is not None:
        content["abrev"] = abrev
    if color_hex is not None:
        content["colorHex"] = color_hex
    if accessible_by_team is not None:
        content["accessibleByTeam"] = accessible_by_team
    if accessor_duids is not None:
        content["accessorIds"] = accessor_duids
    response = session.post(
        _REPLICATE_SPACE_URL_FRAG_FMT.format(duid=duid), json=content
    )
    _check_request_response_and_maybe_exit(response)

    space_duid = response.json()["duid"]

    _log(f"Replicated space at {_get_space_url(config.host, space_duid)}")
    _log("Done.")
    return space_duid


def get_dartboards(space_duid: str, include_special: bool = False) -> list[Dartboard]:
    dart = Dart()

    response = dartboards_list.sync(client=dart, space_duid=space_duid)
    dartboards = response.results if response is not None else []
    if not include_special:
        dartboards = [e for e in dartboards if e.kind == DartboardKind.CUSTOM]

    _log(f"Got {len(dartboards)} dartboards")
    _log("Done.")
    return dartboards


def replicate_dartboard(duid: str, *, title: str | None = None) -> str:
    config = _Config()
    session = _Session(config)

    content = {}
    if title is not None:
        content["title"] = title
    response = session.post(
        _REPLICATE_DARTBOARD_URL_FRAG_FMT.format(duid=duid), json=content
    )
    _check_request_response_and_maybe_exit(response)

    dartboard_duid = response.json()["duid"]

    _log(f"Replicated dartboard at {_get_dartboard_url(config.host, dartboard_duid)}")
    _log("Done.")
    return dartboard_duid


def update_dartboard(
    duid: str,
    *,
    title: str | None = None,
    color_hex: str | None = None,
) -> Dartboard:
    config = _Config()
    session = _Session(config)
    dart = Dart(session)

    dartboard_update_kwargs = {"duid": duid}

    if title is not None:
        dartboard_update_kwargs["title"] = title
    if color_hex is not None:
        dartboard_update_kwargs["color_hex"] = color_hex

    dartboard_update = DartboardUpdate(**dartboard_update_kwargs)
    dartboard_update_op = Operation(
        model=OperationModelKind.DARTBOARD,
        kind=OperationKind.UPDATE,
        data=dartboard_update,
    )
    response = dart.transact([dartboard_update_op], TransactionKind.DARTBOARD_UPDATE)
    dartboard = _parse_transaction_response_and_maybe_exit(
        response, OperationModelKind.DARTBOARD, dartboard_update.duid
    )

    _log(
        f"Updated dartboard {dartboard.title} at {_get_dartboard_url(config.host, dartboard.duid)}"
    )
    _log("Done.")
    return dartboard


def get_folders(space_duid: str, *, include_special: bool = False) -> list[Folder]:
    dart = Dart()

    response = folders_list.sync(client=dart, space_duid=space_duid)
    folders = response.results if response is not None else []
    if not include_special:
        folders = [e for e in folders if e.kind == FolderKind.OTHER]

    _log(f"Got {len(folders)} folders")
    _log("Done.")
    return folders


def update_folder(
    duid: str,
    *,
    title: str | None = None,
    color_hex: str | None = None,
) -> Folder:
    config = _Config()
    session = _Session(config)
    dart = Dart(session)

    folder_update_kwargs = {"duid": duid}

    if title is not None:
        folder_update_kwargs["title"] = title
    if color_hex is not None:
        folder_update_kwargs["color_hex"] = color_hex

    folder_update = FolderUpdate(**folder_update_kwargs)
    folder_update_op = Operation(
        model=OperationModelKind.FOLDER,
        kind=OperationKind.UPDATE,
        data=folder_update,
    )
    response = dart.transact([folder_update_op], TransactionKind.FOLDER_UPDATE)
    folder = _parse_transaction_response_and_maybe_exit(
        response, OperationModelKind.FOLDER, folder_update.duid
    )

    _log(
        f"Updated folder {folder.title} at {_get_folder_url(config.host, folder.duid)}"
    )
    _log("Done.")
    return folder


def _add_standard_task_arguments(parser: ArgumentParser) -> None:
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
        metavar=f"{{{_LOGIN_CMD},{_CREATE_TASK_CMD},{_BEGIN_TASK_CMD}}}",
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
