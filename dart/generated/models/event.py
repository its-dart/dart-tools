from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.entity_name import EntityName
from ..models.event_actor import EventActor
from ..models.event_kind import EventKind

T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """
    Attributes:
        message_frags (Union[None, list[Any]]):
        kind (EventKind): * `tasks/create` - TASK_CREATE
            * `tasks/update_assignees` - TASK_UPDATE_ASSIGNEES
            * `tasks/update_status` - TASK_UPDATE_STATUS
            * `tasks/update_title` - TASK_UPDATE_TITLE
            * `tasks/update_description` - TASK_UPDATE_DESCRIPTION
            * `tasks/set_relationship` - TASK_SET_RELATIONSHIP
            * `tasks/remove_relationship` - TASK_REMOVE_RELATIONSHIP
            * `tasks/update_subscriptions` - TASK_UPDATE_SUBSCRIPTIONS
            * `tasks/update_other` - TASK_UPDATE_OTHER
            * `tasks/comment` - TASK_COMMENT
            * `tasks/due_date_tomorrow` - TASK_DUE_DATE_TOMORROW
            * `tasks/reminder_now` - TASK_REMINDER_NOW
            * `tasks/delete` - TASK_DELETE
            * `tasks/delete_fully` - TASK_DELETE_FULLY
            * `docs/create` - DOC_CREATE
            * `docs/update_title` - DOC_UPDATE_TITLE
            * `docs/update_other` - DOC_UPDATE_OTHER
            * `docs/delete` - DOC_DELETE
            * `pages/create` - PAGE_CREATE
            * `pages/update_title` - PAGE_UPDATE_TITLE
            * `pages/update_permissions` - PAGE_UPDATE_PERMISSIONS
            * `pages/update_other` - PAGE_UPDATE_OTHER
            * `pages/rollover` - DARTBOARD_ROLLOVER
            * `pages/delete` - PAGE_DELETE
            * `workspace/invite` - WORKSPACE_INVITE
            * `workspace/join` - WORKSPACE_JOIN
            * `workspace/update_role` - WORKSPACE_UPDATE_ROLE
            * `workspace/leave` - WORKSPACE_LEAVE
            * `workspace/update_property` - WORKSPACE_UPDATE_PROPERTY
            * `workspace/update_status` - WORKSPACE_UPDATE_STATUS
            * `workspace/update_other` - WORKSPACE_UPDATE_OTHER
            * `workspace/create` - WORKSPACE_CREATE
            * `workspace/data_import` - WORKSPACE_DATA_IMPORT
            * `workspace/data_export` - WORKSPACE_DATA_EXPORT
            * `workspace/delete` - WORKSPACE_DELETE
            * `workspace/upgrade` - WORKSPACE_UPGRADE
            * `workspace/downgrade_initialize` - WORKSPACE_DOWNGRADE_INITIALIZE
            * `workspace/downgrade_finalize` - WORKSPACE_DOWNGRADE_FINALIZE
            * `workspace/become_active` - WORKSPACE_BECOME_ACTIVE
            * `workspace/become_inactive` - WORKSPACE_BECOME_INACTIVE
            * `load/app` - LOAD_APP
            * `load/authenticate` - AUTHENTICATE
            * `load/unidle` - UNIDLE
            * `load/signup` - LOAD_SIGNUP
            * `profile/create` - PROFILE_CREATE
            * `profile/update` - PROFILE_UPDATE
            * `profile/delete` - PROFILE_DELETE
            * `profile/become_active` - PROFILE_BECOME_ACTIVE
            * `profile/become_inactive` - PROFILE_BECOME_INACTIVE
            * `onboarding/finish_step` - ONBOARDING_FINISH_STEP
            * `ai/props` - AI_PROPS
            * `ai/subtasks` - AI_SUBTASKS
            * `ai/content` - AI_CONTENT
            * `ai/translate` - AI_TRANSLATE
            * `ai/emoji` - AI_EMOJI
            * `ai/feedback` - AI_FEEDBACK
            * `ai/icon` - AI_ICON
            * `ai/report` - AI_REPORT
            * `ai/plan` - AI_PLAN
            * `ai/brainstorm_start` - AI_BRAINSTORM_START
            * `ai/detect_duplicates` - AI_DETECT_DUPLICATES
            * `ai/filters` - AI_FILTERS
            * `ai/execute` - AI_EXECUTE
            * `ai/image` - AI_IMAGE
            * `brainstorm/start` - BRAINSTORM_START
            * `brainstorm/stop` - BRAINSTORM_STOP
            * `help/resource_click` - HELP_RESOURCE_CLICK
            * `usage/submit_feedback` - USAGE_SUBMIT_FEEDBACK
            * `usage/undo` - USAGE_UNDO
            * `usage/redo` - USAGE_REDO
            * `usage/open_command_center` - USAGE_OPEN_COMMAND_CENTER
            * `usage/open_rightbar` - USAGE_OPEN_RIGHTBAR
            * `usage/open_fullscreen` - USAGE_OPEN_FULLSCREEN
            * `usage/open_task_overlay` - USAGE_OPEN_TASK_OVERLAY
            * `usage/copy_task_link` - USAGE_COPY_TASK_LINK
            * `usage/copy_branch` - USAGE_COPY_BRANCH
            * `usage/open_search` - USAGE_OPEN_SEARCH
            * `usage/nlp_raw_create` - USAGE_NLP_RAW_CREATE
            * `usage/nlp_raw_delete` - USAGE_NLP_RAW_DELETE
            * `usage/nlp_typeahead_open` - USAGE_NLP_TYPEAHEAD_OPEN
            * `usage/nlp_typeahead_accept` - USAGE_NLP_TYPEAHEAD_ACCEPT
        actor_duid (Union[None, str]):
        actor_str (Union[EventActor, None]):
        main_entity_name (EntityName): * `comment` - COMMENT
            * `task` - TASK
            * `dartboard` - DARTBOARD
            * `dashboard` - DASHBOARD
            * `view` - VIEW
            * `space` - SPACE
            * `doc` - DOC
            * `folder` - FOLDER
            * `form` - FORM
            * `brainstorm` - BRAINSTORM
            * `property` - PROPERTY
            * `status` - STATUS
            * `tenant` - TENANT
            * `user` - USER
            * `UNKNOWN` - UNKNOWN
        comment_duid (Union[None, str]):
        task_duid (Union[None, str]):
        dartboard_duid (Union[None, str]):
        dashboard_duid (Union[None, str]):
        view_duid (Union[None, str]):
        space_duid (Union[None, str]):
        doc_duid (Union[None, str]):
        folder_duid (Union[None, str]):
        form_duid (Union[None, str]):
        brainstorm_duid (Union[None, str]):
        property_duid (Union[None, str]):
        status_duid (Union[None, str]):
        user_duid (Union[None, str]):
        adtl (Any):
    """

    message_frags: Union[None, list[Any]]
    kind: EventKind
    actor_duid: Union[None, str]
    actor_str: Union[EventActor, None]
    main_entity_name: EntityName
    comment_duid: Union[None, str]
    task_duid: Union[None, str]
    dartboard_duid: Union[None, str]
    dashboard_duid: Union[None, str]
    view_duid: Union[None, str]
    space_duid: Union[None, str]
    doc_duid: Union[None, str]
    folder_duid: Union[None, str]
    form_duid: Union[None, str]
    brainstorm_duid: Union[None, str]
    property_duid: Union[None, str]
    status_duid: Union[None, str]
    user_duid: Union[None, str]
    adtl: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_frags: Union[None, list[Any]]
        if isinstance(self.message_frags, list):
            message_frags = self.message_frags

        else:
            message_frags = self.message_frags

        kind = self.kind.value

        actor_duid: Union[None, str]
        actor_duid = self.actor_duid

        actor_str: Union[None, str]
        if isinstance(self.actor_str, EventActor):
            actor_str = self.actor_str.value
        else:
            actor_str = self.actor_str

        main_entity_name = self.main_entity_name.value

        comment_duid: Union[None, str]
        comment_duid = self.comment_duid

        task_duid: Union[None, str]
        task_duid = self.task_duid

        dartboard_duid: Union[None, str]
        dartboard_duid = self.dartboard_duid

        dashboard_duid: Union[None, str]
        dashboard_duid = self.dashboard_duid

        view_duid: Union[None, str]
        view_duid = self.view_duid

        space_duid: Union[None, str]
        space_duid = self.space_duid

        doc_duid: Union[None, str]
        doc_duid = self.doc_duid

        folder_duid: Union[None, str]
        folder_duid = self.folder_duid

        form_duid: Union[None, str]
        form_duid = self.form_duid

        brainstorm_duid: Union[None, str]
        brainstorm_duid = self.brainstorm_duid

        property_duid: Union[None, str]
        property_duid = self.property_duid

        status_duid: Union[None, str]
        status_duid = self.status_duid

        user_duid: Union[None, str]
        user_duid = self.user_duid

        adtl = self.adtl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messageFrags": message_frags,
                "kind": kind,
                "actorDuid": actor_duid,
                "actorStr": actor_str,
                "mainEntityName": main_entity_name,
                "commentDuid": comment_duid,
                "taskDuid": task_duid,
                "dartboardDuid": dartboard_duid,
                "dashboardDuid": dashboard_duid,
                "viewDuid": view_duid,
                "spaceDuid": space_duid,
                "docDuid": doc_duid,
                "folderDuid": folder_duid,
                "formDuid": form_duid,
                "brainstormDuid": brainstorm_duid,
                "propertyDuid": property_duid,
                "statusDuid": status_duid,
                "userDuid": user_duid,
                "adtl": adtl,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_message_frags(data: object) -> Union[None, list[Any]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                message_frags_type_0 = cast(list[Any], data)

                return message_frags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[Any]], data)

        message_frags = _parse_message_frags(d.pop("messageFrags"))

        kind = EventKind(d.pop("kind"))

        def _parse_actor_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        actor_duid = _parse_actor_duid(d.pop("actorDuid"))

        def _parse_actor_str(data: object) -> Union[EventActor, None]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                actor_str_type_0 = EventActor(data)

                return actor_str_type_0
            except:  # noqa: E722
                pass
            return cast(Union[EventActor, None], data)

        actor_str = _parse_actor_str(d.pop("actorStr"))

        main_entity_name = EntityName(d.pop("mainEntityName"))

        def _parse_comment_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        comment_duid = _parse_comment_duid(d.pop("commentDuid"))

        def _parse_task_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        task_duid = _parse_task_duid(d.pop("taskDuid"))

        def _parse_dartboard_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        dartboard_duid = _parse_dartboard_duid(d.pop("dartboardDuid"))

        def _parse_dashboard_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        dashboard_duid = _parse_dashboard_duid(d.pop("dashboardDuid"))

        def _parse_view_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        view_duid = _parse_view_duid(d.pop("viewDuid"))

        def _parse_space_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        space_duid = _parse_space_duid(d.pop("spaceDuid"))

        def _parse_doc_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        doc_duid = _parse_doc_duid(d.pop("docDuid"))

        def _parse_folder_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        folder_duid = _parse_folder_duid(d.pop("folderDuid"))

        def _parse_form_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        form_duid = _parse_form_duid(d.pop("formDuid"))

        def _parse_brainstorm_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        brainstorm_duid = _parse_brainstorm_duid(d.pop("brainstormDuid"))

        def _parse_property_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        property_duid = _parse_property_duid(d.pop("propertyDuid"))

        def _parse_status_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        status_duid = _parse_status_duid(d.pop("statusDuid"))

        def _parse_user_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        user_duid = _parse_user_duid(d.pop("userDuid"))

        adtl = d.pop("adtl")

        event = cls(
            message_frags=message_frags,
            kind=kind,
            actor_duid=actor_duid,
            actor_str=actor_str,
            main_entity_name=main_entity_name,
            comment_duid=comment_duid,
            task_duid=task_duid,
            dartboard_duid=dartboard_duid,
            dashboard_duid=dashboard_duid,
            view_duid=view_duid,
            space_duid=space_duid,
            doc_duid=doc_duid,
            folder_duid=folder_duid,
            form_duid=form_duid,
            brainstorm_duid=brainstorm_duid,
            property_duid=property_duid,
            status_duid=status_duid,
            user_duid=user_duid,
            adtl=adtl,
        )

        event.additional_properties = d
        return event

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
