from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RelationshipCreate")


@_attrs_define
class RelationshipCreate:
    """
    Attributes:
        duid (str):
        source_duid (str):
        kind_duid (str):
        target_duid (str):
        is_forward (Union[Unset, bool]):
    """

    duid: str
    source_duid: str
    kind_duid: str
    target_duid: str
    is_forward: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        source_duid = self.source_duid

        kind_duid = self.kind_duid

        target_duid = self.target_duid

        is_forward = self.is_forward

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "sourceDuid": source_duid,
                "kindDuid": kind_duid,
                "targetDuid": target_duid,
            }
        )
        if is_forward is not UNSET:
            field_dict["isForward"] = is_forward

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        source_duid = d.pop("sourceDuid")

        kind_duid = d.pop("kindDuid")

        target_duid = d.pop("targetDuid")

        is_forward = d.pop("isForward", UNSET)

        relationship_create = cls(
            duid=duid,
            source_duid=source_duid,
            kind_duid=kind_duid,
            target_duid=target_duid,
            is_forward=is_forward,
        )

        relationship_create.additional_properties = d
        return relationship_create

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
