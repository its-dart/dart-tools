from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Attachment")


@_attrs_define
class Attachment:
    """
    Attributes:
        duid (str):
        order (str):
        name (str):
        kind (str):
        file_url (str):
        color_hex (str):
        recommendation_duid (Union[None, str]):
    """

    duid: str
    order: str
    name: str
    kind: str
    file_url: str
    color_hex: str
    recommendation_duid: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        order = self.order

        name = self.name

        kind = self.kind

        file_url = self.file_url

        color_hex = self.color_hex

        recommendation_duid: Union[None, str]
        recommendation_duid = self.recommendation_duid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "order": order,
                "name": name,
                "kind": kind,
                "fileUrl": file_url,
                "colorHex": color_hex,
                "recommendationDuid": recommendation_duid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        order = d.pop("order")

        name = d.pop("name")

        kind = d.pop("kind")

        file_url = d.pop("fileUrl")

        color_hex = d.pop("colorHex")

        def _parse_recommendation_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        recommendation_duid = _parse_recommendation_duid(d.pop("recommendationDuid"))

        attachment = cls(
            duid=duid,
            order=order,
            name=name,
            kind=kind,
            file_url=file_url,
            color_hex=color_hex,
            recommendation_duid=recommendation_duid,
        )

        attachment.additional_properties = d
        return attachment

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
