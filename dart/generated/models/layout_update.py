from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.layout_kind import LayoutKind
from ..models.summary_statistic_kind import SummaryStatisticKind
from ..types import UNSET, Unset

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
        kind_config_map (Union[Unset, Any]):
        filter_group (Union[Unset, Any]):
        sorts (Union[Unset, Any]):
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
    kind_config_map: Union[Unset, Any] = UNSET
    filter_group: Union[Unset, Any] = UNSET
    sorts: Union[Unset, Any] = UNSET
    summary_statistic_kind: Union[Unset, SummaryStatisticKind] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        kind_config_map = self.kind_config_map

        filter_group = self.filter_group

        sorts = self.sorts

        summary_statistic_kind: Union[Unset, str] = UNSET
        if not isinstance(self.summary_statistic_kind, Unset):
            summary_statistic_kind = self.summary_statistic_kind.value

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, LayoutKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = LayoutKind(_kind)

        kind_config_map = d.pop("kindConfigMap", UNSET)

        filter_group = d.pop("filterGroup", UNSET)

        sorts = d.pop("sorts", UNSET)

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
