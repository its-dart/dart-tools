import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.color_name import ColorName
from ..models.icon_kind import IconKind
from ..models.space_kind import SpaceKind
from ..models.sprint_mode import SprintMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="Space")


@_attrs_define
class Space:
    """
    Attributes:
        duid (str):
        kind (SpaceKind): * `Other` - OTHER
            * `Workspace` - WORKSPACE
            * `Personal` - PERSONAL
        accessible_by_team (bool):
        accessible_by_user_duids (List[str]):
        order (str):
        title (str):
        abrev (str):
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
        sprint_mode (SprintMode): * `None` - NONE
            * `ANBA` - ANBA
        standup_recurrence (Any):
        changelog_recurrence (Any):
        updated_by_client_duid (Union[Unset, None, str]):
        drafter_duid (Optional[str]):
        standup_recurrs_next_at (Optional[datetime.datetime]):
        changelog_recurrs_next_at (Optional[datetime.datetime]):
    """

    duid: str
    kind: SpaceKind
    accessible_by_team: bool
    accessible_by_user_duids: List[str]
    order: str
    title: str
    abrev: str
    description: str
    icon_kind: IconKind
    icon_name_or_emoji: str
    color_name: ColorName
    sprint_mode: SprintMode
    standup_recurrence: Any
    changelog_recurrence: Any
    drafter_duid: Optional[str]
    standup_recurrs_next_at: Optional[datetime.datetime]
    changelog_recurrs_next_at: Optional[datetime.datetime]
    updated_by_client_duid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        kind = self.kind.value

        accessible_by_team = self.accessible_by_team
        accessible_by_user_duids = self.accessible_by_user_duids

        order = self.order
        title = self.title
        abrev = self.abrev
        description = self.description
        icon_kind = self.icon_kind.value

        icon_name_or_emoji = self.icon_name_or_emoji
        color_name = self.color_name.value

        sprint_mode = self.sprint_mode.value

        standup_recurrence = self.standup_recurrence
        changelog_recurrence = self.changelog_recurrence
        updated_by_client_duid = self.updated_by_client_duid
        drafter_duid = self.drafter_duid
        standup_recurrs_next_at = self.standup_recurrs_next_at.isoformat() if self.standup_recurrs_next_at else None

        changelog_recurrs_next_at = (
            self.changelog_recurrs_next_at.isoformat() if self.changelog_recurrs_next_at else None
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "kind": kind,
                "accessibleByTeam": accessible_by_team,
                "accessibleByUserDuids": accessible_by_user_duids,
                "order": order,
                "title": title,
                "abrev": abrev,
                "description": description,
                "iconKind": icon_kind,
                "iconNameOrEmoji": icon_name_or_emoji,
                "colorName": color_name,
                "sprintMode": sprint_mode,
                "standupRecurrence": standup_recurrence,
                "changelogRecurrence": changelog_recurrence,
                "drafterDuid": drafter_duid,
                "standupRecurrsNextAt": standup_recurrs_next_at,
                "changelogRecurrsNextAt": changelog_recurrs_next_at,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        kind = SpaceKind(d.pop("kind"))

        accessible_by_team = d.pop("accessibleByTeam")

        accessible_by_user_duids = cast(List[str], d.pop("accessibleByUserDuids"))

        order = d.pop("order")

        title = d.pop("title")

        abrev = d.pop("abrev")

        description = d.pop("description")

        icon_kind = IconKind(d.pop("iconKind"))

        icon_name_or_emoji = d.pop("iconNameOrEmoji")

        color_name = ColorName(d.pop("colorName"))

        sprint_mode = SprintMode(d.pop("sprintMode"))

        standup_recurrence = d.pop("standupRecurrence")

        changelog_recurrence = d.pop("changelogRecurrence")

        updated_by_client_duid = d.pop("updatedByClientDuid", UNSET)

        drafter_duid = d.pop("drafterDuid")

        _standup_recurrs_next_at = d.pop("standupRecurrsNextAt")
        standup_recurrs_next_at: Optional[datetime.datetime]
        if _standup_recurrs_next_at is None:
            standup_recurrs_next_at = None
        else:
            standup_recurrs_next_at = isoparse(_standup_recurrs_next_at)

        _changelog_recurrs_next_at = d.pop("changelogRecurrsNextAt")
        changelog_recurrs_next_at: Optional[datetime.datetime]
        if _changelog_recurrs_next_at is None:
            changelog_recurrs_next_at = None
        else:
            changelog_recurrs_next_at = isoparse(_changelog_recurrs_next_at)

        space = cls(
            duid=duid,
            kind=kind,
            accessible_by_team=accessible_by_team,
            accessible_by_user_duids=accessible_by_user_duids,
            order=order,
            title=title,
            abrev=abrev,
            description=description,
            icon_kind=icon_kind,
            icon_name_or_emoji=icon_name_or_emoji,
            color_name=color_name,
            sprint_mode=sprint_mode,
            standup_recurrence=standup_recurrence,
            changelog_recurrence=changelog_recurrence,
            updated_by_client_duid=updated_by_client_duid,
            drafter_duid=drafter_duid,
            standup_recurrs_next_at=standup_recurrs_next_at,
            changelog_recurrs_next_at=changelog_recurrs_next_at,
        )

        space.additional_properties = d
        return space

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
