from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_option_list import PaginatedOptionList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    default_only: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    property_: Union[Unset, str] = UNSET,
    property_duid: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["default_only"] = default_only

    params["limit"] = limit

    params["offset"] = offset

    params["property"] = property_

    params["property_duid"] = property_duid

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v0/options",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedOptionList]:
    if response.status_code == 200:
        response_200 = PaginatedOptionList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedOptionList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    default_only: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    property_: Union[Unset, str] = UNSET,
    property_duid: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Response[PaginatedOptionList]:
    """
    Args:
        default_only (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        property_ (Union[Unset, str]):
        property_duid (Union[Unset, str]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOptionList]
    """

    kwargs = _get_kwargs(
        default_only=default_only,
        limit=limit,
        offset=offset,
        property_=property_,
        property_duid=property_duid,
        title=title,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    default_only: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    property_: Union[Unset, str] = UNSET,
    property_duid: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Optional[PaginatedOptionList]:
    """
    Args:
        default_only (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        property_ (Union[Unset, str]):
        property_duid (Union[Unset, str]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedOptionList
    """

    return sync_detailed(
        client=client,
        default_only=default_only,
        limit=limit,
        offset=offset,
        property_=property_,
        property_duid=property_duid,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    default_only: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    property_: Union[Unset, str] = UNSET,
    property_duid: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Response[PaginatedOptionList]:
    """
    Args:
        default_only (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        property_ (Union[Unset, str]):
        property_duid (Union[Unset, str]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOptionList]
    """

    kwargs = _get_kwargs(
        default_only=default_only,
        limit=limit,
        offset=offset,
        property_=property_,
        property_duid=property_duid,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    default_only: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    property_: Union[Unset, str] = UNSET,
    property_duid: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Optional[PaginatedOptionList]:
    """
    Args:
        default_only (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        property_ (Union[Unset, str]):
        property_duid (Union[Unset, str]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedOptionList
    """

    return (
        await asyncio_detailed(
            client=client,
            default_only=default_only,
            limit=limit,
            offset=offset,
            property_=property_,
            property_duid=property_duid,
            title=title,
        )
    ).parsed
