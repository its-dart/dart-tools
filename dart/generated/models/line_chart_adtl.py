from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LineChartAdtl")


@_attrs_define
class LineChartAdtl:
    """
    Attributes:
        x_property_duid (str):
        group_by_property_duid (str):
    """

    x_property_duid: str
    group_by_property_duid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        x_property_duid = self.x_property_duid

        group_by_property_duid = self.group_by_property_duid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "xPropertyDuid": x_property_duid,
                "groupByPropertyDuid": group_by_property_duid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        x_property_duid = d.pop("xPropertyDuid")

        group_by_property_duid = d.pop("groupByPropertyDuid")

        line_chart_adtl = cls(
            x_property_duid=x_property_duid,
            group_by_property_duid=group_by_property_duid,
        )

        line_chart_adtl.additional_properties = d
        return line_chart_adtl

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
