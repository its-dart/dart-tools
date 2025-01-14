from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_space_list import PaginatedSpaceList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    abrev: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["abrev"] = abrev

    params["description"] = description

    params["limit"] = limit

    params["offset"] = offset

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v0/spaces",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedSpaceList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedSpaceList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedSpaceList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    abrev: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Response[PaginatedSpaceList]:
    """
    Args:
        abrev (Union[Unset, str]):
        description (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedSpaceList]
    """

    kwargs = _get_kwargs(
        abrev=abrev,
        description=description,
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
    abrev: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Optional[PaginatedSpaceList]:
    """
    Args:
        abrev (Union[Unset, str]):
        description (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedSpaceList
    """

    return sync_detailed(
        client=client,
        abrev=abrev,
        description=description,
        limit=limit,
        offset=offset,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    abrev: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Response[PaginatedSpaceList]:
    """
    Args:
        abrev (Union[Unset, str]):
        description (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedSpaceList]
    """

    kwargs = _get_kwargs(
        abrev=abrev,
        description=description,
        limit=limit,
        offset=offset,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    abrev: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Optional[PaginatedSpaceList]:
    """
    Args:
        abrev (Union[Unset, str]):
        description (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedSpaceList
    """

    return (
        await asyncio_detailed(
            client=client,
            abrev=abrev,
            description=description,
            limit=limit,
            offset=offset,
            title=title,
        )
    ).parsed
