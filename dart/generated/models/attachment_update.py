from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachmentUpdate")


@_attrs_define
class AttachmentUpdate:
    """
    Attributes:
        duid (str):
        order (Union[Unset, str]):
        name (Union[Unset, str]):
        kind (Union[Unset, str]):
        file_path (Union[Unset, str]):
        color_hex (Union[Unset, str]):
        recommendation_duid (Union[None, Unset, str]):
    """

    duid: str
    order: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    file_path: Union[Unset, str] = UNSET
    color_hex: Union[Unset, str] = UNSET
    recommendation_duid: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        order = self.order

        name = self.name

        kind = self.kind

        file_path = self.file_path

        color_hex = self.color_hex

        recommendation_duid: Union[None, Unset, str]
        if isinstance(self.recommendation_duid, Unset):
            recommendation_duid = UNSET
        else:
            recommendation_duid = self.recommendation_duid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if order is not UNSET:
            field_dict["order"] = order
        if name is not UNSET:
            field_dict["name"] = name
        if kind is not UNSET:
            field_dict["kind"] = kind
        if file_path is not UNSET:
            field_dict["filePath"] = file_path
        if color_hex is not UNSET:
            field_dict["colorHex"] = color_hex
        if recommendation_duid is not UNSET:
            field_dict["recommendationDuid"] = recommendation_duid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        order = d.pop("order", UNSET)

        name = d.pop("name", UNSET)

        kind = d.pop("kind", UNSET)

        file_path = d.pop("filePath", UNSET)

        color_hex = d.pop("colorHex", UNSET)

        def _parse_recommendation_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        recommendation_duid = _parse_recommendation_duid(d.pop("recommendationDuid", UNSET))

        attachment_update = cls(
            duid=duid,
            order=order,
            name=name,
            kind=kind,
            file_path=file_path,
            color_hex=color_hex,
            recommendation_duid=recommendation_duid,
        )

        attachment_update.additional_properties = d
        return attachment_update

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
