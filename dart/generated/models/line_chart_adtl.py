from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LineChartAdtl")


@_attrs_define
class LineChartAdtl:
    """
    Attributes:
        x_property_duid (str):
        group_by_property_duid (Union[None, str]):
    """

    x_property_duid: str
    group_by_property_duid: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        x_property_duid = self.x_property_duid

        group_by_property_duid: Union[None, str]
        group_by_property_duid = self.group_by_property_duid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "xPropertyDuid": x_property_duid,
                "groupByPropertyDuid": group_by_property_duid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        x_property_duid = d.pop("xPropertyDuid")

        def _parse_group_by_property_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        group_by_property_duid = _parse_group_by_property_duid(d.pop("groupByPropertyDuid"))

        line_chart_adtl = cls(
            x_property_duid=x_property_duid,
            group_by_property_duid=group_by_property_duid,
        )

        line_chart_adtl.additional_properties = d
        return line_chart_adtl

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
