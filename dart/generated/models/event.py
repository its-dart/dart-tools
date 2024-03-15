from typing import Any, Dict, List, Optional, Type, TypeVar

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
            * `onboarding/finish_step` - ONBOARDING_FINISH_STEP
            * `profile/update` - PROFILE_UPDATE
            * `profile/delete` - PROFILE_DELETE
            * `profile/become_active` - PROFILE_BECOME_ACTIVE
            * `profile/become_inactive` - PROFILE_BECOME_INACTIVE
            * `ai/props` - AI_PROPS
            * `ai/subtasks` - AI_SUBTASKS
            * `ai/content` - AI_CONTENT
            * `ai/translate` - AI_TRANSLATE
            * `ai/emoji` - AI_EMOJI
            * `ai/feedback` - AI_FEEDBACK
            * `ai/icon` - AI_ICON
            * `ai/report` - AI_REPORT
            * `ai/plan` - AI_PLAN
            * `load/signup` - LOAD_SIGNUP
            * `help/resource_click` - HELP_RESOURCE_CLICK
            * `usage/submit_feedback` - USAGE_SUBMIT_FEEDBACK
            * `usage/undo` - USAGE_UNDO
            * `usage/redo` - USAGE_REDO
            * `usage/open_command_center` - USAGE_OPEN_COMMAND_CENTER
            * `usage/open_rightbar` - USAGE_OPEN_RIGHTBAR
            * `usage/open_fullscreen` - USAGE_OPEN_FULLSCREEN
            * `usage/copy_task_link` - USAGE_COPY_TASK_LINK
            * `usage/copy_branch` - USAGE_COPY_BRANCH
            * `usage/open_search` - USAGE_OPEN_SEARCH
            * `usage/nlp_raw_create` - USAGE_NLP_RAW_CREATE
            * `usage/nlp_raw_delete` - USAGE_NLP_RAW_DELETE
            * `usage/nlp_typeahead_open` - USAGE_NLP_TYPEAHEAD_OPEN
            * `usage/nlp_typeahead_accept` - USAGE_NLP_TYPEAHEAD_ACCEPT
            * `brainstorm/start` - BRAINSTORM_START
            * `brainstorm/stop` - BRAINSTORM_STOP
        main_entity_name (EntityName): * `comment` - COMMENT
            * `task` - TASK
            * `dartboard` - DARTBOARD
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
        adtl (Any):
        message (Optional[str]):
        actor_duid (Optional[str]):
        actor_str (Optional[EventActor]): * `Dart AI` - DART_AI
            * `Dart Due Date Bot` - DART_DUE_DATE_BOT
            * `Dart GitHub Bot` - DART_GITHUB_BOT
            * `Dart Metrics Bot` - DART_METRICS_BOT
            * `Dart Recurring Task Bot` - DART_RECURRING_TASK_BOT
            * `Dart Reminder Bot` - DART_REMINDER_BOT
            * `Dart Report Bot` - DART_REPORT_BOT
            * `Dart Slack Bot` - DART_SLACK_BOT
            * `A form user` - FORM_USER
            * `An email user` - EMAIL_USER
            * `Stripe webhook` - STRIPE_WEBHOOK
        comment_duid (Optional[str]):
        task_duid (Optional[str]):
        dartboard_duid (Optional[str]):
        view_duid (Optional[str]):
        space_duid (Optional[str]):
        doc_duid (Optional[str]):
        folder_duid (Optional[str]):
        form_duid (Optional[str]):
        brainstorm_duid (Optional[str]):
        property_duid (Optional[str]):
        status_duid (Optional[str]):
        user_duid (Optional[str]):
    """

    kind: EventKind
    main_entity_name: EntityName
    adtl: Any
    message: Optional[str]
    actor_duid: Optional[str]
    actor_str: Optional[EventActor]
    comment_duid: Optional[str]
    task_duid: Optional[str]
    dartboard_duid: Optional[str]
    view_duid: Optional[str]
    space_duid: Optional[str]
    doc_duid: Optional[str]
    folder_duid: Optional[str]
    form_duid: Optional[str]
    brainstorm_duid: Optional[str]
    property_duid: Optional[str]
    status_duid: Optional[str]
    user_duid: Optional[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind = self.kind.value

        main_entity_name = self.main_entity_name.value

        adtl = self.adtl
        message = self.message
        actor_duid = self.actor_duid
        actor_str = self.actor_str.value if self.actor_str else None

        comment_duid = self.comment_duid
        task_duid = self.task_duid
        dartboard_duid = self.dartboard_duid
        view_duid = self.view_duid
        space_duid = self.space_duid
        doc_duid = self.doc_duid
        folder_duid = self.folder_duid
        form_duid = self.form_duid
        brainstorm_duid = self.brainstorm_duid
        property_duid = self.property_duid
        status_duid = self.status_duid
        user_duid = self.user_duid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "mainEntityName": main_entity_name,
                "adtl": adtl,
                "message": message,
                "actorDuid": actor_duid,
                "actorStr": actor_str,
                "commentDuid": comment_duid,
                "taskDuid": task_duid,
                "dartboardDuid": dartboard_duid,
                "viewDuid": view_duid,
                "spaceDuid": space_duid,
                "docDuid": doc_duid,
                "folderDuid": folder_duid,
                "formDuid": form_duid,
                "brainstormDuid": brainstorm_duid,
                "propertyDuid": property_duid,
                "statusDuid": status_duid,
                "userDuid": user_duid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        kind = EventKind(d.pop("kind"))

        main_entity_name = EntityName(d.pop("mainEntityName"))

        adtl = d.pop("adtl")

        message = d.pop("message")

        actor_duid = d.pop("actorDuid")

        _actor_str = d.pop("actorStr")
        actor_str: Optional[EventActor]
        if _actor_str is None:
            actor_str = None
        else:
            actor_str = EventActor(_actor_str)

        comment_duid = d.pop("commentDuid")

        task_duid = d.pop("taskDuid")

        dartboard_duid = d.pop("dartboardDuid")

        view_duid = d.pop("viewDuid")

        space_duid = d.pop("spaceDuid")

        doc_duid = d.pop("docDuid")

        folder_duid = d.pop("folderDuid")

        form_duid = d.pop("formDuid")

        brainstorm_duid = d.pop("brainstormDuid")

        property_duid = d.pop("propertyDuid")

        status_duid = d.pop("statusDuid")

        user_duid = d.pop("userDuid")

        event = cls(
            kind=kind,
            main_entity_name=main_entity_name,
            adtl=adtl,
            message=message,
            actor_duid=actor_duid,
            actor_str=actor_str,
            comment_duid=comment_duid,
            task_duid=task_duid,
            dartboard_duid=dartboard_duid,
            view_duid=view_duid,
            space_duid=space_duid,
            doc_duid=doc_duid,
            folder_duid=folder_duid,
            form_duid=form_duid,
            brainstorm_duid=brainstorm_duid,
            property_duid=property_duid,
            status_duid=status_duid,
            user_duid=user_duid,
        )

        event.additional_properties = d
        return event

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
