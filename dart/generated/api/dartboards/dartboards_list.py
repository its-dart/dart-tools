import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dartboards_list_kind import DartboardsListKind
from ...models.paginated_dartboard_list import PaginatedDartboardList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    finished_at: Union[Unset, None, datetime.date] = UNSET,
    kind: Union[Unset, None, DartboardsListKind] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    space: Union[Unset, None, str] = UNSET,
    started_at: Union[Unset, None, datetime.date] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_finished_at: Union[Unset, None, str] = UNSET
    if not isinstance(finished_at, Unset):
        json_finished_at = finished_at.isoformat() if finished_at else None

    params["finishedAt"] = json_finished_at

    json_kind: Union[Unset, None, str] = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind.value if kind else None

    params["kind"] = json_kind

    params["limit"] = limit

    params["offset"] = offset

    params["space"] = space

    json_started_at: Union[Unset, None, str] = UNSET
    if not isinstance(started_at, Unset):
        json_started_at = started_at.isoformat() if started_at else None

    params["startedAt"] = json_started_at

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v0/dartboards",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedDartboardList]:
    if response.status_code == HTTPStatus.OK:
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
    finished_at: Union[Unset, None, datetime.date] = UNSET,
    kind: Union[Unset, None, DartboardsListKind] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    space: Union[Unset, None, str] = UNSET,
    started_at: Union[Unset, None, datetime.date] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedDartboardList]:
    """
    Args:
        finished_at (Union[Unset, None, datetime.date]):
        kind (Union[Unset, None, DartboardsListKind]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        space (Union[Unset, None, str]):
        started_at (Union[Unset, None, datetime.date]):
        title (Union[Unset, None, str]):

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
    finished_at: Union[Unset, None, datetime.date] = UNSET,
    kind: Union[Unset, None, DartboardsListKind] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    space: Union[Unset, None, str] = UNSET,
    started_at: Union[Unset, None, datetime.date] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedDartboardList]:
    """
    Args:
        finished_at (Union[Unset, None, datetime.date]):
        kind (Union[Unset, None, DartboardsListKind]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        space (Union[Unset, None, str]):
        started_at (Union[Unset, None, datetime.date]):
        title (Union[Unset, None, str]):

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
        started_at=started_at,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    finished_at: Union[Unset, None, datetime.date] = UNSET,
    kind: Union[Unset, None, DartboardsListKind] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    space: Union[Unset, None, str] = UNSET,
    started_at: Union[Unset, None, datetime.date] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedDartboardList]:
    """
    Args:
        finished_at (Union[Unset, None, datetime.date]):
        kind (Union[Unset, None, DartboardsListKind]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        space (Union[Unset, None, str]):
        started_at (Union[Unset, None, datetime.date]):
        title (Union[Unset, None, str]):

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
        started_at=started_at,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    finished_at: Union[Unset, None, datetime.date] = UNSET,
    kind: Union[Unset, None, DartboardsListKind] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    space: Union[Unset, None, str] = UNSET,
    started_at: Union[Unset, None, datetime.date] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedDartboardList]:
    """
    Args:
        finished_at (Union[Unset, None, datetime.date]):
        kind (Union[Unset, None, DartboardsListKind]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        space (Union[Unset, None, str]):
        started_at (Union[Unset, None, datetime.date]):
        title (Union[Unset, None, str]):

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
            started_at=started_at,
            title=title,
        )
    ).parsed
