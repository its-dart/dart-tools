from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.number_chart_aggregation import NumberChartAggregation

T = TypeVar("T", bound="NumberChartAdtl")


@_attrs_define
class NumberChartAdtl:
    """
    Attributes:
        property_duid (Union[None, str]):
        aggregation (NumberChartAggregation): * `sum` - SUM
            * `avg` - AVG
            * `count` - COUNT
        filter_by_value_id (Any):
    """

    property_duid: Union[None, str]
    aggregation: NumberChartAggregation
    filter_by_value_id: Any
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_duid: Union[None, str]
        property_duid = self.property_duid

        aggregation = self.aggregation.value

        filter_by_value_id = self.filter_by_value_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "propertyDuid": property_duid,
                "aggregation": aggregation,
                "filterByValueId": filter_by_value_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_property_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        property_duid = _parse_property_duid(d.pop("propertyDuid"))

        aggregation = NumberChartAggregation(d.pop("aggregation"))

        filter_by_value_id = d.pop("filterByValueId")

        number_chart_adtl = cls(
            property_duid=property_duid,
            aggregation=aggregation,
            filter_by_value_id=filter_by_value_id,
        )

        number_chart_adtl.additional_properties = d
        return number_chart_adtl

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
