from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.property_kind import PropertyKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="Property")


@_attrs_define
class Property:
    """
    Attributes:
        duid (str):
        kind (PropertyKind): * `Default: Title` - DEFAULT_TITLE
            * `Default: Description` - DEFAULT_DESCRIPTION
            * `Default: Dartboard` - DEFAULT_DARTBOARD
            * `Default: Status` - DEFAULT_STATUS
            * `Default: Assignees` - DEFAULT_ASSIGNEES
            * `Default: Dates` - DEFAULT_DATES
            * `Default: Priority` - DEFAULT_PRIORITY
            * `Default: Tags` - DEFAULT_TAGS
            * `Default: Size` - DEFAULT_SIZE
            * `Default: Attachments` - DEFAULT_ATTACHMENTS
            * `Default: Created` - DEFAULT_CREATED_AT
            * `Default: Created by` - DEFAULT_CREATED_BY
            * `Default: Last updated` - DEFAULT_UPDATED_AT
            * `Default: Last updated by` - DEFAULT_UPDATED_BY
            * `Select` - SELECT
            * `Multiselect` - MULTISELECT
            * `Status` - STATUS
            * `User` - USER
            * `Dates` - DATES
            * `Text` - TEXT
            * `Number` - NUMBER
            * `Checkbox` - CHECKBOX
        order (str):
        hidden (bool):
        title (str):
        description (str):
        adtl (Any):
        updated_by_client_duid (Union[Unset, None, str]):
    """

    duid: str
    kind: PropertyKind
    order: str
    hidden: bool
    title: str
    description: str
    adtl: Any
    updated_by_client_duid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        kind = self.kind.value

        order = self.order
        hidden = self.hidden
        title = self.title
        description = self.description
        adtl = self.adtl
        updated_by_client_duid = self.updated_by_client_duid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "kind": kind,
                "order": order,
                "hidden": hidden,
                "title": title,
                "description": description,
                "adtl": adtl,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        kind = PropertyKind(d.pop("kind"))

        order = d.pop("order")

        hidden = d.pop("hidden")

        title = d.pop("title")

        description = d.pop("description")

        adtl = d.pop("adtl")

        updated_by_client_duid = d.pop("updatedByClientDuid", UNSET)

        property_ = cls(
            duid=duid,
            kind=kind,
            order=order,
            hidden=hidden,
            title=title,
            description=description,
            adtl=adtl,
            updated_by_client_duid=updated_by_client_duid,
        )

        property_.additional_properties = d
        return property_

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
