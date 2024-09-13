from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chart_type import ChartType

if TYPE_CHECKING:
    from ..models.bar_chart_adtl import BarChartAdtl
    from ..models.line_chart_adtl import LineChartAdtl
    from ..models.number_chart_adtl import NumberChartAdtl
    from ..models.pie_chart_adtl import PieChartAdtl
    from ..models.table_chart_adtl import TableChartAdtl


T = TypeVar("T", bound="Chart")


@_attrs_define
class Chart:
    """
    Attributes:
        duid (str):
        type (ChartType): * `bar` - BAR
            * `line` - LINE
            * `number` - NUMBER
            * `pie` - PIE
            * `table` - TABLE
        title (str):
        x (int):
        y (int):
        width (int):
        height (int):
        adtl (Union['BarChartAdtl', 'LineChartAdtl', 'NumberChartAdtl', 'PieChartAdtl', 'TableChartAdtl']):
    """

    duid: str
    type: ChartType
    title: str
    x: int
    y: int
    width: int
    height: int
    adtl: Union["BarChartAdtl", "LineChartAdtl", "NumberChartAdtl", "PieChartAdtl", "TableChartAdtl"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.bar_chart_adtl import BarChartAdtl
        from ..models.line_chart_adtl import LineChartAdtl
        from ..models.number_chart_adtl import NumberChartAdtl
        from ..models.pie_chart_adtl import PieChartAdtl

        duid = self.duid

        type = self.type.value

        title = self.title

        x = self.x

        y = self.y

        width = self.width

        height = self.height

        adtl: Dict[str, Any]
        if isinstance(self.adtl, BarChartAdtl):
            adtl = self.adtl.to_dict()
        elif isinstance(self.adtl, LineChartAdtl):
            adtl = self.adtl.to_dict()
        elif isinstance(self.adtl, NumberChartAdtl):
            adtl = self.adtl.to_dict()
        elif isinstance(self.adtl, PieChartAdtl):
            adtl = self.adtl.to_dict()
        else:
            adtl = self.adtl.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "type": type,
                "title": title,
                "x": x,
                "y": y,
                "width": width,
                "height": height,
                "adtl": adtl,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bar_chart_adtl import BarChartAdtl
        from ..models.line_chart_adtl import LineChartAdtl
        from ..models.number_chart_adtl import NumberChartAdtl
        from ..models.pie_chart_adtl import PieChartAdtl
        from ..models.table_chart_adtl import TableChartAdtl

        d = src_dict.copy()
        duid = d.pop("duid")

        type = ChartType(d.pop("type"))

        title = d.pop("title")

        x = d.pop("x")

        y = d.pop("y")

        width = d.pop("width")

        height = d.pop("height")

        def _parse_adtl(
            data: object,
        ) -> Union["BarChartAdtl", "LineChartAdtl", "NumberChartAdtl", "PieChartAdtl", "TableChartAdtl"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_chart_adtl_type_0 = BarChartAdtl.from_dict(data)

                return componentsschemas_chart_adtl_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_chart_adtl_type_1 = LineChartAdtl.from_dict(data)

                return componentsschemas_chart_adtl_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_chart_adtl_type_2 = NumberChartAdtl.from_dict(data)

                return componentsschemas_chart_adtl_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_chart_adtl_type_3 = PieChartAdtl.from_dict(data)

                return componentsschemas_chart_adtl_type_3
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_chart_adtl_type_4 = TableChartAdtl.from_dict(data)

            return componentsschemas_chart_adtl_type_4

        adtl = _parse_adtl(d.pop("adtl"))

        chart = cls(
            duid=duid,
            type=type,
            title=title,
            x=x,
            y=y,
            width=width,
            height=height,
            adtl=adtl,
        )

        chart.additional_properties = d
        return chart

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
