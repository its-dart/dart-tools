from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OptionUpdate")


@_attrs_define
class OptionUpdate:
    """
    Attributes:
        duid (str):
        property_duid (Union[Unset, str]):
        parent_duid (Union[None, Unset, str]):
        title (Union[Unset, str]):
        color_hex (Union[Unset, str]):
    """

    duid: str
    property_duid: Union[Unset, str] = UNSET
    parent_duid: Union[None, Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    color_hex: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        property_duid = self.property_duid

        parent_duid: Union[None, Unset, str]
        if isinstance(self.parent_duid, Unset):
            parent_duid = UNSET
        else:
            parent_duid = self.parent_duid

        title = self.title

        color_hex = self.color_hex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if property_duid is not UNSET:
            field_dict["propertyDuid"] = property_duid
        if parent_duid is not UNSET:
            field_dict["parentDuid"] = parent_duid
        if title is not UNSET:
            field_dict["title"] = title
        if color_hex is not UNSET:
            field_dict["colorHex"] = color_hex

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        property_duid = d.pop("propertyDuid", UNSET)

        def _parse_parent_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_duid = _parse_parent_duid(d.pop("parentDuid", UNSET))

        title = d.pop("title", UNSET)

        color_hex = d.pop("colorHex", UNSET)

        option_update = cls(
            duid=duid,
            property_duid=property_duid,
            parent_duid=parent_duid,
            title=title,
            color_hex=color_hex,
        )

        option_update.additional_properties = d
        return option_update

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
