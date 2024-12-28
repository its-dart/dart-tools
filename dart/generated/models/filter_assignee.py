from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filter_applicability import FilterApplicability
from ..models.filter_connector import FilterConnector

T = TypeVar("T", bound="FilterAssignee")


@_attrs_define
class FilterAssignee:
    """
    Attributes:
        id (str):
        field (str):
        locked (bool):
        applicability (FilterApplicability): * `is` - IS
            * `is not` - IS_NOT
            * `is not set` - IS_NOT_SET
            * `include` - INCLUDE
            * `don't include` - DO_NOT_INCLUDE
            * `are not set` - ARE_NOT_SET
            * `exists` - EXISTS
            * `exist` - EXIST
            * `contains` - CONTAINS
            * `contain` - CONTAIN
            * `is before` - IS_BEFORE
            * `is after` - IS_AFTER
            * `is between` - IS_BETWEEN
            * `is checked` - IS_CHECKED
            * `is unchecked` - IS_UNCHECKED
        connector (FilterConnector): * `or` - OR
            * `and` - AND
        values (list[Any]):
    """

    id: str
    field: str
    locked: bool
    applicability: FilterApplicability
    connector: FilterConnector
    values: list[Any]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field = self.field

        locked = self.locked

        applicability = self.applicability.value

        connector = self.connector.value

        values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "field": field,
                "locked": locked,
                "applicability": applicability,
                "connector": connector,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        field = d.pop("field")

        locked = d.pop("locked")

        applicability = FilterApplicability(d.pop("applicability"))

        connector = FilterConnector(d.pop("connector"))

        values = cast(list[Any], d.pop("values"))

        filter_assignee = cls(
            id=id,
            field=field,
            locked=locked,
            applicability=applicability,
            connector=connector,
            values=values,
        )

        filter_assignee.additional_properties = d
        return filter_assignee

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
