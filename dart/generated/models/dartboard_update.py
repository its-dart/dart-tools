import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dartboard_kind import DartboardKind
from ..models.icon_kind import IconKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="DartboardUpdate")


@_attrs_define
class DartboardUpdate:
    """
    Attributes:
        duid (str):
        space_duid (Union[Unset, str]):
        kind (Union[Unset, DartboardKind]): * `Active` - ACTIVE
            * `Next` - NEXT
            * `Backlog` - BACKLOG
            * `Finished` - FINISHED
            * `Custom` - CUSTOM
        order (Union[Unset, str]):
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        icon_kind (Union[Unset, IconKind]): * `None` - NONE
            * `Icon` - ICON
            * `Emoji` - EMOJI
        icon_name_or_emoji (Union[Unset, str]):
        color_hex (Union[Unset, str]):
        index (Union[None, Unset, int]):
        started_at (Union[None, Unset, datetime.datetime]):
        finished_at (Union[None, Unset, datetime.datetime]):
        default_property_map (Union[Unset, Any]):
        always_shown_property_duids (Union[Unset, list[str]]):
        always_hidden_property_duids (Union[Unset, list[str]]):
        property_order_duids (Union[Unset, list[str]]):
        property_width_map (Union[Unset, Any]):
    """

    duid: str
    space_duid: Union[Unset, str] = UNSET
    kind: Union[Unset, DartboardKind] = UNSET
    order: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    icon_kind: Union[Unset, IconKind] = UNSET
    icon_name_or_emoji: Union[Unset, str] = UNSET
    color_hex: Union[Unset, str] = UNSET
    index: Union[None, Unset, int] = UNSET
    started_at: Union[None, Unset, datetime.datetime] = UNSET
    finished_at: Union[None, Unset, datetime.datetime] = UNSET
    default_property_map: Union[Unset, Any] = UNSET
    always_shown_property_duids: Union[Unset, list[str]] = UNSET
    always_hidden_property_duids: Union[Unset, list[str]] = UNSET
    property_order_duids: Union[Unset, list[str]] = UNSET
    property_width_map: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        space_duid = self.space_duid

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        order = self.order

        title = self.title

        description = self.description

        icon_kind: Union[Unset, str] = UNSET
        if not isinstance(self.icon_kind, Unset):
            icon_kind = self.icon_kind.value

        icon_name_or_emoji = self.icon_name_or_emoji

        color_hex = self.color_hex

        index: Union[None, Unset, int]
        if isinstance(self.index, Unset):
            index = UNSET
        else:
            index = self.index

        started_at: Union[None, Unset, str]
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        finished_at: Union[None, Unset, str]
        if isinstance(self.finished_at, Unset):
            finished_at = UNSET
        elif isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        default_property_map = self.default_property_map

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
            }
        )
        if space_duid is not UNSET:
            field_dict["spaceDuid"] = space_duid
        if kind is not UNSET:
            field_dict["kind"] = kind
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
        if index is not UNSET:
            field_dict["index"] = index
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at
        if default_property_map is not UNSET:
            field_dict["defaultPropertyMap"] = default_property_map
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

        space_duid = d.pop("spaceDuid", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, DartboardKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = DartboardKind(_kind)

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

        def _parse_index(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        index = _parse_index(d.pop("index", UNSET))

        def _parse_started_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)

                return started_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        started_at = _parse_started_at(d.pop("startedAt", UNSET))

        def _parse_finished_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = isoparse(data)

                return finished_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        finished_at = _parse_finished_at(d.pop("finishedAt", UNSET))

        default_property_map = d.pop("defaultPropertyMap", UNSET)

        always_shown_property_duids = cast(list[str], d.pop("alwaysShownPropertyDuids", UNSET))

        always_hidden_property_duids = cast(list[str], d.pop("alwaysHiddenPropertyDuids", UNSET))

        property_order_duids = cast(list[str], d.pop("propertyOrderDuids", UNSET))

        property_width_map = d.pop("propertyWidthMap", UNSET)

        dartboard_update = cls(
            duid=duid,
            space_duid=space_duid,
            kind=kind,
            order=order,
            title=title,
            description=description,
            icon_kind=icon_kind,
            icon_name_or_emoji=icon_name_or_emoji,
            color_hex=color_hex,
            index=index,
            started_at=started_at,
            finished_at=finished_at,
            default_property_map=default_property_map,
            always_shown_property_duids=always_shown_property_duids,
            always_hidden_property_duids=always_hidden_property_duids,
            property_order_duids=property_order_duids,
            property_width_map=property_width_map,
        )

        dartboard_update.additional_properties = d
        return dartboard_update

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
