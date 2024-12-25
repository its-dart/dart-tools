from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_doc_list import PaginatedDocList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    editor: Union[Unset, str] = UNSET,
    editor_duid: Union[Unset, str] = UNSET,
    folder: Union[Unset, str] = UNSET,
    folder_duid: Union[Unset, str] = UNSET,
    in_trash: Union[Unset, bool] = UNSET,
    is_draft: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    report_kind: Union[Unset, str] = UNSET,
    subscriber: Union[Unset, str] = UNSET,
    subscriber_duid: Union[Unset, str] = UNSET,
    text: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["editor"] = editor

    params["editor_duid"] = editor_duid

    params["folder"] = folder

    params["folder_duid"] = folder_duid

    params["in_trash"] = in_trash

    params["is_draft"] = is_draft

    params["limit"] = limit

    params["offset"] = offset

    params["report_kind"] = report_kind

    params["subscriber"] = subscriber

    params["subscriber_duid"] = subscriber_duid

    params["text"] = text

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v0/docs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedDocList]:
    if response.status_code == 200:
        response_200 = PaginatedDocList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedDocList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    editor: Union[Unset, str] = UNSET,
    editor_duid: Union[Unset, str] = UNSET,
    folder: Union[Unset, str] = UNSET,
    folder_duid: Union[Unset, str] = UNSET,
    in_trash: Union[Unset, bool] = UNSET,
    is_draft: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    report_kind: Union[Unset, str] = UNSET,
    subscriber: Union[Unset, str] = UNSET,
    subscriber_duid: Union[Unset, str] = UNSET,
    text: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Response[PaginatedDocList]:
    """
    Args:
        editor (Union[Unset, str]):
        editor_duid (Union[Unset, str]):
        folder (Union[Unset, str]):
        folder_duid (Union[Unset, str]):
        in_trash (Union[Unset, bool]):
        is_draft (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        report_kind (Union[Unset, str]):
        subscriber (Union[Unset, str]):
        subscriber_duid (Union[Unset, str]):
        text (Union[Unset, str]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDocList]
    """

    kwargs = _get_kwargs(
        editor=editor,
        editor_duid=editor_duid,
        folder=folder,
        folder_duid=folder_duid,
        in_trash=in_trash,
        is_draft=is_draft,
        limit=limit,
        offset=offset,
        report_kind=report_kind,
        subscriber=subscriber,
        subscriber_duid=subscriber_duid,
        text=text,
        title=title,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    editor: Union[Unset, str] = UNSET,
    editor_duid: Union[Unset, str] = UNSET,
    folder: Union[Unset, str] = UNSET,
    folder_duid: Union[Unset, str] = UNSET,
    in_trash: Union[Unset, bool] = UNSET,
    is_draft: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    report_kind: Union[Unset, str] = UNSET,
    subscriber: Union[Unset, str] = UNSET,
    subscriber_duid: Union[Unset, str] = UNSET,
    text: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Optional[PaginatedDocList]:
    """
    Args:
        editor (Union[Unset, str]):
        editor_duid (Union[Unset, str]):
        folder (Union[Unset, str]):
        folder_duid (Union[Unset, str]):
        in_trash (Union[Unset, bool]):
        is_draft (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        report_kind (Union[Unset, str]):
        subscriber (Union[Unset, str]):
        subscriber_duid (Union[Unset, str]):
        text (Union[Unset, str]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDocList
    """

    return sync_detailed(
        client=client,
        editor=editor,
        editor_duid=editor_duid,
        folder=folder,
        folder_duid=folder_duid,
        in_trash=in_trash,
        is_draft=is_draft,
        limit=limit,
        offset=offset,
        report_kind=report_kind,
        subscriber=subscriber,
        subscriber_duid=subscriber_duid,
        text=text,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    editor: Union[Unset, str] = UNSET,
    editor_duid: Union[Unset, str] = UNSET,
    folder: Union[Unset, str] = UNSET,
    folder_duid: Union[Unset, str] = UNSET,
    in_trash: Union[Unset, bool] = UNSET,
    is_draft: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    report_kind: Union[Unset, str] = UNSET,
    subscriber: Union[Unset, str] = UNSET,
    subscriber_duid: Union[Unset, str] = UNSET,
    text: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Response[PaginatedDocList]:
    """
    Args:
        editor (Union[Unset, str]):
        editor_duid (Union[Unset, str]):
        folder (Union[Unset, str]):
        folder_duid (Union[Unset, str]):
        in_trash (Union[Unset, bool]):
        is_draft (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        report_kind (Union[Unset, str]):
        subscriber (Union[Unset, str]):
        subscriber_duid (Union[Unset, str]):
        text (Union[Unset, str]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDocList]
    """

    kwargs = _get_kwargs(
        editor=editor,
        editor_duid=editor_duid,
        folder=folder,
        folder_duid=folder_duid,
        in_trash=in_trash,
        is_draft=is_draft,
        limit=limit,
        offset=offset,
        report_kind=report_kind,
        subscriber=subscriber,
        subscriber_duid=subscriber_duid,
        text=text,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    editor: Union[Unset, str] = UNSET,
    editor_duid: Union[Unset, str] = UNSET,
    folder: Union[Unset, str] = UNSET,
    folder_duid: Union[Unset, str] = UNSET,
    in_trash: Union[Unset, bool] = UNSET,
    is_draft: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    report_kind: Union[Unset, str] = UNSET,
    subscriber: Union[Unset, str] = UNSET,
    subscriber_duid: Union[Unset, str] = UNSET,
    text: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Optional[PaginatedDocList]:
    """
    Args:
        editor (Union[Unset, str]):
        editor_duid (Union[Unset, str]):
        folder (Union[Unset, str]):
        folder_duid (Union[Unset, str]):
        in_trash (Union[Unset, bool]):
        is_draft (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        report_kind (Union[Unset, str]):
        subscriber (Union[Unset, str]):
        subscriber_duid (Union[Unset, str]):
        text (Union[Unset, str]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDocList
    """

    return (
        await asyncio_detailed(
            client=client,
            editor=editor,
            editor_duid=editor_duid,
            folder=folder,
            folder_duid=folder_duid,
            in_trash=in_trash,
            is_draft=is_draft,
            limit=limit,
            offset=offset,
            report_kind=report_kind,
            subscriber=subscriber,
            subscriber_duid=subscriber_duid,
            text=text,
            title=title,
        )
    ).parsed
