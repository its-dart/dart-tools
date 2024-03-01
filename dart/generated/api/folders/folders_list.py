from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.folders_list_kind import FoldersListKind
from ...models.paginated_folder_list import PaginatedFolderList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    kind: Union[Unset, None, FoldersListKind] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    space: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_kind: Union[Unset, None, str] = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind.value if kind else None

    params["kind"] = json_kind

    params["limit"] = limit

    params["offset"] = offset

    params["space"] = space

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v0/folders",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedFolderList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedFolderList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedFolderList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    kind: Union[Unset, None, FoldersListKind] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    space: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedFolderList]:
    """
    Args:
        kind (Union[Unset, None, FoldersListKind]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        space (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedFolderList]
    """

    kwargs = _get_kwargs(
        kind=kind,
        limit=limit,
        offset=offset,
        space=space,
        title=title,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    kind: Union[Unset, None, FoldersListKind] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    space: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedFolderList]:
    """
    Args:
        kind (Union[Unset, None, FoldersListKind]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        space (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedFolderList
    """

    return sync_detailed(
        client=client,
        kind=kind,
        limit=limit,
        offset=offset,
        space=space,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    kind: Union[Unset, None, FoldersListKind] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    space: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedFolderList]:
    """
    Args:
        kind (Union[Unset, None, FoldersListKind]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        space (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedFolderList]
    """

    kwargs = _get_kwargs(
        kind=kind,
        limit=limit,
        offset=offset,
        space=space,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    kind: Union[Unset, None, FoldersListKind] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    space: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedFolderList]:
    """
    Args:
        kind (Union[Unset, None, FoldersListKind]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        space (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedFolderList
    """

    return (
        await asyncio_detailed(
            client=client,
            kind=kind,
            limit=limit,
            offset=offset,
            space=space,
            title=title,
        )
    ).parsed
