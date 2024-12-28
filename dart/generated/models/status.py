from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_kind import StatusKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="Status")


@_attrs_define
class Status:
    """
    Attributes:
        duid (str):
        property_duid (str):
        kind (StatusKind): * `Unstarted` - UNSTARTED
            * `Started` - STARTED
            * `Blocked` - BLOCKED
            * `Finished` - FINISHED
            * `Canceled` - CANCELED
        locked (bool):
        order (str):
        title (str):
        color_hex (str):
        description (str):
        updated_by_client_duid (Union[None, Unset, str]):
    """

    duid: str
    property_duid: str
    kind: StatusKind
    locked: bool
    order: str
    title: str
    color_hex: str
    description: str
    updated_by_client_duid: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        property_duid = self.property_duid

        kind = self.kind.value

        locked = self.locked

        order = self.order

        title = self.title

        color_hex = self.color_hex

        description = self.description

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
                "kind": kind,
                "locked": locked,
                "order": order,
                "title": title,
                "colorHex": color_hex,
                "description": description,
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

        kind = StatusKind(d.pop("kind"))

        locked = d.pop("locked")

        order = d.pop("order")

        title = d.pop("title")

        color_hex = d.pop("colorHex")

        description = d.pop("description")

        def _parse_updated_by_client_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_client_duid = _parse_updated_by_client_duid(d.pop("updatedByClientDuid", UNSET))

        status = cls(
            duid=duid,
            property_duid=property_duid,
            kind=kind,
            locked=locked,
            order=order,
            title=title,
            color_hex=color_hex,
            description=description,
            updated_by_client_duid=updated_by_client_duid,
        )

        status.additional_properties = d
        return status

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
