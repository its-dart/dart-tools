from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
        locked (Union[Unset, bool]):
        order (Union[Unset, str]):
        title (Union[Unset, str]):
        color_hex (Union[Unset, str]):
        description (Union[Unset, str]):
    """

    duid: str
    property_duid: Union[Unset, str] = UNSET
    kind: Union[Unset, StatusKind] = UNSET
    locked: Union[Unset, bool] = UNSET
    order: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    color_hex: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        property_duid = self.property_duid

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        locked = self.locked

        order = self.order

        title = self.title

        color_hex = self.color_hex

        description = self.description

        field_dict: dict[str, Any] = {}
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
        if locked is not UNSET:
            field_dict["locked"] = locked
        if order is not UNSET:
            field_dict["order"] = order
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

        property_duid = d.pop("propertyDuid", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, StatusKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = StatusKind(_kind)

        locked = d.pop("locked", UNSET)

        order = d.pop("order", UNSET)

        title = d.pop("title", UNSET)

        color_hex = d.pop("colorHex", UNSET)

        description = d.pop("description", UNSET)

        status_update = cls(
            duid=duid,
            property_duid=property_duid,
            kind=kind,
            locked=locked,
            order=order,
            title=title,
            color_hex=color_hex,
            description=description,
        )

        status_update.additional_properties = d
        return status_update

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
