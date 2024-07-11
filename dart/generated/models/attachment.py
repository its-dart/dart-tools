from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.color_name import ColorName

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
        color_name (ColorName): * `Red` - RED
            * `Dark Blue` - DARK_BLUE
            * `Dark Orange` - DARK_ORANGE
            * `Dark Green` - DARK_GREEN
            * `Purple` - PURPLE
            * `Dark Teal` - DARK_TEAL
            * `Pink` - PINK
            * `Orange` - ORANGE
            * `Green` - GREEN
            * `Yellow` - YELLOW
            * `Brown` - BROWN
            * `Dark Red` - DARK_RED
            * `Flat Green` - FLAT_GREEN
            * `Red Orange` - RED_ORANGE
            * `Teal` - TEAL
            * `Light Green` - LIGHT_GREEN
            * `Light Blue` - LIGHT_BLUE
            * `Light Purple` - LIGHT_PURPLE
            * `Light Orange` - LIGHT_ORANGE
            * `Light Pink` - LIGHT_PINK
            * `Tan` - TAN
            * `Dark Gray` - DARK_GRAY
            * `Light Brown` - LIGHT_BROWN
            * `Light Gray` - LIGHT_GRAY
        recommendation_duid (Union[None, str]):
    """

    duid: str
    order: str
    name: str
    kind: str
    file_url: str
    color_hex: str
    color_name: ColorName
    recommendation_duid: Union[None, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid

        order = self.order

        name = self.name

        kind = self.kind

        file_url = self.file_url

        color_hex = self.color_hex

        color_name = self.color_name.value

        recommendation_duid: Union[None, str]
        recommendation_duid = self.recommendation_duid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "order": order,
                "name": name,
                "kind": kind,
                "fileUrl": file_url,
                "colorHex": color_hex,
                "colorName": color_name,
                "recommendationDuid": recommendation_duid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        order = d.pop("order")

        name = d.pop("name")

        kind = d.pop("kind")

        file_url = d.pop("fileUrl")

        color_hex = d.pop("colorHex")

        color_name = ColorName(d.pop("colorName"))

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
            color_name=color_name,
            recommendation_duid=recommendation_duid,
        )

        attachment.additional_properties = d
        return attachment

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
