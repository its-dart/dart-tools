from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_user_list import PaginatedUserList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    email: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    role: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["email"] = email

    params["limit"] = limit

    params["name"] = name

    params["offset"] = offset

    params["role"] = role

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v0/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedUserList]:
    if response.status_code == 200:
        response_200 = PaginatedUserList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedUserList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    email: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    role: Union[Unset, str] = UNSET,
) -> Response[PaginatedUserList]:
    """
    Args:
        email (Union[Unset, str]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        offset (Union[Unset, int]):
        role (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserList]
    """

    kwargs = _get_kwargs(
        email=email,
        limit=limit,
        name=name,
        offset=offset,
        role=role,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    email: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    role: Union[Unset, str] = UNSET,
) -> Optional[PaginatedUserList]:
    """
    Args:
        email (Union[Unset, str]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        offset (Union[Unset, int]):
        role (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserList
    """

    return sync_detailed(
        client=client,
        email=email,
        limit=limit,
        name=name,
        offset=offset,
        role=role,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    email: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    role: Union[Unset, str] = UNSET,
) -> Response[PaginatedUserList]:
    """
    Args:
        email (Union[Unset, str]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        offset (Union[Unset, int]):
        role (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserList]
    """

    kwargs = _get_kwargs(
        email=email,
        limit=limit,
        name=name,
        offset=offset,
        role=role,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    email: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    role: Union[Unset, str] = UNSET,
) -> Optional[PaginatedUserList]:
    """
    Args:
        email (Union[Unset, str]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        offset (Union[Unset, int]):
        role (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserList
    """

    return (
        await asyncio_detailed(
            client=client,
            email=email,
            limit=limit,
            name=name,
            offset=offset,
            role=role,
        )
    ).parsed
