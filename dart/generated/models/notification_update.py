from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event import Event


T = TypeVar("T", bound="NotificationUpdate")


@_attrs_define
class NotificationUpdate:
    """
    Attributes:
        duid (str):
        user_duid (Union[Unset, str]):
        event (Union[Unset, Event]):
        read (Union[Unset, bool]):
    """

    duid: str
    user_duid: Union[Unset, str] = UNSET
    event: Union[Unset, "Event"] = UNSET
    read: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        user_duid = self.user_duid

        event: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.to_dict()

        read = self.read

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if user_duid is not UNSET:
            field_dict["userDuid"] = user_duid
        if event is not UNSET:
            field_dict["event"] = event
        if read is not UNSET:
            field_dict["read"] = read

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.event import Event

        d = src_dict.copy()
        duid = d.pop("duid")

        user_duid = d.pop("userDuid", UNSET)

        _event = d.pop("event", UNSET)
        event: Union[Unset, Event]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = Event.from_dict(_event)

        read = d.pop("read", UNSET)

        notification_update = cls(
            duid=duid,
            user_duid=user_duid,
            event=event,
            read=read,
        )

        notification_update.additional_properties = d
        return notification_update

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
