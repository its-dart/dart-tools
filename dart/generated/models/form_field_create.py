from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FormFieldCreate")


@_attrs_define
class FormFieldCreate:
    """
    Attributes:
        duid (str):
        form_duid (str):
        property_duid (str):
        order (str):
        locked (Union[Unset, bool]):
        required (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
        label (Union[Unset, str]):
        default (Union[Unset, Any]):
    """

    duid: str
    form_duid: str
    property_duid: str
    order: str
    locked: Union[Unset, bool] = UNSET
    required: Union[Unset, bool] = UNSET
    hidden: Union[Unset, bool] = UNSET
    label: Union[Unset, str] = UNSET
    default: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        form_duid = self.form_duid

        property_duid = self.property_duid

        order = self.order

        locked = self.locked

        required = self.required

        hidden = self.hidden

        label = self.label

        default = self.default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "formDuid": form_duid,
                "propertyDuid": property_duid,
                "order": order,
            }
        )
        if locked is not UNSET:
            field_dict["locked"] = locked
        if required is not UNSET:
            field_dict["required"] = required
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if label is not UNSET:
            field_dict["label"] = label
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        form_duid = d.pop("formDuid")

        property_duid = d.pop("propertyDuid")

        order = d.pop("order")

        locked = d.pop("locked", UNSET)

        required = d.pop("required", UNSET)

        hidden = d.pop("hidden", UNSET)

        label = d.pop("label", UNSET)

        default = d.pop("default", UNSET)

        form_field_create = cls(
            duid=duid,
            form_duid=form_duid,
            property_duid=property_duid,
            order=order,
            locked=locked,
            required=required,
            hidden=hidden,
            label=label,
            default=default,
        )

        form_field_create.additional_properties = d
        return form_field_create

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
