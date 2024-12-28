from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.icon_kind import IconKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardUpdate")


@_attrs_define
class DashboardUpdate:
    """
    Attributes:
        duid (str):
        accessible_by_team (Union[Unset, bool]):
        accessible_by_user_duids (Union[Unset, list[str]]):
        order (Union[Unset, str]):
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        icon_kind (Union[Unset, IconKind]): * `None` - NONE
            * `Icon` - ICON
            * `Emoji` - EMOJI
        icon_name_or_emoji (Union[Unset, str]):
        color_hex (Union[Unset, str]):
        layout_duid (Union[Unset, str]):
        favorited_by_user_duids (Union[Unset, list[str]]):
        charts (Union[Unset, Any]):
    """

    duid: str
    accessible_by_team: Union[Unset, bool] = UNSET
    accessible_by_user_duids: Union[Unset, list[str]] = UNSET
    order: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    icon_kind: Union[Unset, IconKind] = UNSET
    icon_name_or_emoji: Union[Unset, str] = UNSET
    color_hex: Union[Unset, str] = UNSET
    layout_duid: Union[Unset, str] = UNSET
    favorited_by_user_duids: Union[Unset, list[str]] = UNSET
    charts: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        accessible_by_team = self.accessible_by_team

        accessible_by_user_duids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.accessible_by_user_duids, Unset):
            accessible_by_user_duids = self.accessible_by_user_duids

        order = self.order

        title = self.title

        description = self.description

        icon_kind: Union[Unset, str] = UNSET
        if not isinstance(self.icon_kind, Unset):
            icon_kind = self.icon_kind.value

        icon_name_or_emoji = self.icon_name_or_emoji

        color_hex = self.color_hex

        layout_duid = self.layout_duid

        favorited_by_user_duids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorited_by_user_duids, Unset):
            favorited_by_user_duids = self.favorited_by_user_duids

        charts = self.charts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if accessible_by_team is not UNSET:
            field_dict["accessibleByTeam"] = accessible_by_team
        if accessible_by_user_duids is not UNSET:
            field_dict["accessibleByUserDuids"] = accessible_by_user_duids
        if order is not UNSET:
            field_dict["order"] = order
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if icon_kind is not UNSET:
            field_dict["iconKind"] = icon_kind
        if icon_name_or_emoji is not UNSET:
            field_dict["iconNameOrEmoji"] = icon_name_or_emoji
        if color_hex is not UNSET:
            field_dict["colorHex"] = color_hex
        if layout_duid is not UNSET:
            field_dict["layoutDuid"] = layout_duid
        if favorited_by_user_duids is not UNSET:
            field_dict["favoritedByUserDuids"] = favorited_by_user_duids
        if charts is not UNSET:
            field_dict["charts"] = charts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        accessible_by_team = d.pop("accessibleByTeam", UNSET)

        accessible_by_user_duids = cast(list[str], d.pop("accessibleByUserDuids", UNSET))

        order = d.pop("order", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _icon_kind = d.pop("iconKind", UNSET)
        icon_kind: Union[Unset, IconKind]
        if isinstance(_icon_kind, Unset):
            icon_kind = UNSET
        else:
            icon_kind = IconKind(_icon_kind)

        icon_name_or_emoji = d.pop("iconNameOrEmoji", UNSET)

        color_hex = d.pop("colorHex", UNSET)

        layout_duid = d.pop("layoutDuid", UNSET)

        favorited_by_user_duids = cast(list[str], d.pop("favoritedByUserDuids", UNSET))

        charts = d.pop("charts", UNSET)

        dashboard_update = cls(
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
        )

        dashboard_update.additional_properties = d
        return dashboard_update

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
