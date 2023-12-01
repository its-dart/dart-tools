from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_field_update_default import FormFieldUpdateDefault


T = TypeVar("T", bound="FormFieldUpdate")


@_attrs_define
class FormFieldUpdate:
    """
    Attributes:
        duid (str):
        form_duid (Union[Unset, str]):
        property_duid (Union[Unset, str]):
        locked (Union[Unset, bool]):
        order (Union[Unset, str]):
        hidden (Union[Unset, bool]):
        label (Union[Unset, str]):
        default (Union[Unset, FormFieldUpdateDefault]):
    """

    duid: str
    form_duid: Union[Unset, str] = UNSET
    property_duid: Union[Unset, str] = UNSET
    locked: Union[Unset, bool] = UNSET
    order: Union[Unset, str] = UNSET
    hidden: Union[Unset, bool] = UNSET
    label: Union[Unset, str] = UNSET
    default: Union[Unset, "FormFieldUpdateDefault"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        form_duid = self.form_duid
        property_duid = self.property_duid
        locked = self.locked
        order = self.order
        hidden = self.hidden
        label = self.label
        default: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default, Unset):
            default = self.default.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if form_duid is not UNSET:
            field_dict["formDuid"] = form_duid
        if property_duid is not UNSET:
            field_dict["propertyDuid"] = property_duid
        if locked is not UNSET:
            field_dict["locked"] = locked
        if order is not UNSET:
            field_dict["order"] = order
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if label is not UNSET:
            field_dict["label"] = label
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.form_field_update_default import FormFieldUpdateDefault

        d = src_dict.copy()
        duid = d.pop("duid")

        form_duid = d.pop("formDuid", UNSET)

        property_duid = d.pop("propertyDuid", UNSET)

        locked = d.pop("locked", UNSET)

        order = d.pop("order", UNSET)

        hidden = d.pop("hidden", UNSET)

        label = d.pop("label", UNSET)

        _default = d.pop("default", UNSET)
        default: Union[Unset, FormFieldUpdateDefault]
        if isinstance(_default, Unset):
            default = UNSET
        else:
            default = FormFieldUpdateDefault.from_dict(_default)

        form_field_update = cls(
            duid=duid,
            form_duid=form_duid,
            property_duid=property_duid,
            locked=locked,
            order=order,
            hidden=hidden,
            label=label,
            default=default,
        )

        form_field_update.additional_properties = d
        return form_field_update

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
