from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_field_create_default import FormFieldCreateDefault


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
        hidden (Union[Unset, bool]):
        label (Union[Unset, str]):
        default (Union[Unset, FormFieldCreateDefault]):
    """

    duid: str
    form_duid: str
    property_duid: str
    order: str
    locked: Union[Unset, bool] = UNSET
    hidden: Union[Unset, bool] = UNSET
    label: Union[Unset, str] = UNSET
    default: Union[Unset, "FormFieldCreateDefault"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        form_duid = self.form_duid
        property_duid = self.property_duid
        order = self.order
        locked = self.locked
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
                "formDuid": form_duid,
                "propertyDuid": property_duid,
                "order": order,
            }
        )
        if locked is not UNSET:
            field_dict["locked"] = locked
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if label is not UNSET:
            field_dict["label"] = label
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.form_field_create_default import FormFieldCreateDefault

        d = src_dict.copy()
        duid = d.pop("duid")

        form_duid = d.pop("formDuid")

        property_duid = d.pop("propertyDuid")

        order = d.pop("order")

        locked = d.pop("locked", UNSET)

        hidden = d.pop("hidden", UNSET)

        label = d.pop("label", UNSET)

        _default = d.pop("default", UNSET)
        default: Union[Unset, FormFieldCreateDefault]
        if isinstance(_default, Unset):
            default = UNSET
        else:
            default = FormFieldCreateDefault.from_dict(_default)

        form_field_create = cls(
            duid=duid,
            form_duid=form_duid,
            property_duid=property_duid,
            order=order,
            locked=locked,
            hidden=hidden,
            label=label,
            default=default,
        )

        form_field_create.additional_properties = d
        return form_field_create

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
