import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

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
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        kind (LayoutKind): * `list` - LIST
            * `board` - BOARD
            * `calendar` - CALENDAR
            * `roadmap` - ROADMAP
        kind_config_map (LayoutKindConfigMap):
        filter_group (FilterGroup):
        sorts (list['Sort']):
        summary_statistic_kind (SummaryStatisticKind): * `None` - NONE
            * `TotalCount` - TOTAL_COUNT
            * `IncompleteCount` - INCOMPLETE_COUNT
            * `CompletedPercent` - COMPLETED_PERCENT
            * `TotalCountPoints` - TOTAL_COUNT_POINTS
            * `IncompleteCountPoints` - INCOMPLETE_COUNT_POINTS
            * `CompletedPercentPoints` - COMPLETED_PERCENT_POINTS
        updated_by_client_duid (Union[None, Unset, str]):
    """

    duid: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    kind: LayoutKind
    kind_config_map: "LayoutKindConfigMap"
    filter_group: "FilterGroup"
    sorts: list["Sort"]
    summary_statistic_kind: SummaryStatisticKind
    updated_by_client_duid: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        kind = self.kind.value

        kind_config_map = self.kind_config_map.to_dict()

        filter_group = self.filter_group.to_dict()

        sorts = []
        for sorts_item_data in self.sorts:
            sorts_item = sorts_item_data.to_dict()
            sorts.append(sorts_item)

        summary_statistic_kind = self.summary_statistic_kind.value

        updated_by_client_duid: Union[None, Unset, str]
        if isinstance(self.updated_by_client_duid, Unset):
            updated_by_client_duid = UNSET
        else:
            updated_by_client_duid = self.updated_by_client_duid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "createdAt": created_at,
                "updatedAt": updated_at,
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.filter_group import FilterGroup
        from ..models.layout_kind_config_map import LayoutKindConfigMap
        from ..models.sort import Sort

        d = src_dict.copy()
        duid = d.pop("duid")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        kind = LayoutKind(d.pop("kind"))

        kind_config_map = LayoutKindConfigMap.from_dict(d.pop("kindConfigMap"))

        filter_group = FilterGroup.from_dict(d.pop("filterGroup"))

        sorts = []
        _sorts = d.pop("sorts")
        for sorts_item_data in _sorts:
            sorts_item = Sort.from_dict(sorts_item_data)

            sorts.append(sorts_item)

        summary_statistic_kind = SummaryStatisticKind(d.pop("summaryStatisticKind"))

        def _parse_updated_by_client_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_client_duid = _parse_updated_by_client_duid(d.pop("updatedByClientDuid", UNSET))

        layout = cls(
            duid=duid,
            created_at=created_at,
            updated_at=updated_at,
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
