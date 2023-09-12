from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.request_body import RequestBody
from ...models.response_body import ResponseBody
from ...models.validation_error_response import ValidationErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    json_body: RequestBody,
    x_csrftoken: str,
) -> Dict[str, Any]:
    headers = {}
    headers["x-csrftoken"] = x_csrftoken

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/api/v0/transactions/create",
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ResponseBody, ValidationErrorResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = ResponseBody.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
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
    json_body: RequestBody,
    x_csrftoken: str,
) -> Response[Union[ResponseBody, ValidationErrorResponse]]:
    """
    Args:
        x_csrftoken (str):
        json_body (RequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ResponseBody, ValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        x_csrftoken=x_csrftoken,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: RequestBody,
    x_csrftoken: str,
) -> Optional[Union[ResponseBody, ValidationErrorResponse]]:
    """
    Args:
        x_csrftoken (str):
        json_body (RequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ResponseBody, ValidationErrorResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        x_csrftoken=x_csrftoken,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RequestBody,
    x_csrftoken: str,
) -> Response[Union[ResponseBody, ValidationErrorResponse]]:
    """
    Args:
        x_csrftoken (str):
        json_body (RequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ResponseBody, ValidationErrorResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        x_csrftoken=x_csrftoken,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: RequestBody,
    x_csrftoken: str,
) -> Optional[Union[ResponseBody, ValidationErrorResponse]]:
    """
    Args:
        x_csrftoken (str):
        json_body (RequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ResponseBody, ValidationErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            x_csrftoken=x_csrftoken,
        )
    ).parsed
