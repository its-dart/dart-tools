from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Option")


@_attrs_define
class Option:
    """
    Attributes:
        duid (str):
        property_duid (str):
        parent_duid (Union[None, str]):
        title (str):
        color_hex (str):
        updated_by_client_duid (Union[None, Unset, str]):
    """

    duid: str
    property_duid: str
    parent_duid: Union[None, str]
    title: str
    color_hex: str
    updated_by_client_duid: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        property_duid = self.property_duid

        parent_duid: Union[None, str]
        parent_duid = self.parent_duid

        title = self.title

        color_hex = self.color_hex

        updated_by_client_duid: Union[None, Unset, str]
        if isinstance(self.updated_by_client_duid, Unset):
            updated_by_client_duid = UNSET
        else:
            updated_by_client_duid = self.updated_by_client_duid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "propertyDuid": property_duid,
                "parentDuid": parent_duid,
                "title": title,
                "colorHex": color_hex,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        property_duid = d.pop("propertyDuid")

        def _parse_parent_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        parent_duid = _parse_parent_duid(d.pop("parentDuid"))

        title = d.pop("title")

        color_hex = d.pop("colorHex")

        def _parse_updated_by_client_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_client_duid = _parse_updated_by_client_duid(d.pop("updatedByClientDuid", UNSET))

        option = cls(
            duid=duid,
            property_duid=property_duid,
            parent_duid=parent_duid,
            title=title,
            color_hex=color_hex,
            updated_by_client_duid=updated_by_client_duid,
        )

        option.additional_properties = d
        return option

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
