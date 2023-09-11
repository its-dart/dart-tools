from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RelationshipUpdate")


@_attrs_define
class RelationshipUpdate:
    """
    Attributes:
        duid (str):
        source_duid (Union[Unset, str]):
        kind_duid (Union[Unset, str]):
        target_duid (Union[Unset, str]):
        is_forward (Union[Unset, bool]):
    """

    duid: str
    source_duid: Union[Unset, str] = UNSET
    kind_duid: Union[Unset, str] = UNSET
    target_duid: Union[Unset, str] = UNSET
    is_forward: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        source_duid = self.source_duid
        kind_duid = self.kind_duid
        target_duid = self.target_duid
        is_forward = self.is_forward

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if source_duid is not UNSET:
            field_dict["sourceDuid"] = source_duid
        if kind_duid is not UNSET:
            field_dict["kindDuid"] = kind_duid
        if target_duid is not UNSET:
            field_dict["targetDuid"] = target_duid
        if is_forward is not UNSET:
            field_dict["isForward"] = is_forward

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        source_duid = d.pop("sourceDuid", UNSET)

        kind_duid = d.pop("kindDuid", UNSET)

        target_duid = d.pop("targetDuid", UNSET)

        is_forward = d.pop("isForward", UNSET)

        relationship_update = cls(
            duid=duid,
            source_duid=source_duid,
            kind_duid=kind_duid,
            target_duid=target_duid,
            is_forward=is_forward,
        )

        relationship_update.additional_properties = d
        return relationship_update

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
