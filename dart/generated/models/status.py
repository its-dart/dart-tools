from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.color_name import ColorName
from ..models.status_kind import StatusKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="Status")


@_attrs_define
class Status:
    """
    Attributes:
        duid (str):
        kind (StatusKind): * `Unstarted` - UNSTARTED
            * `Started` - STARTED
            * `Blocked` - BLOCKED
            * `Finished` - FINISHED
            * `Canceled` - CANCELED
        locked (bool):
        order (str):
        title (str):
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
        description (str):
        updated_by_client_duid (Union[Unset, None, str]):
    """

    duid: str
    kind: StatusKind
    locked: bool
    order: str
    title: str
    color_name: ColorName
    description: str
    updated_by_client_duid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        kind = self.kind.value

        locked = self.locked
        order = self.order
        title = self.title
        color_name = self.color_name.value

        description = self.description
        updated_by_client_duid = self.updated_by_client_duid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "kind": kind,
                "locked": locked,
                "order": order,
                "title": title,
                "colorName": color_name,
                "description": description,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        kind = StatusKind(d.pop("kind"))

        locked = d.pop("locked")

        order = d.pop("order")

        title = d.pop("title")

        color_name = ColorName(d.pop("colorName"))

        description = d.pop("description")

        updated_by_client_duid = d.pop("updatedByClientDuid", UNSET)

        status = cls(
            duid=duid,
            kind=kind,
            locked=locked,
            order=order,
            title=title,
            color_name=color_name,
            description=description,
            updated_by_client_duid=updated_by_client_duid,
        )

        status.additional_properties = d
        return status

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
