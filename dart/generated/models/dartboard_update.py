import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.color_name import ColorName
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
        color_name (Union[Unset, ColorName]): * `Red` - RED
            * `Dark Blue` - DARK_BLUE
            * `Dark Orange` - DARK_ORANGE
            * `Dark Green` - DARK_GREEN
            * `Purple` - PURPLE
            * `Dark Teal` - DARK_TEAL
            * `Pink` - PINK
            * `Orange` - ORANGE
            * `Green` - GREEN
            * `Yellow` - YELLOW
            * `Brown` - BROWN
            * `Dark Red` - DARK_RED
            * `Flat Green` - FLAT_GREEN
            * `Red Orange` - RED_ORANGE
            * `Teal` - TEAL
            * `Light Green` - LIGHT_GREEN
            * `Light Blue` - LIGHT_BLUE
            * `Light Purple` - LIGHT_PURPLE
            * `Light Orange` - LIGHT_ORANGE
            * `Light Pink` - LIGHT_PINK
            * `Tan` - TAN
            * `Dark Gray` - DARK_GRAY
            * `Light Brown` - LIGHT_BROWN
            * `Light Gray` - LIGHT_GRAY
        index (Union[Unset, None, int]):
        started_at (Union[Unset, None, datetime.datetime]):
        finished_at (Union[Unset, None, datetime.datetime]):
        always_shown_property_duids (Union[Unset, List[str]]):
        always_hidden_property_duids (Union[Unset, List[str]]):
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
    color_name: Union[Unset, ColorName] = UNSET
    index: Union[Unset, None, int] = UNSET
    started_at: Union[Unset, None, datetime.datetime] = UNSET
    finished_at: Union[Unset, None, datetime.datetime] = UNSET
    always_shown_property_duids: Union[Unset, List[str]] = UNSET
    always_hidden_property_duids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        color_name: Union[Unset, str] = UNSET
        if not isinstance(self.color_name, Unset):
            color_name = self.color_name.value

        index = self.index
        started_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat() if self.started_at else None

        finished_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.finished_at, Unset):
            finished_at = self.finished_at.isoformat() if self.finished_at else None

        always_shown_property_duids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.always_shown_property_duids, Unset):
            always_shown_property_duids = self.always_shown_property_duids

        always_hidden_property_duids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.always_hidden_property_duids, Unset):
            always_hidden_property_duids = self.always_hidden_property_duids

        field_dict: Dict[str, Any] = {}
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
        if color_name is not UNSET:
            field_dict["colorName"] = color_name
        if index is not UNSET:
            field_dict["index"] = index
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at
        if always_shown_property_duids is not UNSET:
            field_dict["alwaysShownPropertyDuids"] = always_shown_property_duids
        if always_hidden_property_duids is not UNSET:
            field_dict["alwaysHiddenPropertyDuids"] = always_hidden_property_duids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        _color_name = d.pop("colorName", UNSET)
        color_name: Union[Unset, ColorName]
        if isinstance(_color_name, Unset):
            color_name = UNSET
        else:
            color_name = ColorName(_color_name)

        index = d.pop("index", UNSET)

        _started_at = d.pop("startedAt", UNSET)
        started_at: Union[Unset, None, datetime.datetime]
        if _started_at is None:
            started_at = None
        elif isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        _finished_at = d.pop("finishedAt", UNSET)
        finished_at: Union[Unset, None, datetime.datetime]
        if _finished_at is None:
            finished_at = None
        elif isinstance(_finished_at, Unset):
            finished_at = UNSET
        else:
            finished_at = isoparse(_finished_at)

        always_shown_property_duids = cast(List[str], d.pop("alwaysShownPropertyDuids", UNSET))

        always_hidden_property_duids = cast(List[str], d.pop("alwaysHiddenPropertyDuids", UNSET))

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
            color_name=color_name,
            index=index,
            started_at=started_at,
            finished_at=finished_at,
            always_shown_property_duids=always_shown_property_duids,
            always_hidden_property_duids=always_hidden_property_duids,
        )

        dartboard_update.additional_properties = d
        return dartboard_update

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
