import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_comment_list import PaginatedCommentList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    author: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    published_at: Union[Unset, None, datetime.date] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    text: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["author"] = author

    params["limit"] = limit

    params["offset"] = offset

    json_published_at: Union[Unset, None, str] = UNSET
    if not isinstance(published_at, Unset):
        json_published_at = published_at.isoformat() if published_at else None

    params["published_at"] = json_published_at

    params["task"] = task

    params["text"] = text

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v0/comments",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedCommentList]:
    if response.status_code == HTTPStatus.OK:
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
    author: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    published_at: Union[Unset, None, datetime.date] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    text: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedCommentList]:
    """
    Args:
        author (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        published_at (Union[Unset, None, datetime.date]):
        task (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCommentList]
    """

    kwargs = _get_kwargs(
        author=author,
        limit=limit,
        offset=offset,
        published_at=published_at,
        task=task,
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
    author: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    published_at: Union[Unset, None, datetime.date] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    text: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedCommentList]:
    """
    Args:
        author (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        published_at (Union[Unset, None, datetime.date]):
        task (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCommentList
    """

    return sync_detailed(
        client=client,
        author=author,
        limit=limit,
        offset=offset,
        published_at=published_at,
        task=task,
        text=text,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    author: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    published_at: Union[Unset, None, datetime.date] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    text: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedCommentList]:
    """
    Args:
        author (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        published_at (Union[Unset, None, datetime.date]):
        task (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCommentList]
    """

    kwargs = _get_kwargs(
        author=author,
        limit=limit,
        offset=offset,
        published_at=published_at,
        task=task,
        text=text,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    author: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    published_at: Union[Unset, None, datetime.date] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    text: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedCommentList]:
    """
    Args:
        author (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        published_at (Union[Unset, None, datetime.date]):
        task (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

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
            limit=limit,
            offset=offset,
            published_at=published_at,
            task=task,
            text=text,
            title=title,
        )
    ).parsed
