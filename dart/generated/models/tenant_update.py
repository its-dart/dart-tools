from typing import Any, Dict, List, Type, TypeVar, Union

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
        copy_parent_fields_on_create (Union[Unset, bool]):
        webhook_enabled (Union[Unset, bool]):
        webhook_secret (Union[Unset, str]):
        webhook_url (Union[Unset, None, str]):
    """

    name: Union[Unset, str] = UNSET
    timezone: Union[Unset, str] = UNSET
    backlog_enabled: Union[Unset, bool] = UNSET
    ai_assignment_enabled: Union[Unset, bool] = UNSET
    email_integration_enabled: Union[Unset, bool] = UNSET
    copy_parent_fields_on_create: Union[Unset, bool] = UNSET
    webhook_enabled: Union[Unset, bool] = UNSET
    webhook_secret: Union[Unset, str] = UNSET
    webhook_url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        timezone = self.timezone
        backlog_enabled = self.backlog_enabled
        ai_assignment_enabled = self.ai_assignment_enabled
        email_integration_enabled = self.email_integration_enabled
        copy_parent_fields_on_create = self.copy_parent_fields_on_create
        webhook_enabled = self.webhook_enabled
        webhook_secret = self.webhook_secret
        webhook_url = self.webhook_url

        field_dict: Dict[str, Any] = {}
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
        if copy_parent_fields_on_create is not UNSET:
            field_dict["copyParentFieldsOnCreate"] = copy_parent_fields_on_create
        if webhook_enabled is not UNSET:
            field_dict["webhookEnabled"] = webhook_enabled
        if webhook_secret is not UNSET:
            field_dict["webhookSecret"] = webhook_secret
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        timezone = d.pop("timezone", UNSET)

        backlog_enabled = d.pop("backlogEnabled", UNSET)

        ai_assignment_enabled = d.pop("aiAssignmentEnabled", UNSET)

        email_integration_enabled = d.pop("emailIntegrationEnabled", UNSET)

        copy_parent_fields_on_create = d.pop("copyParentFieldsOnCreate", UNSET)

        webhook_enabled = d.pop("webhookEnabled", UNSET)

        webhook_secret = d.pop("webhookSecret", UNSET)

        webhook_url = d.pop("webhookUrl", UNSET)

        tenant_update = cls(
            name=name,
            timezone=timezone,
            backlog_enabled=backlog_enabled,
            ai_assignment_enabled=ai_assignment_enabled,
            email_integration_enabled=email_integration_enabled,
            copy_parent_fields_on_create=copy_parent_fields_on_create,
            webhook_enabled=webhook_enabled,
            webhook_secret=webhook_secret,
            webhook_url=webhook_url,
        )

        tenant_update.additional_properties = d
        return tenant_update

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
