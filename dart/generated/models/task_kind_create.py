from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.icon_kind import IconKind
from ..models.task_kind_kind import TaskKindKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskKindCreate")


@_attrs_define
class TaskKindCreate:
    """
    Attributes:
        duid (str):
        kind (TaskKindKind): * `Default` - DEFAULT
            * `Milestone` - MILESTONE
        order (str):
        locked (Union[Unset, bool]):
        title (Union[Unset, str]):
        icon_kind (Union[Unset, IconKind]): * `None` - NONE
            * `Icon` - ICON
            * `Emoji` - EMOJI
        icon_name_or_emoji (Union[Unset, str]):
        color_hex (Union[Unset, str]):
        hidden_status_duids (Union[Unset, list[str]]):
    """

    duid: str
    kind: TaskKindKind
    order: str
    locked: Union[Unset, bool] = UNSET
    title: Union[Unset, str] = UNSET
    icon_kind: Union[Unset, IconKind] = UNSET
    icon_name_or_emoji: Union[Unset, str] = UNSET
    color_hex: Union[Unset, str] = UNSET
    hidden_status_duids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        kind = self.kind.value

        order = self.order

        locked = self.locked

        title = self.title

        icon_kind: Union[Unset, str] = UNSET
        if not isinstance(self.icon_kind, Unset):
            icon_kind = self.icon_kind.value

        icon_name_or_emoji = self.icon_name_or_emoji

        color_hex = self.color_hex

        hidden_status_duids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.hidden_status_duids, Unset):
            hidden_status_duids = self.hidden_status_duids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "kind": kind,
                "order": order,
            }
        )
        if locked is not UNSET:
            field_dict["locked"] = locked
        if title is not UNSET:
            field_dict["title"] = title
        if icon_kind is not UNSET:
            field_dict["iconKind"] = icon_kind
        if icon_name_or_emoji is not UNSET:
            field_dict["iconNameOrEmoji"] = icon_name_or_emoji
        if color_hex is not UNSET:
            field_dict["colorHex"] = color_hex
        if hidden_status_duids is not UNSET:
            field_dict["hiddenStatusDuids"] = hidden_status_duids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        kind = TaskKindKind(d.pop("kind"))

        order = d.pop("order")

        locked = d.pop("locked", UNSET)

        title = d.pop("title", UNSET)

        _icon_kind = d.pop("iconKind", UNSET)
        icon_kind: Union[Unset, IconKind]
        if isinstance(_icon_kind, Unset):
            icon_kind = UNSET
        else:
            icon_kind = IconKind(_icon_kind)

        icon_name_or_emoji = d.pop("iconNameOrEmoji", UNSET)

        color_hex = d.pop("colorHex", UNSET)

        hidden_status_duids = cast(list[str], d.pop("hiddenStatusDuids", UNSET))

        task_kind_create = cls(
            duid=duid,
            kind=kind,
            order=order,
            locked=locked,
            title=title,
            icon_kind=icon_kind,
            icon_name_or_emoji=icon_name_or_emoji,
            color_hex=color_hex,
            hidden_status_duids=hidden_status_duids,
        )

        task_kind_create.additional_properties = d
        return task_kind_create

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
