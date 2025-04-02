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
    duids: Union[Unset, str] = UNSET,
    finished_at_after: Union[Unset, datetime.datetime] = UNSET,
    finished_at_before: Union[Unset, datetime.datetime] = UNSET,
    kind: Union[Unset, DartboardsListKind] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    space: Union[Unset, str] = UNSET,
    space_duid: Union[Unset, str] = UNSET,
    started_at_after: Union[Unset, datetime.datetime] = UNSET,
    started_at_before: Union[Unset, datetime.datetime] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["duids"] = duids

    json_finished_at_after: Union[Unset, str] = UNSET
    if not isinstance(finished_at_after, Unset):
        json_finished_at_after = finished_at_after.isoformat()
    params["finished_at_after"] = json_finished_at_after

    json_finished_at_before: Union[Unset, str] = UNSET
    if not isinstance(finished_at_before, Unset):
        json_finished_at_before = finished_at_before.isoformat()
    params["finished_at_before"] = json_finished_at_before

    json_kind: Union[Unset, str] = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind.value

    params["kind"] = json_kind

    params["limit"] = limit

    params["offset"] = offset

    params["space"] = space

    params["space_duid"] = space_duid

    json_started_at_after: Union[Unset, str] = UNSET
    if not isinstance(started_at_after, Unset):
        json_started_at_after = started_at_after.isoformat()
    params["started_at_after"] = json_started_at_after

    json_started_at_before: Union[Unset, str] = UNSET
    if not isinstance(started_at_before, Unset):
        json_started_at_before = started_at_before.isoformat()
    params["started_at_before"] = json_started_at_before

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
    duids: Union[Unset, str] = UNSET,
    finished_at_after: Union[Unset, datetime.datetime] = UNSET,
    finished_at_before: Union[Unset, datetime.datetime] = UNSET,
    kind: Union[Unset, DartboardsListKind] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    space: Union[Unset, str] = UNSET,
    space_duid: Union[Unset, str] = UNSET,
    started_at_after: Union[Unset, datetime.datetime] = UNSET,
    started_at_before: Union[Unset, datetime.datetime] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Response[PaginatedDartboardList]:
    """
    Args:
        duids (Union[Unset, str]):
        finished_at_after (Union[Unset, datetime.datetime]):
        finished_at_before (Union[Unset, datetime.datetime]):
        kind (Union[Unset, DartboardsListKind]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        space (Union[Unset, str]):
        space_duid (Union[Unset, str]):
        started_at_after (Union[Unset, datetime.datetime]):
        started_at_before (Union[Unset, datetime.datetime]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDartboardList]
    """

    kwargs = _get_kwargs(
        duids=duids,
        finished_at_after=finished_at_after,
        finished_at_before=finished_at_before,
        kind=kind,
        limit=limit,
        offset=offset,
        space=space,
        space_duid=space_duid,
        started_at_after=started_at_after,
        started_at_before=started_at_before,
        title=title,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    duids: Union[Unset, str] = UNSET,
    finished_at_after: Union[Unset, datetime.datetime] = UNSET,
    finished_at_before: Union[Unset, datetime.datetime] = UNSET,
    kind: Union[Unset, DartboardsListKind] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    space: Union[Unset, str] = UNSET,
    space_duid: Union[Unset, str] = UNSET,
    started_at_after: Union[Unset, datetime.datetime] = UNSET,
    started_at_before: Union[Unset, datetime.datetime] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Optional[PaginatedDartboardList]:
    """
    Args:
        duids (Union[Unset, str]):
        finished_at_after (Union[Unset, datetime.datetime]):
        finished_at_before (Union[Unset, datetime.datetime]):
        kind (Union[Unset, DartboardsListKind]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        space (Union[Unset, str]):
        space_duid (Union[Unset, str]):
        started_at_after (Union[Unset, datetime.datetime]):
        started_at_before (Union[Unset, datetime.datetime]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDartboardList
    """

    return sync_detailed(
        client=client,
        duids=duids,
        finished_at_after=finished_at_after,
        finished_at_before=finished_at_before,
        kind=kind,
        limit=limit,
        offset=offset,
        space=space,
        space_duid=space_duid,
        started_at_after=started_at_after,
        started_at_before=started_at_before,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    duids: Union[Unset, str] = UNSET,
    finished_at_after: Union[Unset, datetime.datetime] = UNSET,
    finished_at_before: Union[Unset, datetime.datetime] = UNSET,
    kind: Union[Unset, DartboardsListKind] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    space: Union[Unset, str] = UNSET,
    space_duid: Union[Unset, str] = UNSET,
    started_at_after: Union[Unset, datetime.datetime] = UNSET,
    started_at_before: Union[Unset, datetime.datetime] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Response[PaginatedDartboardList]:
    """
    Args:
        duids (Union[Unset, str]):
        finished_at_after (Union[Unset, datetime.datetime]):
        finished_at_before (Union[Unset, datetime.datetime]):
        kind (Union[Unset, DartboardsListKind]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        space (Union[Unset, str]):
        space_duid (Union[Unset, str]):
        started_at_after (Union[Unset, datetime.datetime]):
        started_at_before (Union[Unset, datetime.datetime]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDartboardList]
    """

    kwargs = _get_kwargs(
        duids=duids,
        finished_at_after=finished_at_after,
        finished_at_before=finished_at_before,
        kind=kind,
        limit=limit,
        offset=offset,
        space=space,
        space_duid=space_duid,
        started_at_after=started_at_after,
        started_at_before=started_at_before,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    duids: Union[Unset, str] = UNSET,
    finished_at_after: Union[Unset, datetime.datetime] = UNSET,
    finished_at_before: Union[Unset, datetime.datetime] = UNSET,
    kind: Union[Unset, DartboardsListKind] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    space: Union[Unset, str] = UNSET,
    space_duid: Union[Unset, str] = UNSET,
    started_at_after: Union[Unset, datetime.datetime] = UNSET,
    started_at_before: Union[Unset, datetime.datetime] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Optional[PaginatedDartboardList]:
    """
    Args:
        duids (Union[Unset, str]):
        finished_at_after (Union[Unset, datetime.datetime]):
        finished_at_before (Union[Unset, datetime.datetime]):
        kind (Union[Unset, DartboardsListKind]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        space (Union[Unset, str]):
        space_duid (Union[Unset, str]):
        started_at_after (Union[Unset, datetime.datetime]):
        started_at_before (Union[Unset, datetime.datetime]):
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
            duids=duids,
            finished_at_after=finished_at_after,
            finished_at_before=finished_at_before,
            kind=kind,
            limit=limit,
            offset=offset,
            space=space,
            space_duid=space_duid,
            started_at_after=started_at_after,
            started_at_before=started_at_before,
            title=title,
        )
    ).parsed
