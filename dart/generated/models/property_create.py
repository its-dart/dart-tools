from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.property_kind import PropertyKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.property_create_adtl import PropertyCreateAdtl


T = TypeVar("T", bound="PropertyCreate")


@_attrs_define
class PropertyCreate:
    """
    Attributes:
        duid (str):
        kind (PropertyKind): * `Default: Status` - DEFAULT_STATUS
            * `Default: Assignee` - DEFAULT_ASSIGNEE
            * `Default: Dates` - DEFAULT_DATES
            * `Default: Priority` - DEFAULT_PRIORITY
            * `Default: Tags` - DEFAULT_TAGS
            * `Default: Size` - DEFAULT_SIZE
            * `Default: Created` - DEFAULT_CREATED_AT
            * `Default: Created by` - DEFAULT_CREATED_BY
            * `Default: Last updated` - DEFAULT_UPDATED_AT
            * `Default: Last updated by` - DEFAULT_UPDATED_BY
            * `Text` - TEXT
            * `Number` - NUMBER
            * `Checkbox` - CHECKBOX
            * `Select` - SELECT
            * `Multiselect` - MULTISELECT
            * `Status` - STATUS
            * `User` - USER
            * `Dates` - DATES
        order (str):
        hidden (Union[Unset, bool]):
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        adtl (Union[Unset, PropertyCreateAdtl]):
    """

    duid: str
    kind: PropertyKind
    order: str
    hidden: Union[Unset, bool] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    adtl: Union[Unset, "PropertyCreateAdtl"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        kind = self.kind.value

        order = self.order
        hidden = self.hidden
        title = self.title
        description = self.description
        adtl: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.adtl, Unset):
            adtl = self.adtl.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "kind": kind,
                "order": order,
            }
        )
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if adtl is not UNSET:
            field_dict["adtl"] = adtl

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.property_create_adtl import PropertyCreateAdtl

        d = src_dict.copy()
        duid = d.pop("duid")

        kind = PropertyKind(d.pop("kind"))

        order = d.pop("order")

        hidden = d.pop("hidden", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _adtl = d.pop("adtl", UNSET)
        adtl: Union[Unset, PropertyCreateAdtl]
        if isinstance(_adtl, Unset):
            adtl = UNSET
        else:
            adtl = PropertyCreateAdtl.from_dict(_adtl)

        property_create = cls(
            duid=duid,
            kind=kind,
            order=order,
            hidden=hidden,
            title=title,
            description=description,
            adtl=adtl,
        )

        property_create.additional_properties = d
        return property_create

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
