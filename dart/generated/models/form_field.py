from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_field_default import FormFieldDefault


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
        hidden (bool):
        label (str):
        default (FormFieldDefault):
        updated_by_client_duid (Union[Unset, None, str]):
    """

    duid: str
    form_duid: str
    property_duid: str
    locked: bool
    order: str
    hidden: bool
    label: str
    default: "FormFieldDefault"
    updated_by_client_duid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        form_duid = self.form_duid
        property_duid = self.property_duid
        locked = self.locked
        order = self.order
        hidden = self.hidden
        label = self.label
        default = self.default.to_dict()

        updated_by_client_duid = self.updated_by_client_duid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "formDuid": form_duid,
                "propertyDuid": property_duid,
                "locked": locked,
                "order": order,
                "hidden": hidden,
                "label": label,
                "default": default,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.form_field_default import FormFieldDefault

        d = src_dict.copy()
        duid = d.pop("duid")

        form_duid = d.pop("formDuid")

        property_duid = d.pop("propertyDuid")

        locked = d.pop("locked")

        order = d.pop("order")

        hidden = d.pop("hidden")

        label = d.pop("label")

        default = FormFieldDefault.from_dict(d.pop("default"))

        updated_by_client_duid = d.pop("updatedByClientDuid", UNSET)

        form_field = cls(
            duid=duid,
            form_duid=form_duid,
            property_duid=property_duid,
            locked=locked,
            order=order,
            hidden=hidden,
            label=label,
            default=default,
            updated_by_client_duid=updated_by_client_duid,
        )

        form_field.additional_properties = d
        return form_field

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
