from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.icon_kind import IconKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chart import Chart


T = TypeVar("T", bound="Dashboard")


@_attrs_define
class Dashboard:
    """
    Attributes:
        duid (str):
        accessible_by_team (bool):
        accessible_by_user_duids (list[str]):
        order (str):
        title (str):
        description (str):
        icon_kind (IconKind): * `None` - NONE
            * `Icon` - ICON
            * `Emoji` - EMOJI
        icon_name_or_emoji (str):
        color_hex (str):
        layout_duid (str):
        favorited_by_user_duids (list[str]):
        charts (list['Chart']):
        updated_by_client_duid (Union[None, Unset, str]):
    """

    duid: str
    accessible_by_team: bool
    accessible_by_user_duids: list[str]
    order: str
    title: str
    description: str
    icon_kind: IconKind
    icon_name_or_emoji: str
    color_hex: str
    layout_duid: str
    favorited_by_user_duids: list[str]
    charts: list["Chart"]
    updated_by_client_duid: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        accessible_by_team = self.accessible_by_team

        accessible_by_user_duids = self.accessible_by_user_duids

        order = self.order

        title = self.title

        description = self.description

        icon_kind = self.icon_kind.value

        icon_name_or_emoji = self.icon_name_or_emoji

        color_hex = self.color_hex

        layout_duid = self.layout_duid

        favorited_by_user_duids = self.favorited_by_user_duids

        charts = []
        for charts_item_data in self.charts:
            charts_item = charts_item_data.to_dict()
            charts.append(charts_item)

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
                "accessibleByTeam": accessible_by_team,
                "accessibleByUserDuids": accessible_by_user_duids,
                "order": order,
                "title": title,
                "description": description,
                "iconKind": icon_kind,
                "iconNameOrEmoji": icon_name_or_emoji,
                "colorHex": color_hex,
                "layoutDuid": layout_duid,
                "favoritedByUserDuids": favorited_by_user_duids,
                "charts": charts,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.chart import Chart

        d = src_dict.copy()
        duid = d.pop("duid")

        accessible_by_team = d.pop("accessibleByTeam")

        accessible_by_user_duids = cast(list[str], d.pop("accessibleByUserDuids"))

        order = d.pop("order")

        title = d.pop("title")

        description = d.pop("description")

        icon_kind = IconKind(d.pop("iconKind"))

        icon_name_or_emoji = d.pop("iconNameOrEmoji")

        color_hex = d.pop("colorHex")

        layout_duid = d.pop("layoutDuid")

        favorited_by_user_duids = cast(list[str], d.pop("favoritedByUserDuids"))

        charts = []
        _charts = d.pop("charts")
        for charts_item_data in _charts:
            charts_item = Chart.from_dict(charts_item_data)

            charts.append(charts_item)

        def _parse_updated_by_client_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_client_duid = _parse_updated_by_client_duid(d.pop("updatedByClientDuid", UNSET))

        dashboard = cls(
            duid=duid,
            accessible_by_team=accessible_by_team,
            accessible_by_user_duids=accessible_by_user_duids,
            order=order,
            title=title,
            description=description,
            icon_kind=icon_kind,
            icon_name_or_emoji=icon_name_or_emoji,
            color_hex=color_hex,
            layout_duid=layout_duid,
            favorited_by_user_duids=favorited_by_user_duids,
            charts=charts,
            updated_by_client_duid=updated_by_client_duid,
        )

        dashboard.additional_properties = d
        return dashboard

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
