from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_kind import StatusKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusCreate")


@_attrs_define
class StatusCreate:
    """
    Attributes:
        duid (str):
        property_duid (str):
        kind (StatusKind): * `Unstarted` - UNSTARTED
            * `Started` - STARTED
            * `Blocked` - BLOCKED
            * `Finished` - FINISHED
            * `Canceled` - CANCELED
        order (str):
        locked (Union[Unset, bool]):
        title (Union[Unset, str]):
        color_hex (Union[Unset, str]):
        description (Union[Unset, str]):
    """

    duid: str
    property_duid: str
    kind: StatusKind
    order: str
    locked: Union[Unset, bool] = UNSET
    title: Union[Unset, str] = UNSET
    color_hex: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        property_duid = self.property_duid

        kind = self.kind.value

        order = self.order

        locked = self.locked

        title = self.title

        color_hex = self.color_hex

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "propertyDuid": property_duid,
                "kind": kind,
                "order": order,
            }
        )
        if locked is not UNSET:
            field_dict["locked"] = locked
        if title is not UNSET:
            field_dict["title"] = title
        if color_hex is not UNSET:
            field_dict["colorHex"] = color_hex
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        property_duid = d.pop("propertyDuid")

        kind = StatusKind(d.pop("kind"))

        order = d.pop("order")

        locked = d.pop("locked", UNSET)

        title = d.pop("title", UNSET)

        color_hex = d.pop("colorHex", UNSET)

        description = d.pop("description", UNSET)

        status_create = cls(
            duid=duid,
            property_duid=property_duid,
            kind=kind,
            order=order,
            locked=locked,
            title=title,
            color_hex=color_hex,
            description=description,
        )

        status_create.additional_properties = d
        return status_create

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
