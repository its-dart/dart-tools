import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_task_list import PaginatedTaskList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    assignee: Union[Unset, None, str] = UNSET,
    dartboard: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    due_at: Union[Unset, None, datetime.date] = UNSET,
    in_trash: Union[Unset, None, bool] = UNSET,
    is_draft: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    priority: Union[Unset, None, str] = UNSET,
    size: Union[Unset, None, str] = UNSET,
    start_at: Union[Unset, None, datetime.date] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    subscriber: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["assignee"] = assignee

    params["dartboard"] = dartboard

    params["description"] = description

    json_due_at: Union[Unset, None, str] = UNSET
    if not isinstance(due_at, Unset):
        json_due_at = due_at.isoformat() if due_at else None

    params["dueAt"] = json_due_at

    params["inTrash"] = in_trash

    params["isDraft"] = is_draft

    params["limit"] = limit

    params["offset"] = offset

    params["priority"] = priority

    params["size"] = size

    json_start_at: Union[Unset, None, str] = UNSET
    if not isinstance(start_at, Unset):
        json_start_at = start_at.isoformat() if start_at else None

    params["startAt"] = json_start_at

    params["status"] = status

    params["subscriber"] = subscriber

    params["tag"] = tag

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v0/tasks",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedTaskList]:
    if response.status_code == HTTPStatus.OK:
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
    assignee: Union[Unset, None, str] = UNSET,
    dartboard: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    due_at: Union[Unset, None, datetime.date] = UNSET,
    in_trash: Union[Unset, None, bool] = UNSET,
    is_draft: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    priority: Union[Unset, None, str] = UNSET,
    size: Union[Unset, None, str] = UNSET,
    start_at: Union[Unset, None, datetime.date] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    subscriber: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedTaskList]:
    """
    Args:
        assignee (Union[Unset, None, str]):
        dartboard (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        due_at (Union[Unset, None, datetime.date]):
        in_trash (Union[Unset, None, bool]):
        is_draft (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        priority (Union[Unset, None, str]):
        size (Union[Unset, None, str]):
        start_at (Union[Unset, None, datetime.date]):
        status (Union[Unset, None, str]):
        subscriber (Union[Unset, None, str]):
        tag (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTaskList]
    """

    kwargs = _get_kwargs(
        assignee=assignee,
        dartboard=dartboard,
        description=description,
        due_at=due_at,
        in_trash=in_trash,
        is_draft=is_draft,
        limit=limit,
        offset=offset,
        priority=priority,
        size=size,
        start_at=start_at,
        status=status,
        subscriber=subscriber,
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
    assignee: Union[Unset, None, str] = UNSET,
    dartboard: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    due_at: Union[Unset, None, datetime.date] = UNSET,
    in_trash: Union[Unset, None, bool] = UNSET,
    is_draft: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    priority: Union[Unset, None, str] = UNSET,
    size: Union[Unset, None, str] = UNSET,
    start_at: Union[Unset, None, datetime.date] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    subscriber: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedTaskList]:
    """
    Args:
        assignee (Union[Unset, None, str]):
        dartboard (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        due_at (Union[Unset, None, datetime.date]):
        in_trash (Union[Unset, None, bool]):
        is_draft (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        priority (Union[Unset, None, str]):
        size (Union[Unset, None, str]):
        start_at (Union[Unset, None, datetime.date]):
        status (Union[Unset, None, str]):
        subscriber (Union[Unset, None, str]):
        tag (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTaskList
    """

    return sync_detailed(
        client=client,
        assignee=assignee,
        dartboard=dartboard,
        description=description,
        due_at=due_at,
        in_trash=in_trash,
        is_draft=is_draft,
        limit=limit,
        offset=offset,
        priority=priority,
        size=size,
        start_at=start_at,
        status=status,
        subscriber=subscriber,
        tag=tag,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    assignee: Union[Unset, None, str] = UNSET,
    dartboard: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    due_at: Union[Unset, None, datetime.date] = UNSET,
    in_trash: Union[Unset, None, bool] = UNSET,
    is_draft: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    priority: Union[Unset, None, str] = UNSET,
    size: Union[Unset, None, str] = UNSET,
    start_at: Union[Unset, None, datetime.date] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    subscriber: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedTaskList]:
    """
    Args:
        assignee (Union[Unset, None, str]):
        dartboard (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        due_at (Union[Unset, None, datetime.date]):
        in_trash (Union[Unset, None, bool]):
        is_draft (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        priority (Union[Unset, None, str]):
        size (Union[Unset, None, str]):
        start_at (Union[Unset, None, datetime.date]):
        status (Union[Unset, None, str]):
        subscriber (Union[Unset, None, str]):
        tag (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTaskList]
    """

    kwargs = _get_kwargs(
        assignee=assignee,
        dartboard=dartboard,
        description=description,
        due_at=due_at,
        in_trash=in_trash,
        is_draft=is_draft,
        limit=limit,
        offset=offset,
        priority=priority,
        size=size,
        start_at=start_at,
        status=status,
        subscriber=subscriber,
        tag=tag,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    assignee: Union[Unset, None, str] = UNSET,
    dartboard: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    due_at: Union[Unset, None, datetime.date] = UNSET,
    in_trash: Union[Unset, None, bool] = UNSET,
    is_draft: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    priority: Union[Unset, None, str] = UNSET,
    size: Union[Unset, None, str] = UNSET,
    start_at: Union[Unset, None, datetime.date] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    subscriber: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedTaskList]:
    """
    Args:
        assignee (Union[Unset, None, str]):
        dartboard (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        due_at (Union[Unset, None, datetime.date]):
        in_trash (Union[Unset, None, bool]):
        is_draft (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        priority (Union[Unset, None, str]):
        size (Union[Unset, None, str]):
        start_at (Union[Unset, None, datetime.date]):
        status (Union[Unset, None, str]):
        subscriber (Union[Unset, None, str]):
        tag (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

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
            dartboard=dartboard,
            description=description,
            due_at=due_at,
            in_trash=in_trash,
            is_draft=is_draft,
            limit=limit,
            offset=offset,
            priority=priority,
            size=size,
            start_at=start_at,
            status=status,
            subscriber=subscriber,
            tag=tag,
            title=title,
        )
    ).parsed
