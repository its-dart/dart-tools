from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_status_list import PaginatedStatusList
from ...models.statuses_list_kind import StatusesListKind
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    default_only: Union[Unset, None, bool] = UNSET,
    kind: Union[Unset, None, StatusesListKind] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    property_: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["default_only"] = default_only

    json_kind: Union[Unset, None, str] = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind.value if kind else None

    params["kind"] = json_kind

    params["limit"] = limit

    params["offset"] = offset

    params["property"] = property_

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v0/statuses",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedStatusList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedStatusList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedStatusList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    default_only: Union[Unset, None, bool] = UNSET,
    kind: Union[Unset, None, StatusesListKind] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    property_: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedStatusList]:
    """
    Args:
        default_only (Union[Unset, None, bool]):
        kind (Union[Unset, None, StatusesListKind]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        property_ (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedStatusList]
    """

    kwargs = _get_kwargs(
        default_only=default_only,
        kind=kind,
        limit=limit,
        offset=offset,
        property_=property_,
        title=title,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    default_only: Union[Unset, None, bool] = UNSET,
    kind: Union[Unset, None, StatusesListKind] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    property_: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedStatusList]:
    """
    Args:
        default_only (Union[Unset, None, bool]):
        kind (Union[Unset, None, StatusesListKind]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        property_ (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedStatusList
    """

    return sync_detailed(
        client=client,
        default_only=default_only,
        kind=kind,
        limit=limit,
        offset=offset,
        property_=property_,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    default_only: Union[Unset, None, bool] = UNSET,
    kind: Union[Unset, None, StatusesListKind] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    property_: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedStatusList]:
    """
    Args:
        default_only (Union[Unset, None, bool]):
        kind (Union[Unset, None, StatusesListKind]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        property_ (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedStatusList]
    """

    kwargs = _get_kwargs(
        default_only=default_only,
        kind=kind,
        limit=limit,
        offset=offset,
        property_=property_,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    default_only: Union[Unset, None, bool] = UNSET,
    kind: Union[Unset, None, StatusesListKind] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    property_: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedStatusList]:
    """
    Args:
        default_only (Union[Unset, None, bool]):
        kind (Union[Unset, None, StatusesListKind]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        property_ (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedStatusList
    """

    return (
        await asyncio_detailed(
            client=client,
            default_only=default_only,
            kind=kind,
            limit=limit,
            offset=offset,
            property_=property_,
            title=title,
        )
    ).parsed
