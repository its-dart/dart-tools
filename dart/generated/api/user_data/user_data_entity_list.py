from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_user_data_entity_list import PaginatedUserDataEntityList
from ...models.user_data_entity_list_entity_kind import UserDataEntityListEntityKind
from ...types import UNSET, Response, Unset


def _get_kwargs(
    entity_kind: UserDataEntityListEntityKind,
    *,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v0/{entityKind}".format(
            entityKind=entity_kind,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedUserDataEntityList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedUserDataEntityList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedUserDataEntityList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    entity_kind: UserDataEntityListEntityKind,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedUserDataEntityList]:
    """
    Args:
        entity_kind (UserDataEntityListEntityKind):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserDataEntityList]
    """

    kwargs = _get_kwargs(
        entity_kind=entity_kind,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity_kind: UserDataEntityListEntityKind,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedUserDataEntityList]:
    """
    Args:
        entity_kind (UserDataEntityListEntityKind):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserDataEntityList
    """

    return sync_detailed(
        entity_kind=entity_kind,
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    entity_kind: UserDataEntityListEntityKind,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedUserDataEntityList]:
    """
    Args:
        entity_kind (UserDataEntityListEntityKind):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserDataEntityList]
    """

    kwargs = _get_kwargs(
        entity_kind=entity_kind,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity_kind: UserDataEntityListEntityKind,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedUserDataEntityList]:
    """
    Args:
        entity_kind (UserDataEntityListEntityKind):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserDataEntityList
    """

    return (
        await asyncio_detailed(
            entity_kind=entity_kind,
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
