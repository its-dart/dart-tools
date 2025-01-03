from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FilterSearch")


@_attrs_define
class FilterSearch:
    """
    Attributes:
        id (str):
        field (str):
        locked (bool):
        values (list[Any]):
    """

    id: str
    field: str
    locked: bool
    values: list[Any]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field = self.field

        locked = self.locked

        values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "field": field,
                "locked": locked,
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

        values = cast(list[Any], d.pop("values"))

        filter_search = cls(
            id=id,
            field=field,
            locked=locked,
            values=values,
        )

        filter_search.additional_properties = d
        return filter_search

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
