from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pie_chart_display_metric import PieChartDisplayMetric

T = TypeVar("T", bound="PieChartAdtl")


@_attrs_define
class PieChartAdtl:
    """
    Attributes:
        property_duid (str):
        display_metric (PieChartDisplayMetric): * `count` - COUNT
            * `pct` - PCT
    """

    property_duid: str
    display_metric: PieChartDisplayMetric
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_duid = self.property_duid

        display_metric = self.display_metric.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "propertyDuid": property_duid,
                "displayMetric": display_metric,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        property_duid = d.pop("propertyDuid")

        display_metric = PieChartDisplayMetric(d.pop("displayMetric"))

        pie_chart_adtl = cls(
            property_duid=property_duid,
            display_metric=display_metric,
        )

        pie_chart_adtl.additional_properties = d
        return pie_chart_adtl

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
