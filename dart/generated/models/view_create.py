from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.icon_kind import IconKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="ViewCreate")


@_attrs_define
class ViewCreate:
    """
    Attributes:
        duid (str):
        order (str):
        layout_duid (str):
        accessible_by_team (Union[Unset, bool]):
        accessible_by_user_duids (Union[Unset, list[str]]):
        public (Union[Unset, bool]):
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        icon_kind (Union[Unset, IconKind]): * `None` - NONE
            * `Icon` - ICON
            * `Emoji` - EMOJI
        icon_name_or_emoji (Union[Unset, str]):
        color_hex (Union[Unset, str]):
        favorited_by_user_duids (Union[Unset, list[str]]):
        always_shown_property_duids (Union[Unset, list[str]]):
        always_hidden_property_duids (Union[Unset, list[str]]):
        property_order_duids (Union[Unset, list[str]]):
        property_width_map (Union[Unset, Any]):
    """

    duid: str
    order: str
    layout_duid: str
    accessible_by_team: Union[Unset, bool] = UNSET
    accessible_by_user_duids: Union[Unset, list[str]] = UNSET
    public: Union[Unset, bool] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    icon_kind: Union[Unset, IconKind] = UNSET
    icon_name_or_emoji: Union[Unset, str] = UNSET
    color_hex: Union[Unset, str] = UNSET
    favorited_by_user_duids: Union[Unset, list[str]] = UNSET
    always_shown_property_duids: Union[Unset, list[str]] = UNSET
    always_hidden_property_duids: Union[Unset, list[str]] = UNSET
    property_order_duids: Union[Unset, list[str]] = UNSET
    property_width_map: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        order = self.order

        layout_duid = self.layout_duid

        accessible_by_team = self.accessible_by_team

        accessible_by_user_duids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.accessible_by_user_duids, Unset):
            accessible_by_user_duids = self.accessible_by_user_duids

        public = self.public

        title = self.title

        description = self.description

        icon_kind: Union[Unset, str] = UNSET
        if not isinstance(self.icon_kind, Unset):
            icon_kind = self.icon_kind.value

        icon_name_or_emoji = self.icon_name_or_emoji

        color_hex = self.color_hex

        favorited_by_user_duids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorited_by_user_duids, Unset):
            favorited_by_user_duids = self.favorited_by_user_duids

        always_shown_property_duids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.always_shown_property_duids, Unset):
            always_shown_property_duids = self.always_shown_property_duids

        always_hidden_property_duids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.always_hidden_property_duids, Unset):
            always_hidden_property_duids = self.always_hidden_property_duids

        property_order_duids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.property_order_duids, Unset):
            property_order_duids = self.property_order_duids

        property_width_map = self.property_width_map

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "order": order,
                "layoutDuid": layout_duid,
            }
        )
        if accessible_by_team is not UNSET:
            field_dict["accessibleByTeam"] = accessible_by_team
        if accessible_by_user_duids is not UNSET:
            field_dict["accessibleByUserDuids"] = accessible_by_user_duids
        if public is not UNSET:
            field_dict["public"] = public
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
        if favorited_by_user_duids is not UNSET:
            field_dict["favoritedByUserDuids"] = favorited_by_user_duids
        if always_shown_property_duids is not UNSET:
            field_dict["alwaysShownPropertyDuids"] = always_shown_property_duids
        if always_hidden_property_duids is not UNSET:
            field_dict["alwaysHiddenPropertyDuids"] = always_hidden_property_duids
        if property_order_duids is not UNSET:
            field_dict["propertyOrderDuids"] = property_order_duids
        if property_width_map is not UNSET:
            field_dict["propertyWidthMap"] = property_width_map

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        order = d.pop("order")

        layout_duid = d.pop("layoutDuid")

        accessible_by_team = d.pop("accessibleByTeam", UNSET)

        accessible_by_user_duids = cast(list[str], d.pop("accessibleByUserDuids", UNSET))

        public = d.pop("public", UNSET)

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

        favorited_by_user_duids = cast(list[str], d.pop("favoritedByUserDuids", UNSET))

        always_shown_property_duids = cast(list[str], d.pop("alwaysShownPropertyDuids", UNSET))

        always_hidden_property_duids = cast(list[str], d.pop("alwaysHiddenPropertyDuids", UNSET))

        property_order_duids = cast(list[str], d.pop("propertyOrderDuids", UNSET))

        property_width_map = d.pop("propertyWidthMap", UNSET)

        view_create = cls(
            duid=duid,
            order=order,
            layout_duid=layout_duid,
            accessible_by_team=accessible_by_team,
            accessible_by_user_duids=accessible_by_user_duids,
            public=public,
            title=title,
            description=description,
            icon_kind=icon_kind,
            icon_name_or_emoji=icon_name_or_emoji,
            color_hex=color_hex,
            favorited_by_user_duids=favorited_by_user_duids,
            always_shown_property_duids=always_shown_property_duids,
            always_hidden_property_duids=always_hidden_property_duids,
            property_order_duids=property_order_duids,
            property_width_map=property_width_map,
        )

        view_create.additional_properties = d
        return view_create

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
