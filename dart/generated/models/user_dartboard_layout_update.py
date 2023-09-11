from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserDartboardLayoutUpdate")


@_attrs_define
class UserDartboardLayoutUpdate:
    """
    Attributes:
        user_duid (Union[Unset, str]):
        dartboard_duid (Union[Unset, str]):
        layout_duid (Union[Unset, str]):
    """

    user_duid: Union[Unset, str] = UNSET
    dartboard_duid: Union[Unset, str] = UNSET
    layout_duid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_duid = self.user_duid
        dartboard_duid = self.dartboard_duid
        layout_duid = self.layout_duid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_duid is not UNSET:
            field_dict["userDuid"] = user_duid
        if dartboard_duid is not UNSET:
            field_dict["dartboardDuid"] = dartboard_duid
        if layout_duid is not UNSET:
            field_dict["layoutDuid"] = layout_duid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_duid = d.pop("userDuid", UNSET)

        dartboard_duid = d.pop("dartboardDuid", UNSET)

        layout_duid = d.pop("layoutDuid", UNSET)

        user_dartboard_layout_update = cls(
            user_duid=user_duid,
            dartboard_duid=dartboard_duid,
            layout_duid=layout_duid,
        )

        user_dartboard_layout_update.additional_properties = d
        return user_dartboard_layout_update

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
