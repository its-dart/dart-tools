from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attachment import Attachment
from ...models.comment import Comment
from ...models.comment_reaction import CommentReaction
from ...models.dartboard import Dartboard
from ...models.doc import Doc
from ...models.folder import Folder
from ...models.form import Form
from ...models.form_field import FormField
from ...models.layout import Layout
from ...models.option import Option
from ...models.property_ import Property
from ...models.relationship import Relationship
from ...models.relationship_kind import RelationshipKind
from ...models.space import Space
from ...models.status import Status
from ...models.task import Task
from ...models.task_doc_relationship import TaskDocRelationship
from ...models.task_link import TaskLink
from ...models.tenant import Tenant
from ...models.user import User
from ...models.user_dartboard_layout import UserDartboardLayout
from ...models.user_data_entity_retrieve_entity_kind import UserDataEntityRetrieveEntityKind
from ...models.view import View
from ...types import Response


def _get_kwargs(
    entity_kind: UserDataEntityRetrieveEntityKind,
    entity_duid: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/api/v0/{entityKind}/{entityDuid}".format(
            entityKind=entity_kind,
            entityDuid=entity_duid,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        "Attachment",
        "Comment",
        "CommentReaction",
        "Dartboard",
        "Doc",
        "Folder",
        "Form",
        "FormField",
        "Layout",
        "Option",
        "Property",
        "Relationship",
        "RelationshipKind",
        "Space",
        "Status",
        "Task",
        "TaskDocRelationship",
        "TaskLink",
        "Tenant",
        "User",
        "UserDartboardLayout",
        "View",
    ]
]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(
            data: object,
        ) -> Union[
            "Attachment",
            "Comment",
            "CommentReaction",
            "Dartboard",
            "Doc",
            "Folder",
            "Form",
            "FormField",
            "Layout",
            "Option",
            "Property",
            "Relationship",
            "RelationshipKind",
            "Space",
            "Status",
            "Task",
            "TaskDocRelationship",
            "TaskLink",
            "Tenant",
            "User",
            "UserDartboardLayout",
            "View",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_0 = Attachment.from_dict(data)

                return componentsschemas_user_data_entity_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_1 = Comment.from_dict(data)

                return componentsschemas_user_data_entity_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_2 = CommentReaction.from_dict(data)

                return componentsschemas_user_data_entity_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_3 = User.from_dict(data)

                return componentsschemas_user_data_entity_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_4 = Dartboard.from_dict(data)

                return componentsschemas_user_data_entity_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_5 = Doc.from_dict(data)

                return componentsschemas_user_data_entity_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_6 = Folder.from_dict(data)

                return componentsschemas_user_data_entity_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_7 = Form.from_dict(data)

                return componentsschemas_user_data_entity_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_8 = FormField.from_dict(data)

                return componentsschemas_user_data_entity_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_9 = Layout.from_dict(data)

                return componentsschemas_user_data_entity_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_10 = Option.from_dict(data)

                return componentsschemas_user_data_entity_type_10
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_11 = Property.from_dict(data)

                return componentsschemas_user_data_entity_type_11
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_12 = Relationship.from_dict(data)

                return componentsschemas_user_data_entity_type_12
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_13 = RelationshipKind.from_dict(data)

                return componentsschemas_user_data_entity_type_13
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_14 = Space.from_dict(data)

                return componentsschemas_user_data_entity_type_14
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_15 = Status.from_dict(data)

                return componentsschemas_user_data_entity_type_15
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_16 = Task.from_dict(data)

                return componentsschemas_user_data_entity_type_16
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_17 = TaskDocRelationship.from_dict(data)

                return componentsschemas_user_data_entity_type_17
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_18 = TaskLink.from_dict(data)

                return componentsschemas_user_data_entity_type_18
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_19 = Tenant.from_dict(data)

                return componentsschemas_user_data_entity_type_19
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_data_entity_type_20 = UserDartboardLayout.from_dict(data)

                return componentsschemas_user_data_entity_type_20
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_user_data_entity_type_21 = View.from_dict(data)

            return componentsschemas_user_data_entity_type_21

        response_200 = _parse_response_200(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        "Attachment",
        "Comment",
        "CommentReaction",
        "Dartboard",
        "Doc",
        "Folder",
        "Form",
        "FormField",
        "Layout",
        "Option",
        "Property",
        "Relationship",
        "RelationshipKind",
        "Space",
        "Status",
        "Task",
        "TaskDocRelationship",
        "TaskLink",
        "Tenant",
        "User",
        "UserDartboardLayout",
        "View",
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    entity_kind: UserDataEntityRetrieveEntityKind,
    entity_duid: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        "Attachment",
        "Comment",
        "CommentReaction",
        "Dartboard",
        "Doc",
        "Folder",
        "Form",
        "FormField",
        "Layout",
        "Option",
        "Property",
        "Relationship",
        "RelationshipKind",
        "Space",
        "Status",
        "Task",
        "TaskDocRelationship",
        "TaskLink",
        "Tenant",
        "User",
        "UserDartboardLayout",
        "View",
    ]
]:
    """
    Args:
        entity_kind (UserDataEntityRetrieveEntityKind):
        entity_duid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['Attachment', 'Comment', 'CommentReaction', 'Dartboard', 'Doc', 'Folder', 'Form', 'FormField', 'Layout', 'Option', 'Property', 'Relationship', 'RelationshipKind', 'Space', 'Status', 'Task', 'TaskDocRelationship', 'TaskLink', 'Tenant', 'User', 'UserDartboardLayout', 'View']]
    """

    kwargs = _get_kwargs(
        entity_kind=entity_kind,
        entity_duid=entity_duid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity_kind: UserDataEntityRetrieveEntityKind,
    entity_duid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        "Attachment",
        "Comment",
        "CommentReaction",
        "Dartboard",
        "Doc",
        "Folder",
        "Form",
        "FormField",
        "Layout",
        "Option",
        "Property",
        "Relationship",
        "RelationshipKind",
        "Space",
        "Status",
        "Task",
        "TaskDocRelationship",
        "TaskLink",
        "Tenant",
        "User",
        "UserDartboardLayout",
        "View",
    ]
]:
    """
    Args:
        entity_kind (UserDataEntityRetrieveEntityKind):
        entity_duid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['Attachment', 'Comment', 'CommentReaction', 'Dartboard', 'Doc', 'Folder', 'Form', 'FormField', 'Layout', 'Option', 'Property', 'Relationship', 'RelationshipKind', 'Space', 'Status', 'Task', 'TaskDocRelationship', 'TaskLink', 'Tenant', 'User', 'UserDartboardLayout', 'View']
    """

    return sync_detailed(
        entity_kind=entity_kind,
        entity_duid=entity_duid,
        client=client,
    ).parsed


