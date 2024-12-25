import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

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
        drafter_duid (Union[None, str]):
        kind (SpaceKind): * `Other` - OTHER
            * `Workspace` - WORKSPACE
            * `Personal` - PERSONAL
        accessible_by_team (bool):
        accessible_by_user_duids (list[str]):
        order (str):
        title (str):
        abrev (str):
        description (str):
        icon_kind (IconKind): * `None` - NONE
            * `Icon` - ICON
            * `Emoji` - EMOJI
        icon_name_or_emoji (str):
        color_hex (str):
        sprint_mode (SprintMode): * `None` - NONE
            * `ANBA` - ANBA
        sprint_replicate_on_rollover (bool):
        sprint_name_fmt (str):
        standup_recurrence (Union[Any, None]):
        standup_recurs_next_at (Union[None, datetime.datetime]):
        changelog_recurrence (Union[Any, None]):
        changelog_recurs_next_at (Union[None, datetime.datetime]):
        rollover_recurrence (Union[Any, None]):
        rollover_recurs_next_at (Union[None, datetime.datetime]):
        updated_by_client_duid (Union[None, Unset, str]):
    """

    duid: str
    drafter_duid: Union[None, str]
    kind: SpaceKind
    accessible_by_team: bool
    accessible_by_user_duids: list[str]
    order: str
    title: str
    abrev: str
    description: str
    icon_kind: IconKind
    icon_name_or_emoji: str
    color_hex: str
    sprint_mode: SprintMode
    sprint_replicate_on_rollover: bool
    sprint_name_fmt: str
    standup_recurrence: Union[Any, None]
    standup_recurs_next_at: Union[None, datetime.datetime]
    changelog_recurrence: Union[Any, None]
    changelog_recurs_next_at: Union[None, datetime.datetime]
    rollover_recurrence: Union[Any, None]
    rollover_recurs_next_at: Union[None, datetime.datetime]
    updated_by_client_duid: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        drafter_duid: Union[None, str]
        drafter_duid = self.drafter_duid

        kind = self.kind.value

        accessible_by_team = self.accessible_by_team

        accessible_by_user_duids = self.accessible_by_user_duids

        order = self.order

        title = self.title

        abrev = self.abrev

        description = self.description

        icon_kind = self.icon_kind.value

        icon_name_or_emoji = self.icon_name_or_emoji

        color_hex = self.color_hex

        sprint_mode = self.sprint_mode.value

        sprint_replicate_on_rollover = self.sprint_replicate_on_rollover

        sprint_name_fmt = self.sprint_name_fmt

        standup_recurrence: Union[Any, None]
        standup_recurrence = self.standup_recurrence

        standup_recurs_next_at: Union[None, str]
        if isinstance(self.standup_recurs_next_at, datetime.datetime):
            standup_recurs_next_at = self.standup_recurs_next_at.isoformat()
        else:
            standup_recurs_next_at = self.standup_recurs_next_at

        changelog_recurrence: Union[Any, None]
        changelog_recurrence = self.changelog_recurrence

        changelog_recurs_next_at: Union[None, str]
        if isinstance(self.changelog_recurs_next_at, datetime.datetime):
            changelog_recurs_next_at = self.changelog_recurs_next_at.isoformat()
        else:
            changelog_recurs_next_at = self.changelog_recurs_next_at

        rollover_recurrence: Union[Any, None]
        rollover_recurrence = self.rollover_recurrence

        rollover_recurs_next_at: Union[None, str]
        if isinstance(self.rollover_recurs_next_at, datetime.datetime):
            rollover_recurs_next_at = self.rollover_recurs_next_at.isoformat()
        else:
            rollover_recurs_next_at = self.rollover_recurs_next_at

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
                "drafterDuid": drafter_duid,
                "kind": kind,
                "accessibleByTeam": accessible_by_team,
                "accessibleByUserDuids": accessible_by_user_duids,
                "order": order,
                "title": title,
                "abrev": abrev,
                "description": description,
                "iconKind": icon_kind,
                "iconNameOrEmoji": icon_name_or_emoji,
                "colorHex": color_hex,
                "sprintMode": sprint_mode,
                "sprintReplicateOnRollover": sprint_replicate_on_rollover,
                "sprintNameFmt": sprint_name_fmt,
                "standupRecurrence": standup_recurrence,
                "standupRecursNextAt": standup_recurs_next_at,
                "changelogRecurrence": changelog_recurrence,
                "changelogRecursNextAt": changelog_recurs_next_at,
                "rolloverRecurrence": rollover_recurrence,
                "rolloverRecursNextAt": rollover_recurs_next_at,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        def _parse_drafter_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        drafter_duid = _parse_drafter_duid(d.pop("drafterDuid"))

        kind = SpaceKind(d.pop("kind"))

        accessible_by_team = d.pop("accessibleByTeam")

        accessible_by_user_duids = cast(list[str], d.pop("accessibleByUserDuids"))

        order = d.pop("order")

        title = d.pop("title")

        abrev = d.pop("abrev")

        description = d.pop("description")

        icon_kind = IconKind(d.pop("iconKind"))

        icon_name_or_emoji = d.pop("iconNameOrEmoji")

        color_hex = d.pop("colorHex")

        sprint_mode = SprintMode(d.pop("sprintMode"))

        sprint_replicate_on_rollover = d.pop("sprintReplicateOnRollover")

        sprint_name_fmt = d.pop("sprintNameFmt")

        def _parse_standup_recurrence(data: object) -> Union[Any, None]:
            if data is None:
                return data
            return cast(Union[Any, None], data)

        standup_recurrence = _parse_standup_recurrence(d.pop("standupRecurrence"))

        def _parse_standup_recurs_next_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                standup_recurs_next_at_type_0 = isoparse(data)

                return standup_recurs_next_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        standup_recurs_next_at = _parse_standup_recurs_next_at(d.pop("standupRecursNextAt"))

        def _parse_changelog_recurrence(data: object) -> Union[Any, None]:
            if data is None:
                return data
            return cast(Union[Any, None], data)

        changelog_recurrence = _parse_changelog_recurrence(d.pop("changelogRecurrence"))

        def _parse_changelog_recurs_next_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                changelog_recurs_next_at_type_0 = isoparse(data)

                return changelog_recurs_next_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        changelog_recurs_next_at = _parse_changelog_recurs_next_at(d.pop("changelogRecursNextAt"))

        def _parse_rollover_recurrence(data: object) -> Union[Any, None]:
            if data is None:
                return data
            return cast(Union[Any, None], data)

        rollover_recurrence = _parse_rollover_recurrence(d.pop("rolloverRecurrence"))

        def _parse_rollover_recurs_next_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rollover_recurs_next_at_type_0 = isoparse(data)

                return rollover_recurs_next_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        rollover_recurs_next_at = _parse_rollover_recurs_next_at(d.pop("rolloverRecursNextAt"))

        def _parse_updated_by_client_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_client_duid = _parse_updated_by_client_duid(d.pop("updatedByClientDuid", UNSET))

        space = cls(
            duid=duid,
            drafter_duid=drafter_duid,
            kind=kind,
            accessible_by_team=accessible_by_team,
            accessible_by_user_duids=accessible_by_user_duids,
            order=order,
            title=title,
            abrev=abrev,
            description=description,
            icon_kind=icon_kind,
            icon_name_or_emoji=icon_name_or_emoji,
            color_hex=color_hex,
            sprint_mode=sprint_mode,
            sprint_replicate_on_rollover=sprint_replicate_on_rollover,
            sprint_name_fmt=sprint_name_fmt,
            standup_recurrence=standup_recurrence,
            standup_recurs_next_at=standup_recurs_next_at,
            changelog_recurrence=changelog_recurrence,
            changelog_recurs_next_at=changelog_recurs_next_at,
            rollover_recurrence=rollover_recurrence,
            rollover_recurs_next_at=rollover_recurs_next_at,
            updated_by_client_duid=updated_by_client_duid,
        )

        space.additional_properties = d
        return space

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
