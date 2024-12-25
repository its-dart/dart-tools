import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dartboard_kind import DartboardKind
from ..models.icon_kind import IconKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_dartboard_layout import UserDartboardLayout


T = TypeVar("T", bound="Dartboard")


@_attrs_define
class Dartboard:
    """
    Attributes:
        duid (str):
        space_duid (str):
        kind (DartboardKind): * `Active` - ACTIVE
            * `Next` - NEXT
            * `Backlog` - BACKLOG
            * `Finished` - FINISHED
            * `Custom` - CUSTOM
        order (str):
        title (str):
        description (str):
        icon_kind (IconKind): * `None` - NONE
            * `Icon` - ICON
            * `Emoji` - EMOJI
        icon_name_or_emoji (str):
        color_hex (str):
        user_duids_to_layout_duids (list['UserDartboardLayout']):
        index (Union[None, int]):
        started_at (Union[None, datetime.datetime]):
        finished_at (Union[None, datetime.datetime]):
        default_property_map (Any):
        always_shown_property_duids (list[str]):
        always_hidden_property_duids (list[str]):
        property_order_duids (list[str]):
        property_width_map (Any):
        updated_by_client_duid (Union[None, Unset, str]):
    """

    duid: str
    space_duid: str
    kind: DartboardKind
    order: str
    title: str
    description: str
    icon_kind: IconKind
    icon_name_or_emoji: str
    color_hex: str
    user_duids_to_layout_duids: list["UserDartboardLayout"]
    index: Union[None, int]
    started_at: Union[None, datetime.datetime]
    finished_at: Union[None, datetime.datetime]
    default_property_map: Any
    always_shown_property_duids: list[str]
    always_hidden_property_duids: list[str]
    property_order_duids: list[str]
    property_width_map: Any
    updated_by_client_duid: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        space_duid = self.space_duid

        kind = self.kind.value

        order = self.order

        title = self.title

        description = self.description

        icon_kind = self.icon_kind.value

        icon_name_or_emoji = self.icon_name_or_emoji

        color_hex = self.color_hex

        user_duids_to_layout_duids = []
        for user_duids_to_layout_duids_item_data in self.user_duids_to_layout_duids:
            user_duids_to_layout_duids_item = user_duids_to_layout_duids_item_data.to_dict()
            user_duids_to_layout_duids.append(user_duids_to_layout_duids_item)

        index: Union[None, int]
        index = self.index

        started_at: Union[None, str]
        if isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        finished_at: Union[None, str]
        if isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        default_property_map = self.default_property_map

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
                "spaceDuid": space_duid,
                "kind": kind,
                "order": order,
                "title": title,
                "description": description,
                "iconKind": icon_kind,
                "iconNameOrEmoji": icon_name_or_emoji,
                "colorHex": color_hex,
                "userDuidsToLayoutDuids": user_duids_to_layout_duids,
                "index": index,
                "startedAt": started_at,
                "finishedAt": finished_at,
                "defaultPropertyMap": default_property_map,
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
        from ..models.user_dartboard_layout import UserDartboardLayout

        d = src_dict.copy()
        duid = d.pop("duid")

        space_duid = d.pop("spaceDuid")

        kind = DartboardKind(d.pop("kind"))

        order = d.pop("order")

        title = d.pop("title")

        description = d.pop("description")

        icon_kind = IconKind(d.pop("iconKind"))

        icon_name_or_emoji = d.pop("iconNameOrEmoji")

        color_hex = d.pop("colorHex")

        user_duids_to_layout_duids = []
        _user_duids_to_layout_duids = d.pop("userDuidsToLayoutDuids")
        for user_duids_to_layout_duids_item_data in _user_duids_to_layout_duids:
            user_duids_to_layout_duids_item = UserDartboardLayout.from_dict(user_duids_to_layout_duids_item_data)

            user_duids_to_layout_duids.append(user_duids_to_layout_duids_item)

        def _parse_index(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        index = _parse_index(d.pop("index"))

        def _parse_started_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)

                return started_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        started_at = _parse_started_at(d.pop("startedAt"))

        def _parse_finished_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = isoparse(data)

                return finished_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        finished_at = _parse_finished_at(d.pop("finishedAt"))

        default_property_map = d.pop("defaultPropertyMap")

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

        dartboard = cls(
            duid=duid,
            space_duid=space_duid,
            kind=kind,
            order=order,
            title=title,
            description=description,
            icon_kind=icon_kind,
            icon_name_or_emoji=icon_name_or_emoji,
            color_hex=color_hex,
            user_duids_to_layout_duids=user_duids_to_layout_duids,
            index=index,
            started_at=started_at,
            finished_at=finished_at,
            default_property_map=default_property_map,
            always_shown_property_duids=always_shown_property_duids,
            always_hidden_property_duids=always_hidden_property_duids,
            property_order_duids=property_order_duids,
            property_width_map=property_width_map,
            updated_by_client_duid=updated_by_client_duid,
        )

        dartboard.additional_properties = d
        return dartboard

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
