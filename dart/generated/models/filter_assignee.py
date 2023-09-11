from typing import Any, Dict, List, Type, TypeVar, cast

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
        connector (FilterConnector): * `or` - OR
            * `and` - AND
        values (List[Any]):
    """

    id: str
    field: str
    locked: bool
    applicability: FilterApplicability
    connector: FilterConnector
    values: List[Any]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        field = self.field
        locked = self.locked
        applicability = self.applicability.value

        connector = self.connector.value

        values = self.values

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        field = d.pop("field")

        locked = d.pop("locked")

        applicability = FilterApplicability(d.pop("applicability"))

        connector = FilterConnector(d.pop("connector"))

        values = cast(List[Any], d.pop("values"))

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
