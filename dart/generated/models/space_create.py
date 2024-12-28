import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.icon_kind import IconKind
from ..models.sprint_mode import SprintMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="SpaceCreate")


@_attrs_define
class SpaceCreate:
    """
    Attributes:
        duid (str):
        order (str):
        drafter_duid (Union[None, Unset, str]):
        accessible_by_team (Union[Unset, bool]):
        accessible_by_user_duids (Union[Unset, list[str]]):
        title (Union[Unset, str]):
        abrev (Union[Unset, str]):
        description (Union[Unset, str]):
        icon_kind (Union[Unset, IconKind]): * `None` - NONE
            * `Icon` - ICON
            * `Emoji` - EMOJI
        icon_name_or_emoji (Union[Unset, str]):
        color_hex (Union[Unset, str]):
        sprint_mode (Union[Unset, SprintMode]): * `None` - NONE
            * `ANBA` - ANBA
        sprint_replicate_on_rollover (Union[Unset, bool]):
        sprint_name_fmt (Union[Unset, str]):
        standup_recurrence (Union[Any, None, Unset]):
        standup_recurs_next_at (Union[None, Unset, datetime.datetime]):
        changelog_recurrence (Union[Any, None, Unset]):
        changelog_recurs_next_at (Union[None, Unset, datetime.datetime]):
        rollover_recurrence (Union[Any, None, Unset]):
        rollover_recurs_next_at (Union[None, Unset, datetime.datetime]):
    """

    duid: str
    order: str
    drafter_duid: Union[None, Unset, str] = UNSET
    accessible_by_team: Union[Unset, bool] = UNSET
    accessible_by_user_duids: Union[Unset, list[str]] = UNSET
    title: Union[Unset, str] = UNSET
    abrev: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    icon_kind: Union[Unset, IconKind] = UNSET
    icon_name_or_emoji: Union[Unset, str] = UNSET
    color_hex: Union[Unset, str] = UNSET
    sprint_mode: Union[Unset, SprintMode] = UNSET
    sprint_replicate_on_rollover: Union[Unset, bool] = UNSET
    sprint_name_fmt: Union[Unset, str] = UNSET
    standup_recurrence: Union[Any, None, Unset] = UNSET
    standup_recurs_next_at: Union[None, Unset, datetime.datetime] = UNSET
    changelog_recurrence: Union[Any, None, Unset] = UNSET
    changelog_recurs_next_at: Union[None, Unset, datetime.datetime] = UNSET
    rollover_recurrence: Union[Any, None, Unset] = UNSET
    rollover_recurs_next_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        order = self.order

        drafter_duid: Union[None, Unset, str]
        if isinstance(self.drafter_duid, Unset):
            drafter_duid = UNSET
        else:
            drafter_duid = self.drafter_duid

        accessible_by_team = self.accessible_by_team

        accessible_by_user_duids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.accessible_by_user_duids, Unset):
            accessible_by_user_duids = self.accessible_by_user_duids

        title = self.title

        abrev = self.abrev

        description = self.description

        icon_kind: Union[Unset, str] = UNSET
        if not isinstance(self.icon_kind, Unset):
            icon_kind = self.icon_kind.value

        icon_name_or_emoji = self.icon_name_or_emoji

        color_hex = self.color_hex

        sprint_mode: Union[Unset, str] = UNSET
        if not isinstance(self.sprint_mode, Unset):
            sprint_mode = self.sprint_mode.value

        sprint_replicate_on_rollover = self.sprint_replicate_on_rollover

        sprint_name_fmt = self.sprint_name_fmt

        standup_recurrence: Union[Any, None, Unset]
        if isinstance(self.standup_recurrence, Unset):
            standup_recurrence = UNSET
        else:
            standup_recurrence = self.standup_recurrence

        standup_recurs_next_at: Union[None, Unset, str]
        if isinstance(self.standup_recurs_next_at, Unset):
            standup_recurs_next_at = UNSET
        elif isinstance(self.standup_recurs_next_at, datetime.datetime):
            standup_recurs_next_at = self.standup_recurs_next_at.isoformat()
        else:
            standup_recurs_next_at = self.standup_recurs_next_at

        changelog_recurrence: Union[Any, None, Unset]
        if isinstance(self.changelog_recurrence, Unset):
            changelog_recurrence = UNSET
        else:
            changelog_recurrence = self.changelog_recurrence

        changelog_recurs_next_at: Union[None, Unset, str]
        if isinstance(self.changelog_recurs_next_at, Unset):
            changelog_recurs_next_at = UNSET
        elif isinstance(self.changelog_recurs_next_at, datetime.datetime):
            changelog_recurs_next_at = self.changelog_recurs_next_at.isoformat()
        else:
            changelog_recurs_next_at = self.changelog_recurs_next_at

        rollover_recurrence: Union[Any, None, Unset]
        if isinstance(self.rollover_recurrence, Unset):
            rollover_recurrence = UNSET
        else:
            rollover_recurrence = self.rollover_recurrence

        rollover_recurs_next_at: Union[None, Unset, str]
        if isinstance(self.rollover_recurs_next_at, Unset):
            rollover_recurs_next_at = UNSET
        elif isinstance(self.rollover_recurs_next_at, datetime.datetime):
            rollover_recurs_next_at = self.rollover_recurs_next_at.isoformat()
        else:
            rollover_recurs_next_at = self.rollover_recurs_next_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "order": order,
            }
        )
        if drafter_duid is not UNSET:
            field_dict["drafterDuid"] = drafter_duid
        if accessible_by_team is not UNSET:
            field_dict["accessibleByTeam"] = accessible_by_team
        if accessible_by_user_duids is not UNSET:
            field_dict["accessibleByUserDuids"] = accessible_by_user_duids
        if title is not UNSET:
            field_dict["title"] = title
        if abrev is not UNSET:
            field_dict["abrev"] = abrev
        if description is not UNSET:
            field_dict["description"] = description
        if icon_kind is not UNSET:
            field_dict["iconKind"] = icon_kind
        if icon_name_or_emoji is not UNSET:
            field_dict["iconNameOrEmoji"] = icon_name_or_emoji
        if color_hex is not UNSET:
            field_dict["colorHex"] = color_hex
        if sprint_mode is not UNSET:
            field_dict["sprintMode"] = sprint_mode
        if sprint_replicate_on_rollover is not UNSET:
            field_dict["sprintReplicateOnRollover"] = sprint_replicate_on_rollover
        if sprint_name_fmt is not UNSET:
            field_dict["sprintNameFmt"] = sprint_name_fmt
        if standup_recurrence is not UNSET:
            field_dict["standupRecurrence"] = standup_recurrence
        if standup_recurs_next_at is not UNSET:
            field_dict["standupRecursNextAt"] = standup_recurs_next_at
        if changelog_recurrence is not UNSET:
            field_dict["changelogRecurrence"] = changelog_recurrence
        if changelog_recurs_next_at is not UNSET:
            field_dict["changelogRecursNextAt"] = changelog_recurs_next_at
        if rollover_recurrence is not UNSET:
            field_dict["rolloverRecurrence"] = rollover_recurrence
        if rollover_recurs_next_at is not UNSET:
            field_dict["rolloverRecursNextAt"] = rollover_recurs_next_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        order = d.pop("order")

        def _parse_drafter_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        drafter_duid = _parse_drafter_duid(d.pop("drafterDuid", UNSET))

        accessible_by_team = d.pop("accessibleByTeam", UNSET)

        accessible_by_user_duids = cast(list[str], d.pop("accessibleByUserDuids", UNSET))

        title = d.pop("title", UNSET)

        abrev = d.pop("abrev", UNSET)

        description = d.pop("description", UNSET)

        _icon_kind = d.pop("iconKind", UNSET)
        icon_kind: Union[Unset, IconKind]
        if isinstance(_icon_kind, Unset):
            icon_kind = UNSET
        else:
            icon_kind = IconKind(_icon_kind)

        icon_name_or_emoji = d.pop("iconNameOrEmoji", UNSET)

        color_hex = d.pop("colorHex", UNSET)

        _sprint_mode = d.pop("sprintMode", UNSET)
        sprint_mode: Union[Unset, SprintMode]
        if isinstance(_sprint_mode, Unset):
            sprint_mode = UNSET
        else:
            sprint_mode = SprintMode(_sprint_mode)

        sprint_replicate_on_rollover = d.pop("sprintReplicateOnRollover", UNSET)

        sprint_name_fmt = d.pop("sprintNameFmt", UNSET)

        def _parse_standup_recurrence(data: object) -> Union[Any, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[Any, None, Unset], data)

        standup_recurrence = _parse_standup_recurrence(d.pop("standupRecurrence", UNSET))

        def _parse_standup_recurs_next_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                standup_recurs_next_at_type_0 = isoparse(data)

                return standup_recurs_next_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        standup_recurs_next_at = _parse_standup_recurs_next_at(d.pop("standupRecursNextAt", UNSET))

        def _parse_changelog_recurrence(data: object) -> Union[Any, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[Any, None, Unset], data)

        changelog_recurrence = _parse_changelog_recurrence(d.pop("changelogRecurrence", UNSET))

        def _parse_changelog_recurs_next_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                changelog_recurs_next_at_type_0 = isoparse(data)

                return changelog_recurs_next_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        changelog_recurs_next_at = _parse_changelog_recurs_next_at(d.pop("changelogRecursNextAt", UNSET))

        def _parse_rollover_recurrence(data: object) -> Union[Any, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[Any, None, Unset], data)

        rollover_recurrence = _parse_rollover_recurrence(d.pop("rolloverRecurrence", UNSET))

        def _parse_rollover_recurs_next_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rollover_recurs_next_at_type_0 = isoparse(data)

                return rollover_recurs_next_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        rollover_recurs_next_at = _parse_rollover_recurs_next_at(d.pop("rolloverRecursNextAt", UNSET))

        space_create = cls(
            duid=duid,
            order=order,
            drafter_duid=drafter_duid,
            accessible_by_team=accessible_by_team,
            accessible_by_user_duids=accessible_by_user_duids,
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
        )

        space_create.additional_properties = d
        return space_create

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
