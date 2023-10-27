from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.color_name import ColorName
from ..models.status_kind import StatusKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusUpdate")


@_attrs_define
class StatusUpdate:
    """
    Attributes:
        duid (str):
        property_duid (Union[Unset, str]):
        kind (Union[Unset, StatusKind]): * `Unstarted` - UNSTARTED
            * `Started` - STARTED
            * `Blocked` - BLOCKED
            * `Finished` - FINISHED
            * `Canceled` - CANCELED
        order (Union[Unset, str]):
        title (Union[Unset, str]):
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
        description (Union[Unset, str]):
    """

    duid: str
    property_duid: Union[Unset, str] = UNSET
    kind: Union[Unset, StatusKind] = UNSET
    order: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    color_name: Union[Unset, ColorName] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        property_duid = self.property_duid
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        order = self.order
        title = self.title
        color_name: Union[Unset, str] = UNSET
        if not isinstance(self.color_name, Unset):
            color_name = self.color_name.value

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if property_duid is not UNSET:
            field_dict["propertyDuid"] = property_duid
        if kind is not UNSET:
            field_dict["kind"] = kind
        if order is not UNSET:
            field_dict["order"] = order
        if title is not UNSET:
            field_dict["title"] = title
        if color_name is not UNSET:
            field_dict["colorName"] = color_name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        property_duid = d.pop("propertyDuid", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, StatusKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = StatusKind(_kind)

        order = d.pop("order", UNSET)

        title = d.pop("title", UNSET)

        _color_name = d.pop("colorName", UNSET)
        color_name: Union[Unset, ColorName]
        if isinstance(_color_name, Unset):
            color_name = UNSET
        else:
            color_name = ColorName(_color_name)

        description = d.pop("description", UNSET)

        status_update = cls(
            duid=duid,
            property_duid=property_duid,
            kind=kind,
            order=order,
            title=title,
            color_name=color_name,
            description=description,
        )

        status_update.additional_properties = d
        return status_update

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
