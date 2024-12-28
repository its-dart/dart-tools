from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_task_kind_list import PaginatedTaskKindList
from ...models.task_kinds_list_kind import TaskKindsListKind
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    kind: Union[Unset, TaskKindsListKind] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_kind: Union[Unset, str] = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind.value

    params["kind"] = json_kind

    params["limit"] = limit

    params["offset"] = offset

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v0/task-kinds",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedTaskKindList]:
    if response.status_code == 200:
        response_200 = PaginatedTaskKindList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedTaskKindList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    kind: Union[Unset, TaskKindsListKind] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Response[PaginatedTaskKindList]:
    """
    Args:
        kind (Union[Unset, TaskKindsListKind]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTaskKindList]
    """

    kwargs = _get_kwargs(
        kind=kind,
        limit=limit,
        offset=offset,
        title=title,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    kind: Union[Unset, TaskKindsListKind] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Optional[PaginatedTaskKindList]:
    """
    Args:
        kind (Union[Unset, TaskKindsListKind]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTaskKindList
    """

    return sync_detailed(
        client=client,
        kind=kind,
        limit=limit,
        offset=offset,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    kind: Union[Unset, TaskKindsListKind] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Response[PaginatedTaskKindList]:
    """
    Args:
        kind (Union[Unset, TaskKindsListKind]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTaskKindList]
    """

    kwargs = _get_kwargs(
        kind=kind,
        limit=limit,
        offset=offset,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    kind: Union[Unset, TaskKindsListKind] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Optional[PaginatedTaskKindList]:
    """
    Args:
        kind (Union[Unset, TaskKindsListKind]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTaskKindList
    """

    return (
        await asyncio_detailed(
            client=client,
            kind=kind,
            limit=limit,
            offset=offset,
            title=title,
        )
    ).parsed
