from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.layout_kind import LayoutKind
from ..models.summary_statistic_kind import SummaryStatisticKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_group import FilterGroup
    from ..models.layout_kind_config_map import LayoutKindConfigMap
    from ..models.sort import Sort


T = TypeVar("T", bound="Layout")


@_attrs_define
class Layout:
    """
    Attributes:
        duid (str):
        kind (LayoutKind): * `list` - LIST
            * `board` - BOARD
            * `calendar` - CALENDAR
            * `roadmap` - ROADMAP
        kind_config_map (LayoutKindConfigMap):
        filter_group (FilterGroup):
        sorts (List['Sort']):
        summary_statistic_kind (SummaryStatisticKind): * `None` - NONE
            * `TotalCount` - TOTAL_COUNT
            * `IncompleteCount` - INCOMPLETE_COUNT
            * `CompletedPercent` - COMPLETED_PERCENT
            * `TotalCountPoints` - TOTAL_COUNT_POINTS
            * `IncompleteCountPoints` - INCOMPLETE_COUNT_POINTS
            * `CompletedPercentPoints` - COMPLETED_PERCENT_POINTS
        updated_by_client_duid (Union[Unset, None, str]):
    """

    duid: str
    kind: LayoutKind
    kind_config_map: "LayoutKindConfigMap"
    filter_group: "FilterGroup"
    sorts: List["Sort"]
    summary_statistic_kind: SummaryStatisticKind
    updated_by_client_duid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        kind = self.kind.value

        kind_config_map = self.kind_config_map.to_dict()

        filter_group = self.filter_group.to_dict()

        sorts = []
        for sorts_item_data in self.sorts:
            sorts_item = sorts_item_data.to_dict()

            sorts.append(sorts_item)

        summary_statistic_kind = self.summary_statistic_kind.value

        updated_by_client_duid = self.updated_by_client_duid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "kind": kind,
                "kindConfigMap": kind_config_map,
                "filterGroup": filter_group,
                "sorts": sorts,
                "summaryStatisticKind": summary_statistic_kind,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_group import FilterGroup
        from ..models.layout_kind_config_map import LayoutKindConfigMap
        from ..models.sort import Sort

        d = src_dict.copy()
        duid = d.pop("duid")

        kind = LayoutKind(d.pop("kind"))

        kind_config_map = LayoutKindConfigMap.from_dict(d.pop("kindConfigMap"))

        filter_group = FilterGroup.from_dict(d.pop("filterGroup"))

        sorts = []
        _sorts = d.pop("sorts")
        for sorts_item_data in _sorts:
            sorts_item = Sort.from_dict(sorts_item_data)

            sorts.append(sorts_item)

        summary_statistic_kind = SummaryStatisticKind(d.pop("summaryStatisticKind"))

        updated_by_client_duid = d.pop("updatedByClientDuid", UNSET)

        layout = cls(
            duid=duid,
            kind=kind,
            kind_config_map=kind_config_map,
            filter_group=filter_group,
            sorts=sorts,
            summary_statistic_kind=summary_statistic_kind,
            updated_by_client_duid=updated_by_client_duid,
        )

        layout.additional_properties = d
        return layout

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
