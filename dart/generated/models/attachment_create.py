from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.color_name import ColorName
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachmentCreate")


@_attrs_define
class AttachmentCreate:
    """
    Attributes:
        duid (str):
        order (str):
        name (str):
        kind (str):
        file_path (str):
        color_hex (Union[Unset, str]):
        color_name (Union[Unset, ColorName]): * `Red` - RED
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
        recommendation_duid (Union[Unset, None, str]):
    """

    duid: str
    order: str
    name: str
    kind: str
    file_path: str
    color_hex: Union[Unset, str] = UNSET
    color_name: Union[Unset, ColorName] = UNSET
    recommendation_duid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        order = self.order
        name = self.name
        kind = self.kind
        file_path = self.file_path
        color_hex = self.color_hex
        color_name: Union[Unset, str] = UNSET
        if not isinstance(self.color_name, Unset):
            color_name = self.color_name.value

        recommendation_duid = self.recommendation_duid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "order": order,
                "name": name,
                "kind": kind,
                "filePath": file_path,
            }
        )
        if color_hex is not UNSET:
            field_dict["colorHex"] = color_hex
        if color_name is not UNSET:
            field_dict["colorName"] = color_name
        if recommendation_duid is not UNSET:
            field_dict["recommendationDuid"] = recommendation_duid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        order = d.pop("order")

        name = d.pop("name")

        kind = d.pop("kind")

        file_path = d.pop("filePath")

        color_hex = d.pop("colorHex", UNSET)

        _color_name = d.pop("colorName", UNSET)
        color_name: Union[Unset, ColorName]
        if isinstance(_color_name, Unset):
            color_name = UNSET
        else:
            color_name = ColorName(_color_name)

        recommendation_duid = d.pop("recommendationDuid", UNSET)

        attachment_create = cls(
            duid=duid,
            order=order,
            name=name,
            kind=kind,
            file_path=file_path,
            color_hex=color_hex,
            color_name=color_name,
            recommendation_duid=recommendation_duid,
        )

        attachment_create.additional_properties = d
        return attachment_create

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
