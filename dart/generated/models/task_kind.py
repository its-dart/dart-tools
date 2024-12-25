from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.icon_kind import IconKind
from ..models.task_kind_kind import TaskKindKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskKind")


@_attrs_define
class TaskKind:
    """
    Attributes:
        duid (str):
        kind (TaskKindKind): * `Default` - DEFAULT
            * `Milestone` - MILESTONE
        locked (bool):
        order (str):
        title (str):
        icon_kind (IconKind): * `None` - NONE
            * `Icon` - ICON
            * `Emoji` - EMOJI
        icon_name_or_emoji (str):
        color_hex (str):
        hidden_status_duids (list[str]):
        updated_by_client_duid (Union[None, Unset, str]):
    """

    duid: str
    kind: TaskKindKind
    locked: bool
    order: str
    title: str
    icon_kind: IconKind
    icon_name_or_emoji: str
    color_hex: str
    hidden_status_duids: list[str]
    updated_by_client_duid: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        kind = self.kind.value

        locked = self.locked

        order = self.order

        title = self.title

        icon_kind = self.icon_kind.value

        icon_name_or_emoji = self.icon_name_or_emoji

        color_hex = self.color_hex

        hidden_status_duids = self.hidden_status_duids

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
                "locked": locked,
                "order": order,
                "title": title,
                "iconKind": icon_kind,
                "iconNameOrEmoji": icon_name_or_emoji,
                "colorHex": color_hex,
                "hiddenStatusDuids": hidden_status_duids,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        kind = TaskKindKind(d.pop("kind"))

        locked = d.pop("locked")

        order = d.pop("order")

        title = d.pop("title")

        icon_kind = IconKind(d.pop("iconKind"))

        icon_name_or_emoji = d.pop("iconNameOrEmoji")

        color_hex = d.pop("colorHex")

        hidden_status_duids = cast(list[str], d.pop("hiddenStatusDuids"))

        def _parse_updated_by_client_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_client_duid = _parse_updated_by_client_duid(d.pop("updatedByClientDuid", UNSET))

        task_kind = cls(
            duid=duid,
            kind=kind,
            locked=locked,
            order=order,
            title=title,
            icon_kind=icon_kind,
            icon_name_or_emoji=icon_name_or_emoji,
            color_hex=color_hex,
            hidden_status_duids=hidden_status_duids,
            updated_by_client_duid=updated_by_client_duid,
        )

        task_kind.additional_properties = d
        return task_kind

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
