from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chart_aggregation import ChartAggregation

T = TypeVar("T", bound="NumberChartAdtl")


@_attrs_define
class NumberChartAdtl:
    """
    Attributes:
        property_duid (Union[None, str]):
        aggregation (ChartAggregation): * `sum` - SUM
            * `avg` - AVG
            * `count` - COUNT
    """

    property_duid: Union[None, str]
    aggregation: ChartAggregation
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        property_duid: Union[None, str]
        property_duid = self.property_duid

        aggregation = self.aggregation.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "propertyDuid": property_duid,
                "aggregation": aggregation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_property_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        property_duid = _parse_property_duid(d.pop("propertyDuid"))

        aggregation = ChartAggregation(d.pop("aggregation"))

        number_chart_adtl = cls(
            property_duid=property_duid,
            aggregation=aggregation,
        )

        number_chart_adtl.additional_properties = d
        return number_chart_adtl

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
