import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.color_name import ColorName
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
            * `YC` - YC
            * `Finished` - FINISHED
            * `Custom` - CUSTOM
        order (str):
        title (str):
        description (str):
        icon_kind (IconKind): * `None` - NONE
            * `Icon` - ICON
            * `Emoji` - EMOJI
        icon_name_or_emoji (str):
        color_name (ColorName): * `Red` - RED
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
        user_duids_to_layout_duids (List['UserDartboardLayout']):
        updated_by_client_duid (Union[Unset, None, str]):
        index (Optional[int]):
        started_at (Optional[datetime.datetime]):
        finished_at (Optional[datetime.datetime]):
    """

    duid: str
    space_duid: str
    kind: DartboardKind
    order: str
    title: str
    description: str
    icon_kind: IconKind
    icon_name_or_emoji: str
    color_name: ColorName
    user_duids_to_layout_duids: List["UserDartboardLayout"]
    index: Optional[int]
    started_at: Optional[datetime.datetime]
    finished_at: Optional[datetime.datetime]
    updated_by_client_duid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        space_duid = self.space_duid
        kind = self.kind.value

        order = self.order
        title = self.title
        description = self.description
        icon_kind = self.icon_kind.value

        icon_name_or_emoji = self.icon_name_or_emoji
        color_name = self.color_name.value

        user_duids_to_layout_duids = []
        for user_duids_to_layout_duids_item_data in self.user_duids_to_layout_duids:
            user_duids_to_layout_duids_item = user_duids_to_layout_duids_item_data.to_dict()

            user_duids_to_layout_duids.append(user_duids_to_layout_duids_item)

        updated_by_client_duid = self.updated_by_client_duid
        index = self.index
        started_at = self.started_at.isoformat() if self.started_at else None

        finished_at = self.finished_at.isoformat() if self.finished_at else None

        field_dict: Dict[str, Any] = {}
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
                "colorName": color_name,
                "userDuidsToLayoutDuids": user_duids_to_layout_duids,
                "index": index,
                "startedAt": started_at,
                "finishedAt": finished_at,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        color_name = ColorName(d.pop("colorName"))

        user_duids_to_layout_duids = []
        _user_duids_to_layout_duids = d.pop("userDuidsToLayoutDuids")
        for user_duids_to_layout_duids_item_data in _user_duids_to_layout_duids:
            user_duids_to_layout_duids_item = UserDartboardLayout.from_dict(user_duids_to_layout_duids_item_data)

            user_duids_to_layout_duids.append(user_duids_to_layout_duids_item)

        updated_by_client_duid = d.pop("updatedByClientDuid", UNSET)

        index = d.pop("index")

        _started_at = d.pop("startedAt")
        started_at: Optional[datetime.datetime]
        if _started_at is None:
            started_at = None
        else:
            started_at = isoparse(_started_at)

        _finished_at = d.pop("finishedAt")
        finished_at: Optional[datetime.datetime]
        if _finished_at is None:
            finished_at = None
        else:
            finished_at = isoparse(_finished_at)

        dartboard = cls(
            duid=duid,
            space_duid=space_duid,
            kind=kind,
            order=order,
            title=title,
            description=description,
            icon_kind=icon_kind,
            icon_name_or_emoji=icon_name_or_emoji,
            color_name=color_name,
            user_duids_to_layout_duids=user_duids_to_layout_duids,
            updated_by_client_duid=updated_by_client_duid,
            index=index,
            started_at=started_at,
            finished_at=finished_at,
        )

        dartboard.additional_properties = d
        return dartboard

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
