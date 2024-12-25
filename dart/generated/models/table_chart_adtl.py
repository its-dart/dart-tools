from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chart_aggregation import ChartAggregation

T = TypeVar("T", bound="TableChartAdtl")


@_attrs_define
class TableChartAdtl:
    """
    Attributes:
        column_property_duid (str):
        row_property_duid (Union[None, str]):
        aggregation (ChartAggregation): * `sum` - SUM
            * `avg` - AVG
            * `count` - COUNT
        aggregation_property_duid (Union[None, str]):
    """

    column_property_duid: str
    row_property_duid: Union[None, str]
    aggregation: ChartAggregation
    aggregation_property_duid: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        column_property_duid = self.column_property_duid

        row_property_duid: Union[None, str]
        row_property_duid = self.row_property_duid

        aggregation = self.aggregation.value

        aggregation_property_duid: Union[None, str]
        aggregation_property_duid = self.aggregation_property_duid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columnPropertyDuid": column_property_duid,
                "rowPropertyDuid": row_property_duid,
                "aggregation": aggregation,
                "aggregationPropertyDuid": aggregation_property_duid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        column_property_duid = d.pop("columnPropertyDuid")

        def _parse_row_property_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        row_property_duid = _parse_row_property_duid(d.pop("rowPropertyDuid"))

        aggregation = ChartAggregation(d.pop("aggregation"))

        def _parse_aggregation_property_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        aggregation_property_duid = _parse_aggregation_property_duid(d.pop("aggregationPropertyDuid"))

        table_chart_adtl = cls(
            column_property_duid=column_property_duid,
            row_property_duid=row_property_duid,
            aggregation=aggregation,
            aggregation_property_duid=aggregation_property_duid,
        )

        table_chart_adtl.additional_properties = d
        return table_chart_adtl

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
