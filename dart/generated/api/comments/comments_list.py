import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_comment_list import PaginatedCommentList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    author: Union[Unset, str] = UNSET,
    author_duid: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    published_at: Union[Unset, datetime.date] = UNSET,
    task: Union[Unset, str] = UNSET,
    task_duid: Union[Unset, str] = UNSET,
    text: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["author"] = author

    params["author_duid"] = author_duid

    params["limit"] = limit

    params["offset"] = offset

    json_published_at: Union[Unset, str] = UNSET
    if not isinstance(published_at, Unset):
        json_published_at = published_at.isoformat()
    params["published_at"] = json_published_at

    params["task"] = task

    params["task_duid"] = task_duid

    params["text"] = text

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v0/comments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedCommentList]:
    if response.status_code == 200:
        response_200 = PaginatedCommentList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedCommentList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    author: Union[Unset, str] = UNSET,
    author_duid: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    published_at: Union[Unset, datetime.date] = UNSET,
    task: Union[Unset, str] = UNSET,
    task_duid: Union[Unset, str] = UNSET,
    text: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Response[PaginatedCommentList]:
    """
    Args:
        author (Union[Unset, str]):
        author_duid (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        published_at (Union[Unset, datetime.date]):
        task (Union[Unset, str]):
        task_duid (Union[Unset, str]):
        text (Union[Unset, str]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCommentList]
    """

    kwargs = _get_kwargs(
        author=author,
        author_duid=author_duid,
        limit=limit,
        offset=offset,
        published_at=published_at,
        task=task,
        task_duid=task_duid,
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
    author: Union[Unset, str] = UNSET,
    author_duid: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    published_at: Union[Unset, datetime.date] = UNSET,
    task: Union[Unset, str] = UNSET,
    task_duid: Union[Unset, str] = UNSET,
    text: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Optional[PaginatedCommentList]:
    """
    Args:
        author (Union[Unset, str]):
        author_duid (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        published_at (Union[Unset, datetime.date]):
        task (Union[Unset, str]):
        task_duid (Union[Unset, str]):
        text (Union[Unset, str]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCommentList
    """

    return sync_detailed(
        client=client,
        author=author,
        author_duid=author_duid,
        limit=limit,
        offset=offset,
        published_at=published_at,
        task=task,
        task_duid=task_duid,
        text=text,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    author: Union[Unset, str] = UNSET,
    author_duid: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    published_at: Union[Unset, datetime.date] = UNSET,
    task: Union[Unset, str] = UNSET,
    task_duid: Union[Unset, str] = UNSET,
    text: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Response[PaginatedCommentList]:
    """
    Args:
        author (Union[Unset, str]):
        author_duid (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        published_at (Union[Unset, datetime.date]):
        task (Union[Unset, str]):
        task_duid (Union[Unset, str]):
        text (Union[Unset, str]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCommentList]
    """

    kwargs = _get_kwargs(
        author=author,
        author_duid=author_duid,
        limit=limit,
        offset=offset,
        published_at=published_at,
        task=task,
        task_duid=task_duid,
        text=text,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    author: Union[Unset, str] = UNSET,
    author_duid: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    published_at: Union[Unset, datetime.date] = UNSET,
    task: Union[Unset, str] = UNSET,
    task_duid: Union[Unset, str] = UNSET,
    text: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
) -> Optional[PaginatedCommentList]:
    """
    Args:
        author (Union[Unset, str]):
        author_duid (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        published_at (Union[Unset, datetime.date]):
        task (Union[Unset, str]):
        task_duid (Union[Unset, str]):
        text (Union[Unset, str]):
        title (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCommentList
    """

    return (
        await asyncio_detailed(
            client=client,
            author=author,
            author_duid=author_duid,
            limit=limit,
            offset=offset,
            published_at=published_at,
            task=task,
            task_duid=task_duid,
            text=text,
            title=title,
        )
    ).parsed
