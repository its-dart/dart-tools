from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TenantUpdate")


@_attrs_define
class TenantUpdate:
    """
    Attributes:
        name (Union[Unset, str]):
        timezone (Union[Unset, str]):
        backlog_enabled (Union[Unset, bool]):
        ai_assignment_enabled (Union[Unset, bool]):
        email_integration_enabled (Union[Unset, bool]):
        close_parent_on_close_all_subtasks (Union[Unset, bool]):
        move_subtasks_on_move_parent (Union[Unset, bool]):
        update_subtasks_status_on_update_parent_status (Union[Unset, bool]):
        copy_parent_fields_on_create (Union[Unset, bool]):
        update_blockee_dates_on_update_blocker_due_date (Union[Unset, bool]):
        webhook_enabled (Union[Unset, bool]):
        webhook_secret (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    timezone: Union[Unset, str] = UNSET
    backlog_enabled: Union[Unset, bool] = UNSET
    ai_assignment_enabled: Union[Unset, bool] = UNSET
    email_integration_enabled: Union[Unset, bool] = UNSET
    close_parent_on_close_all_subtasks: Union[Unset, bool] = UNSET
    move_subtasks_on_move_parent: Union[Unset, bool] = UNSET
    update_subtasks_status_on_update_parent_status: Union[Unset, bool] = UNSET
    copy_parent_fields_on_create: Union[Unset, bool] = UNSET
    update_blockee_dates_on_update_blocker_due_date: Union[Unset, bool] = UNSET
    webhook_enabled: Union[Unset, bool] = UNSET
    webhook_secret: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        timezone = self.timezone

        backlog_enabled = self.backlog_enabled

        ai_assignment_enabled = self.ai_assignment_enabled

        email_integration_enabled = self.email_integration_enabled

        close_parent_on_close_all_subtasks = self.close_parent_on_close_all_subtasks

        move_subtasks_on_move_parent = self.move_subtasks_on_move_parent

        update_subtasks_status_on_update_parent_status = self.update_subtasks_status_on_update_parent_status

        copy_parent_fields_on_create = self.copy_parent_fields_on_create

        update_blockee_dates_on_update_blocker_due_date = self.update_blockee_dates_on_update_blocker_due_date

        webhook_enabled = self.webhook_enabled

        webhook_secret = self.webhook_secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if backlog_enabled is not UNSET:
            field_dict["backlogEnabled"] = backlog_enabled
        if ai_assignment_enabled is not UNSET:
            field_dict["aiAssignmentEnabled"] = ai_assignment_enabled
        if email_integration_enabled is not UNSET:
            field_dict["emailIntegrationEnabled"] = email_integration_enabled
        if close_parent_on_close_all_subtasks is not UNSET:
            field_dict["closeParentOnCloseAllSubtasks"] = close_parent_on_close_all_subtasks
        if move_subtasks_on_move_parent is not UNSET:
            field_dict["moveSubtasksOnMoveParent"] = move_subtasks_on_move_parent
        if update_subtasks_status_on_update_parent_status is not UNSET:
            field_dict["updateSubtasksStatusOnUpdateParentStatus"] = update_subtasks_status_on_update_parent_status
        if copy_parent_fields_on_create is not UNSET:
            field_dict["copyParentFieldsOnCreate"] = copy_parent_fields_on_create
        if update_blockee_dates_on_update_blocker_due_date is not UNSET:
            field_dict["updateBlockeeDatesOnUpdateBlockerDueDate"] = update_blockee_dates_on_update_blocker_due_date
        if webhook_enabled is not UNSET:
            field_dict["webhookEnabled"] = webhook_enabled
        if webhook_secret is not UNSET:
            field_dict["webhookSecret"] = webhook_secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        timezone = d.pop("timezone", UNSET)

        backlog_enabled = d.pop("backlogEnabled", UNSET)

        ai_assignment_enabled = d.pop("aiAssignmentEnabled", UNSET)

        email_integration_enabled = d.pop("emailIntegrationEnabled", UNSET)

        close_parent_on_close_all_subtasks = d.pop("closeParentOnCloseAllSubtasks", UNSET)

        move_subtasks_on_move_parent = d.pop("moveSubtasksOnMoveParent", UNSET)

        update_subtasks_status_on_update_parent_status = d.pop("updateSubtasksStatusOnUpdateParentStatus", UNSET)

        copy_parent_fields_on_create = d.pop("copyParentFieldsOnCreate", UNSET)

        update_blockee_dates_on_update_blocker_due_date = d.pop("updateBlockeeDatesOnUpdateBlockerDueDate", UNSET)

        webhook_enabled = d.pop("webhookEnabled", UNSET)

        webhook_secret = d.pop("webhookSecret", UNSET)

        tenant_update = cls(
            name=name,
            timezone=timezone,
            backlog_enabled=backlog_enabled,
            ai_assignment_enabled=ai_assignment_enabled,
            email_integration_enabled=email_integration_enabled,
            close_parent_on_close_all_subtasks=close_parent_on_close_all_subtasks,
            move_subtasks_on_move_parent=move_subtasks_on_move_parent,
            update_subtasks_status_on_update_parent_status=update_subtasks_status_on_update_parent_status,
            copy_parent_fields_on_create=copy_parent_fields_on_create,
            update_blockee_dates_on_update_blocker_due_date=update_blockee_dates_on_update_blocker_due_date,
            webhook_enabled=webhook_enabled,
            webhook_secret=webhook_secret,
        )

        tenant_update.additional_properties = d
        return tenant_update

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
