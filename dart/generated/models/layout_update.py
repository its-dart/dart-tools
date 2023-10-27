from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.layout_kind import LayoutKind
from ..models.summary_statistic_kind import SummaryStatisticKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.layout_update_filter_group import LayoutUpdateFilterGroup
    from ..models.layout_update_kind_config_map import LayoutUpdateKindConfigMap
    from ..models.layout_update_sorts import LayoutUpdateSorts


T = TypeVar("T", bound="LayoutUpdate")


@_attrs_define
class LayoutUpdate:
    """
    Attributes:
        duid (str):
        kind (Union[Unset, LayoutKind]): * `list` - LIST
            * `board` - BOARD
            * `calendar` - CALENDAR
            * `roadmap` - ROADMAP
        kind_config_map (Union[Unset, LayoutUpdateKindConfigMap]):
        filter_group (Union[Unset, LayoutUpdateFilterGroup]):
        sorts (Union[Unset, LayoutUpdateSorts]):
        summary_statistic_kind (Union[Unset, SummaryStatisticKind]): * `None` - NONE
            * `TotalCount` - TOTAL_COUNT
            * `IncompleteCount` - INCOMPLETE_COUNT
            * `CompletedPercent` - COMPLETED_PERCENT
            * `TotalCountPoints` - TOTAL_COUNT_POINTS
            * `IncompleteCountPoints` - INCOMPLETE_COUNT_POINTS
            * `CompletedPercentPoints` - COMPLETED_PERCENT_POINTS
    """

    duid: str
    kind: Union[Unset, LayoutKind] = UNSET
    kind_config_map: Union[Unset, "LayoutUpdateKindConfigMap"] = UNSET
    filter_group: Union[Unset, "LayoutUpdateFilterGroup"] = UNSET
    sorts: Union[Unset, "LayoutUpdateSorts"] = UNSET
    summary_statistic_kind: Union[Unset, SummaryStatisticKind] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        kind_config_map: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.kind_config_map, Unset):
            kind_config_map = self.kind_config_map.to_dict()

        filter_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_group, Unset):
            filter_group = self.filter_group.to_dict()

        sorts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sorts, Unset):
            sorts = self.sorts.to_dict()

        summary_statistic_kind: Union[Unset, str] = UNSET
        if not isinstance(self.summary_statistic_kind, Unset):
            summary_statistic_kind = self.summary_statistic_kind.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if kind_config_map is not UNSET:
            field_dict["kindConfigMap"] = kind_config_map
        if filter_group is not UNSET:
            field_dict["filterGroup"] = filter_group
        if sorts is not UNSET:
            field_dict["sorts"] = sorts
        if summary_statistic_kind is not UNSET:
            field_dict["summaryStatisticKind"] = summary_statistic_kind

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.layout_update_filter_group import LayoutUpdateFilterGroup
        from ..models.layout_update_kind_config_map import LayoutUpdateKindConfigMap
        from ..models.layout_update_sorts import LayoutUpdateSorts

        d = src_dict.copy()
        duid = d.pop("duid")

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, LayoutKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = LayoutKind(_kind)

        _kind_config_map = d.pop("kindConfigMap", UNSET)
        kind_config_map: Union[Unset, LayoutUpdateKindConfigMap]
        if isinstance(_kind_config_map, Unset):
            kind_config_map = UNSET
        else:
            kind_config_map = LayoutUpdateKindConfigMap.from_dict(_kind_config_map)

        _filter_group = d.pop("filterGroup", UNSET)
        filter_group: Union[Unset, LayoutUpdateFilterGroup]
        if isinstance(_filter_group, Unset):
            filter_group = UNSET
        else:
            filter_group = LayoutUpdateFilterGroup.from_dict(_filter_group)

        _sorts = d.pop("sorts", UNSET)
        sorts: Union[Unset, LayoutUpdateSorts]
        if isinstance(_sorts, Unset):
            sorts = UNSET
        else:
            sorts = LayoutUpdateSorts.from_dict(_sorts)

        _summary_statistic_kind = d.pop("summaryStatisticKind", UNSET)
        summary_statistic_kind: Union[Unset, SummaryStatisticKind]
        if isinstance(_summary_statistic_kind, Unset):
            summary_statistic_kind = UNSET
        else:
            summary_statistic_kind = SummaryStatisticKind(_summary_statistic_kind)

        layout_update = cls(
            duid=duid,
            kind=kind,
            kind_config_map=kind_config_map,
            filter_group=filter_group,
            sorts=sorts,
            summary_statistic_kind=summary_statistic_kind,
        )

        layout_update.additional_properties = d
        return layout_update

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
