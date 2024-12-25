from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ZapierIntegration")


@_attrs_define
class ZapierIntegration:
    """
    Attributes:
        enabled (bool):
        linked_user_duids (list[str]):
    """

    enabled: bool
    linked_user_duids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        linked_user_duids = self.linked_user_duids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "linkedUserDuids": linked_user_duids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled")

        linked_user_duids = cast(list[str], d.pop("linkedUserDuids"))

        zapier_integration = cls(
            enabled=enabled,
            linked_user_duids=linked_user_duids,
        )

        zapier_integration.additional_properties = d
        return zapier_integration

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
