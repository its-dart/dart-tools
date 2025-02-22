from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chart_aggregation import ChartAggregation

T = TypeVar("T", bound="BarChartAdtl")


@_attrs_define
class BarChartAdtl:
    """
    Attributes:
        x_property_duid (str):
        stack_property_duid (Union[None, str]):
        aggregation_property_duid (Union[None, str]):
        aggregation (ChartAggregation): * `sum` - SUM
            * `avg` - AVG
            * `count` - COUNT
    """

    x_property_duid: str
    stack_property_duid: Union[None, str]
    aggregation_property_duid: Union[None, str]
    aggregation: ChartAggregation
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        x_property_duid = self.x_property_duid

        stack_property_duid: Union[None, str]
        stack_property_duid = self.stack_property_duid

        aggregation_property_duid: Union[None, str]
        aggregation_property_duid = self.aggregation_property_duid

        aggregation = self.aggregation.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "xPropertyDuid": x_property_duid,
                "stackPropertyDuid": stack_property_duid,
                "aggregationPropertyDuid": aggregation_property_duid,
                "aggregation": aggregation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        x_property_duid = d.pop("xPropertyDuid")

        def _parse_stack_property_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        stack_property_duid = _parse_stack_property_duid(d.pop("stackPropertyDuid"))

        def _parse_aggregation_property_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        aggregation_property_duid = _parse_aggregation_property_duid(d.pop("aggregationPropertyDuid"))

        aggregation = ChartAggregation(d.pop("aggregation"))

        bar_chart_adtl = cls(
            x_property_duid=x_property_duid,
            stack_property_duid=stack_property_duid,
            aggregation_property_duid=aggregation_property_duid,
            aggregation=aggregation,
        )

        bar_chart_adtl.additional_properties = d
        return bar_chart_adtl

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
