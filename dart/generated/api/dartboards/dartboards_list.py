import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dartboards_list_kind import DartboardsListKind
from ...models.paginated_dartboard_list import PaginatedDartboardList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    finished_at: Union[Unset, datetime.date] = UNSET,
    kind: Union[Unset, DartboardsListKind] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    space: Union[Unset, str] = UNSET,
    space_duid: Union[Unset, str] = UNSET,
    started_at: Union[Unset, datetime.date] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_finished_at: Union[Unset, str] = UNSET
    if not isinstance(finished_at, Unset):
        json_finished_at = finished_at.isoformat()
    params["finished_at"] = json_finished_at

    json_kind: Union[Unset, str] = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind.value

    params["kind"] = json_kind

    params["limit"] = limit

    params["offset"] = offset

    params["space"] = space

    params["space_duid"] = space_duid

    json_started_at: Union[Unset, str] = UNSET
    if not isinstance(started_at, Unset):
        json_started_at = started_at.isoformat()
    params["started_at"] = json_started_at

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v0/dartboards",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedDartboardList]:
    if response.status_code == 200:
        response_200 = PaginatedDartboardList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedDartboardList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    finished_at: Union[Unset, datetime.date] = UNSET,
    kind: Union[Unset, DartboardsListKind] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    space: Union[Unset, str] = UNSET,
    space_duid: Union[Unset, str] = UNSET,
    started_at: Union[Unset, datetime.date] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Response[PaginatedDartboardList]:
    """
    Args:
        finished_at (Union[Unset, datetime.date]):
        kind (Union[Unset, DartboardsListKind]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        space (Union[Unset, str]):
        space_duid (Union[Unset, str]):
        started_at (Union[Unset, datetime.date]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDartboardList]
    """

    kwargs = _get_kwargs(
        finished_at=finished_at,
        kind=kind,
        limit=limit,
        offset=offset,
        space=space,
        space_duid=space_duid,
        started_at=started_at,
        title=title,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    finished_at: Union[Unset, datetime.date] = UNSET,
    kind: Union[Unset, DartboardsListKind] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    space: Union[Unset, str] = UNSET,
    space_duid: Union[Unset, str] = UNSET,
    started_at: Union[Unset, datetime.date] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Optional[PaginatedDartboardList]:
    """
    Args:
        finished_at (Union[Unset, datetime.date]):
        kind (Union[Unset, DartboardsListKind]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        space (Union[Unset, str]):
        space_duid (Union[Unset, str]):
        started_at (Union[Unset, datetime.date]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDartboardList
    """

    return sync_detailed(
        client=client,
        finished_at=finished_at,
        kind=kind,
        limit=limit,
        offset=offset,
        space=space,
        space_duid=space_duid,
        started_at=started_at,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    finished_at: Union[Unset, datetime.date] = UNSET,
    kind: Union[Unset, DartboardsListKind] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    space: Union[Unset, str] = UNSET,
    space_duid: Union[Unset, str] = UNSET,
    started_at: Union[Unset, datetime.date] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Response[PaginatedDartboardList]:
    """
    Args:
        finished_at (Union[Unset, datetime.date]):
        kind (Union[Unset, DartboardsListKind]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        space (Union[Unset, str]):
        space_duid (Union[Unset, str]):
        started_at (Union[Unset, datetime.date]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDartboardList]
    """

    kwargs = _get_kwargs(
        finished_at=finished_at,
        kind=kind,
        limit=limit,
        offset=offset,
        space=space,
        space_duid=space_duid,
        started_at=started_at,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    finished_at: Union[Unset, datetime.date] = UNSET,
    kind: Union[Unset, DartboardsListKind] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    space: Union[Unset, str] = UNSET,
    space_duid: Union[Unset, str] = UNSET,
    started_at: Union[Unset, datetime.date] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Optional[PaginatedDartboardList]:
    """
    Args:
        finished_at (Union[Unset, datetime.date]):
        kind (Union[Unset, DartboardsListKind]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        space (Union[Unset, str]):
        space_duid (Union[Unset, str]):
        started_at (Union[Unset, datetime.date]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDartboardList
    """

    return (
        await asyncio_detailed(
            client=client,
            finished_at=finished_at,
            kind=kind,
            limit=limit,
            offset=offset,
            space=space,
            space_duid=space_duid,
            started_at=started_at,
            title=title,
        )
    ).parsed