async def asyncio_detailed(
    entity_kind: UserDataEntityRetrieveEntityKind,
    entity_duid: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        "Attachment",
        "Comment",
        "CommentReaction",
        "Dartboard",
        "Doc",
        "Folder",
        "Form",
        "FormField",
        "Layout",
        "Option",
        "Property",
        "Relationship",
        "RelationshipKind",
        "Space",
        "Status",
        "Task",
        "TaskDocRelationship",
        "TaskLink",
        "Tenant",
        "User",
        "UserDartboardLayout",
        "View",
    ]
]:
    """
    Args:
        entity_kind (UserDataEntityRetrieveEntityKind):
        entity_duid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['Attachment', 'Comment', 'CommentReaction', 'Dartboard', 'Doc', 'Folder', 'Form', 'FormField', 'Layout', 'Option', 'Property', 'Relationship', 'RelationshipKind', 'Space', 'Status', 'Task', 'TaskDocRelationship', 'TaskLink', 'Tenant', 'User', 'UserDartboardLayout', 'View']]
    """

    kwargs = _get_kwargs(
        entity_kind=entity_kind,
        entity_duid=entity_duid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity_kind: UserDataEntityRetrieveEntityKind,
    entity_duid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        "Attachment",
        "Comment",
        "CommentReaction",
        "Dartboard",
        "Doc",
        "Folder",
        "Form",
        "FormField",
        "Layout",
        "Option",
        "Property",
        "Relationship",
        "RelationshipKind",
        "Space",
        "Status",
        "Task",
        "TaskDocRelationship",
        "TaskLink",
        "Tenant",
        "User",
        "UserDartboardLayout",
        "View",
    ]
]:
    """
    Args:
        entity_kind (UserDataEntityRetrieveEntityKind):
        entity_duid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['Attachment', 'Comment', 'CommentReaction', 'Dartboard', 'Doc', 'Folder', 'Form', 'FormField', 'Layout', 'Option', 'Property', 'Relationship', 'RelationshipKind', 'Space', 'Status', 'Task', 'TaskDocRelationship', 'TaskLink', 'Tenant', 'User', 'UserDartboardLayout', 'View']
    """

    return (
        await asyncio_detailed(
            entity_kind=entity_kind,
            entity_duid=entity_duid,
            client=client,
        )
    ).parsed
