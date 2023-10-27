from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_kind import EventKind

T = TypeVar("T", bound="EventSubscriptionCreate")


@_attrs_define
class EventSubscriptionCreate:
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
        email (bool):
        slack (bool):
    """

    kind: EventKind
    email: bool
    slack: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind = self.kind.value

        email = self.email
        slack = self.slack

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "email": email,
                "slack": slack,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        kind = EventKind(d.pop("kind"))

        email = d.pop("email")

        slack = d.pop("slack")

        event_subscription_create = cls(
            kind=kind,
            email=email,
            slack=slack,
        )

        event_subscription_create.additional_properties = d
        return event_subscription_create

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
