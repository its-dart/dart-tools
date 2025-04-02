from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.request_body import RequestBody
from ...models.response_body import ResponseBody
from ...models.validation_error_response import ValidationErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RequestBody,
    x_csrftoken: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_csrftoken, Unset):
        headers["x-csrftoken"] = x_csrftoken

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v0/transactions/create",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ResponseBody, ValidationErrorResponse]]:
    if response.status_code == 201:
        response_201 = ResponseBody.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = ValidationErrorResponse.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ResponseBody, ValidationErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RequestBody,
    x_csrftoken: Union[Unset, str] = UNSET,
) -> Response[Union[ResponseBody, ValidationErrorResponse]]:
    """
    Args:
        x_csrftoken (Union[Unset, str]):
        body (RequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ResponseBody, ValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_csrftoken=x_csrftoken,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RequestBody,
    x_csrftoken: Union[Unset, str] = UNSET,
) -> Optional[Union[ResponseBody, ValidationErrorResponse]]:
    """
    Args:
        x_csrftoken (Union[Unset, str]):
        body (RequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ResponseBody, ValidationErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        x_csrftoken=x_csrftoken,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RequestBody,
    x_csrftoken: Union[Unset, str] = UNSET,
) -> Response[Union[ResponseBody, ValidationErrorResponse]]:
    """
    Args:
        x_csrftoken (Union[Unset, str]):
        body (RequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ResponseBody, ValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_csrftoken=x_csrftoken,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RequestBody,
    x_csrftoken: Union[Unset, str] = UNSET,
) -> Optional[Union[ResponseBody, ValidationErrorResponse]]:
    """
    Args:
        x_csrftoken (Union[Unset, str]):
        body (RequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ResponseBody, ValidationErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_csrftoken=x_csrftoken,
        )
    ).parsed
