from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Relationship")


@_attrs_define
class Relationship:
    """
    Attributes:
        duid (str):
        source_duid (str):
        target_duid (str):
    """

    duid: str
    source_duid: str
    target_duid: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        source_duid = self.source_duid

        target_duid = self.target_duid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "sourceDuid": source_duid,
                "targetDuid": target_duid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        source_duid = d.pop("sourceDuid")

        target_duid = d.pop("targetDuid")

        relationship = cls(
            duid=duid,
            source_duid=source_duid,
            target_duid=target_duid,
        )

        relationship.additional_properties = d
        return relationship

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
