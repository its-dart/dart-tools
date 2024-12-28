from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FormField")


@_attrs_define
class FormField:
    """
    Attributes:
        duid (str):
        form_duid (str):
        property_duid (str):
        locked (bool):
        order (str):
        required (bool):
        hidden (bool):
        label (str):
        default (Any):
        updated_by_client_duid (Union[None, Unset, str]):
    """

    duid: str
    form_duid: str
    property_duid: str
    locked: bool
    order: str
    required: bool
    hidden: bool
    label: str
    default: Any
    updated_by_client_duid: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        form_duid = self.form_duid

        property_duid = self.property_duid

        locked = self.locked

        order = self.order

        required = self.required

        hidden = self.hidden

        label = self.label

        default = self.default

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
                "formDuid": form_duid,
                "propertyDuid": property_duid,
                "locked": locked,
                "order": order,
                "required": required,
                "hidden": hidden,
                "label": label,
                "default": default,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        form_duid = d.pop("formDuid")

        property_duid = d.pop("propertyDuid")

        locked = d.pop("locked")

        order = d.pop("order")

        required = d.pop("required")

        hidden = d.pop("hidden")

        label = d.pop("label")

        default = d.pop("default")

        def _parse_updated_by_client_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_client_duid = _parse_updated_by_client_duid(d.pop("updatedByClientDuid", UNSET))

        form_field = cls(
            duid=duid,
            form_duid=form_duid,
            property_duid=property_duid,
            locked=locked,
            order=order,
            required=required,
            hidden=hidden,
            label=label,
            default=default,
            updated_by_client_duid=updated_by_client_duid,
        )

        form_field.additional_properties = d
        return form_field

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
