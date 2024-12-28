from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.icon_kind import IconKind
from ..models.view_kind import ViewKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="View")


@_attrs_define
class View:
    """
    Attributes:
        duid (str):
        kind (ViewKind): * `Custom` - CUSTOM
            * `Search` - SEARCH
            * `Trash` - TRASH
            * `My tasks` - MY_TASKS
        accessible_by_team (bool):
        accessible_by_user_duids (list[str]):
        public (bool):
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
        always_shown_property_duids (list[str]):
        always_hidden_property_duids (list[str]):
        property_order_duids (list[str]):
        property_width_map (Any):
        updated_by_client_duid (Union[None, Unset, str]):
    """

    duid: str
    kind: ViewKind
    accessible_by_team: bool
    accessible_by_user_duids: list[str]
    public: bool
    order: str
    title: str
    description: str
    icon_kind: IconKind
    icon_name_or_emoji: str
    color_hex: str
    layout_duid: str
    favorited_by_user_duids: list[str]
    always_shown_property_duids: list[str]
    always_hidden_property_duids: list[str]
    property_order_duids: list[str]
    property_width_map: Any
    updated_by_client_duid: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        kind = self.kind.value

        accessible_by_team = self.accessible_by_team

        accessible_by_user_duids = self.accessible_by_user_duids

        public = self.public

        order = self.order

        title = self.title

        description = self.description

        icon_kind = self.icon_kind.value

        icon_name_or_emoji = self.icon_name_or_emoji

        color_hex = self.color_hex

        layout_duid = self.layout_duid

        favorited_by_user_duids = self.favorited_by_user_duids

        always_shown_property_duids = self.always_shown_property_duids

        always_hidden_property_duids = self.always_hidden_property_duids

        property_order_duids = self.property_order_duids

        property_width_map = self.property_width_map

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
                "kind": kind,
                "accessibleByTeam": accessible_by_team,
                "accessibleByUserDuids": accessible_by_user_duids,
                "public": public,
                "order": order,
                "title": title,
                "description": description,
                "iconKind": icon_kind,
                "iconNameOrEmoji": icon_name_or_emoji,
                "colorHex": color_hex,
                "layoutDuid": layout_duid,
                "favoritedByUserDuids": favorited_by_user_duids,
                "alwaysShownPropertyDuids": always_shown_property_duids,
                "alwaysHiddenPropertyDuids": always_hidden_property_duids,
                "propertyOrderDuids": property_order_duids,
                "propertyWidthMap": property_width_map,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        kind = ViewKind(d.pop("kind"))

        accessible_by_team = d.pop("accessibleByTeam")

        accessible_by_user_duids = cast(list[str], d.pop("accessibleByUserDuids"))

        public = d.pop("public")

        order = d.pop("order")

        title = d.pop("title")

        description = d.pop("description")

        icon_kind = IconKind(d.pop("iconKind"))

        icon_name_or_emoji = d.pop("iconNameOrEmoji")

        color_hex = d.pop("colorHex")

        layout_duid = d.pop("layoutDuid")

        favorited_by_user_duids = cast(list[str], d.pop("favoritedByUserDuids"))

        always_shown_property_duids = cast(list[str], d.pop("alwaysShownPropertyDuids"))

        always_hidden_property_duids = cast(list[str], d.pop("alwaysHiddenPropertyDuids"))

        property_order_duids = cast(list[str], d.pop("propertyOrderDuids"))

        property_width_map = d.pop("propertyWidthMap")

        def _parse_updated_by_client_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_client_duid = _parse_updated_by_client_duid(d.pop("updatedByClientDuid", UNSET))

        view = cls(
            duid=duid,
            kind=kind,
            accessible_by_team=accessible_by_team,
            accessible_by_user_duids=accessible_by_user_duids,
            public=public,
            order=order,
            title=title,
            description=description,
            icon_kind=icon_kind,
            icon_name_or_emoji=icon_name_or_emoji,
            color_hex=color_hex,
            layout_duid=layout_duid,
            favorited_by_user_duids=favorited_by_user_duids,
            always_shown_property_duids=always_shown_property_duids,
            always_hidden_property_duids=always_hidden_property_duids,
            property_order_duids=property_order_duids,
            property_width_map=property_width_map,
            updated_by_client_duid=updated_by_client_duid,
        )

        view.additional_properties = d
        return view

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
