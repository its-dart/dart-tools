import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_task_list import PaginatedTaskList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    assignee: Union[Unset, str] = UNSET,
    assignee_duid: Union[Unset, str] = UNSET,
    dartboard: Union[Unset, str] = UNSET,
    dartboard_duid: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    due_at: Union[Unset, datetime.date] = UNSET,
    in_trash: Union[Unset, bool] = UNSET,
    is_draft: Union[Unset, bool] = UNSET,
    kind: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    priority: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
    start_at: Union[Unset, datetime.date] = UNSET,
    status: Union[Unset, str] = UNSET,
    status_duid: Union[Unset, str] = UNSET,
    subscriber: Union[Unset, str] = UNSET,
    subscriber_duid: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["assignee"] = assignee

    params["assignee_duid"] = assignee_duid

    params["dartboard"] = dartboard

    params["dartboard_duid"] = dartboard_duid

    params["description"] = description

    json_due_at: Union[Unset, str] = UNSET
    if not isinstance(due_at, Unset):
        json_due_at = due_at.isoformat()
    params["due_at"] = json_due_at

    params["in_trash"] = in_trash

    params["is_draft"] = is_draft

    params["kind"] = kind

    params["limit"] = limit

    params["offset"] = offset

    params["priority"] = priority

    params["size"] = size

    json_start_at: Union[Unset, str] = UNSET
    if not isinstance(start_at, Unset):
        json_start_at = start_at.isoformat()
    params["start_at"] = json_start_at

    params["status"] = status

    params["status_duid"] = status_duid

    params["subscriber"] = subscriber

    params["subscriber_duid"] = subscriber_duid

    params["tag"] = tag

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v0/tasks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedTaskList]:
    if response.status_code == 200:
        response_200 = PaginatedTaskList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedTaskList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    assignee: Union[Unset, str] = UNSET,
    assignee_duid: Union[Unset, str] = UNSET,
    dartboard: Union[Unset, str] = UNSET,
    dartboard_duid: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    due_at: Union[Unset, datetime.date] = UNSET,
    in_trash: Union[Unset, bool] = UNSET,
    is_draft: Union[Unset, bool] = UNSET,
    kind: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    priority: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
    start_at: Union[Unset, datetime.date] = UNSET,
    status: Union[Unset, str] = UNSET,
    status_duid: Union[Unset, str] = UNSET,
    subscriber: Union[Unset, str] = UNSET,
    subscriber_duid: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Response[PaginatedTaskList]:
    """
    Args:
        assignee (Union[Unset, str]):
        assignee_duid (Union[Unset, str]):
        dartboard (Union[Unset, str]):
        dartboard_duid (Union[Unset, str]):
        description (Union[Unset, str]):
        due_at (Union[Unset, datetime.date]):
        in_trash (Union[Unset, bool]):
        is_draft (Union[Unset, bool]):
        kind (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        priority (Union[Unset, str]):
        size (Union[Unset, int]):
        start_at (Union[Unset, datetime.date]):
        status (Union[Unset, str]):
        status_duid (Union[Unset, str]):
        subscriber (Union[Unset, str]):
        subscriber_duid (Union[Unset, str]):
        tag (Union[Unset, str]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTaskList]
    """

    kwargs = _get_kwargs(
        assignee=assignee,
        assignee_duid=assignee_duid,
        dartboard=dartboard,
        dartboard_duid=dartboard_duid,
        description=description,
        due_at=due_at,
        in_trash=in_trash,
        is_draft=is_draft,
        kind=kind,
        limit=limit,
        offset=offset,
        priority=priority,
        size=size,
        start_at=start_at,
        status=status,
        status_duid=status_duid,
        subscriber=subscriber,
        subscriber_duid=subscriber_duid,
        tag=tag,
        title=title,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    assignee: Union[Unset, str] = UNSET,
    assignee_duid: Union[Unset, str] = UNSET,
    dartboard: Union[Unset, str] = UNSET,
    dartboard_duid: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    due_at: Union[Unset, datetime.date] = UNSET,
    in_trash: Union[Unset, bool] = UNSET,
    is_draft: Union[Unset, bool] = UNSET,
    kind: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    priority: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
    start_at: Union[Unset, datetime.date] = UNSET,
    status: Union[Unset, str] = UNSET,
    status_duid: Union[Unset, str] = UNSET,
    subscriber: Union[Unset, str] = UNSET,
    subscriber_duid: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Optional[PaginatedTaskList]:
    """
    Args:
        assignee (Union[Unset, str]):
        assignee_duid (Union[Unset, str]):
        dartboard (Union[Unset, str]):
        dartboard_duid (Union[Unset, str]):
        description (Union[Unset, str]):
        due_at (Union[Unset, datetime.date]):
        in_trash (Union[Unset, bool]):
        is_draft (Union[Unset, bool]):
        kind (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        priority (Union[Unset, str]):
        size (Union[Unset, int]):
        start_at (Union[Unset, datetime.date]):
        status (Union[Unset, str]):
        status_duid (Union[Unset, str]):
        subscriber (Union[Unset, str]):
        subscriber_duid (Union[Unset, str]):
        tag (Union[Unset, str]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTaskList
    """

    return sync_detailed(
        client=client,
        assignee=assignee,
        assignee_duid=assignee_duid,
        dartboard=dartboard,
        dartboard_duid=dartboard_duid,
        description=description,
        due_at=due_at,
        in_trash=in_trash,
        is_draft=is_draft,
        kind=kind,
        limit=limit,
        offset=offset,
        priority=priority,
        size=size,
        start_at=start_at,
        status=status,
        status_duid=status_duid,
        subscriber=subscriber,
        subscriber_duid=subscriber_duid,
        tag=tag,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    assignee: Union[Unset, str] = UNSET,
    assignee_duid: Union[Unset, str] = UNSET,
    dartboard: Union[Unset, str] = UNSET,
    dartboard_duid: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    due_at: Union[Unset, datetime.date] = UNSET,
    in_trash: Union[Unset, bool] = UNSET,
    is_draft: Union[Unset, bool] = UNSET,
    kind: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    priority: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
    start_at: Union[Unset, datetime.date] = UNSET,
    status: Union[Unset, str] = UNSET,
    status_duid: Union[Unset, str] = UNSET,
    subscriber: Union[Unset, str] = UNSET,
    subscriber_duid: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Response[PaginatedTaskList]:
    """
    Args:
        assignee (Union[Unset, str]):
        assignee_duid (Union[Unset, str]):
        dartboard (Union[Unset, str]):
        dartboard_duid (Union[Unset, str]):
        description (Union[Unset, str]):
        due_at (Union[Unset, datetime.date]):
        in_trash (Union[Unset, bool]):
        is_draft (Union[Unset, bool]):
        kind (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        priority (Union[Unset, str]):
        size (Union[Unset, int]):
        start_at (Union[Unset, datetime.date]):
        status (Union[Unset, str]):
        status_duid (Union[Unset, str]):
        subscriber (Union[Unset, str]):
        subscriber_duid (Union[Unset, str]):
        tag (Union[Unset, str]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTaskList]
    """

    kwargs = _get_kwargs(
        assignee=assignee,
        assignee_duid=assignee_duid,
        dartboard=dartboard,
        dartboard_duid=dartboard_duid,
        description=description,
        due_at=due_at,
        in_trash=in_trash,
        is_draft=is_draft,
        kind=kind,
        limit=limit,
        offset=offset,
        priority=priority,
        size=size,
        start_at=start_at,
        status=status,
        status_duid=status_duid,
        subscriber=subscriber,
        subscriber_duid=subscriber_duid,
        tag=tag,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    assignee: Union[Unset, str] = UNSET,
    assignee_duid: Union[Unset, str] = UNSET,
    dartboard: Union[Unset, str] = UNSET,
    dartboard_duid: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    due_at: Union[Unset, datetime.date] = UNSET,
    in_trash: Union[Unset, bool] = UNSET,
    is_draft: Union[Unset, bool] = UNSET,
    kind: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    priority: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
    start_at: Union[Unset, datetime.date] = UNSET,
    status: Union[Unset, str] = UNSET,
    status_duid: Union[Unset, str] = UNSET,
    subscriber: Union[Unset, str] = UNSET,
    subscriber_duid: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Optional[PaginatedTaskList]:
    """
    Args:
        assignee (Union[Unset, str]):
        assignee_duid (Union[Unset, str]):
        dartboard (Union[Unset, str]):
        dartboard_duid (Union[Unset, str]):
        description (Union[Unset, str]):
        due_at (Union[Unset, datetime.date]):
        in_trash (Union[Unset, bool]):
        is_draft (Union[Unset, bool]):
        kind (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        priority (Union[Unset, str]):
        size (Union[Unset, int]):
        start_at (Union[Unset, datetime.date]):
        status (Union[Unset, str]):
        status_duid (Union[Unset, str]):
        subscriber (Union[Unset, str]):
        subscriber_duid (Union[Unset, str]):
        tag (Union[Unset, str]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTaskList
    """

    return (
        await asyncio_detailed(
            client=client,
            assignee=assignee,
            assignee_duid=assignee_duid,
            dartboard=dartboard,
            dartboard_duid=dartboard_duid,
            description=description,
            due_at=due_at,
            in_trash=in_trash,
            is_draft=is_draft,
            kind=kind,
            limit=limit,
            offset=offset,
            priority=priority,
            size=size,
            start_at=start_at,
            status=status,
            status_duid=status_duid,
            subscriber=subscriber,
            subscriber_duid=subscriber_duid,
            tag=tag,
            title=title,
        )
    ).parsed
