from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.property_kind import PropertyKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="PropertyUpdate")


@_attrs_define
class PropertyUpdate:
    """
    Attributes:
        duid (str):
        kind (Union[Unset, PropertyKind]): * `Default: Type` - DEFAULT_KIND
            * `Default: Title` - DEFAULT_TITLE
            * `Default: Description` - DEFAULT_DESCRIPTION
            * `Default: Dartboard` - DEFAULT_DARTBOARD
            * `Default: Status` - DEFAULT_STATUS
            * `Default: Assignees` - DEFAULT_ASSIGNEES
            * `Default: Dates` - DEFAULT_DATES
            * `Default: Priority` - DEFAULT_PRIORITY
            * `Default: Tags` - DEFAULT_TAGS
            * `Default: Size` - DEFAULT_SIZE
            * `Default: Time tracking` - DEFAULT_TIME_TRACKING
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
            * `Time tracking` - TIME_TRACKING
            * `Text` - TEXT
            * `Number` - NUMBER
            * `Checkbox` - CHECKBOX
        order (Union[Unset, str]):
        hidden (Union[Unset, bool]):
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        adtl (Union[Unset, Any]):
    """

    duid: str
    kind: Union[Unset, PropertyKind] = UNSET
    order: Union[Unset, str] = UNSET
    hidden: Union[Unset, bool] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    adtl: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        order = self.order

        hidden = self.hidden

        title = self.title

        description = self.description

        adtl = self.adtl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if order is not UNSET:
            field_dict["order"] = order
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, PropertyKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = PropertyKind(_kind)

        order = d.pop("order", UNSET)

        hidden = d.pop("hidden", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        adtl = d.pop("adtl", UNSET)

        property_update = cls(
            duid=duid,
            kind=kind,
            order=order,
            hidden=hidden,
            title=title,
            description=description,
            adtl=adtl,
        )

        property_update.additional_properties = d
        return property_update

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
