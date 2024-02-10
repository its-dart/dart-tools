import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event import Event


T = TypeVar("T", bound="Notification")


@_attrs_define
class Notification:
    """
    Attributes:
        duid (str):
        created_at (datetime.datetime):
        user_duid (str):
        event (Event):
        read (bool):
        updated_by_client_duid (Union[Unset, None, str]):
    """

    duid: str
    created_at: datetime.datetime
    user_duid: str
    event: "Event"
    read: bool
    updated_by_client_duid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        created_at = self.created_at.isoformat()

        user_duid = self.user_duid
        event = self.event.to_dict()

        read = self.read
        updated_by_client_duid = self.updated_by_client_duid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "createdAt": created_at,
                "userDuid": user_duid,
                "event": event,
                "read": read,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event import Event

        d = src_dict.copy()
        duid = d.pop("duid")

        created_at = isoparse(d.pop("createdAt"))

        user_duid = d.pop("userDuid")

        event = Event.from_dict(d.pop("event"))

        read = d.pop("read")

        updated_by_client_duid = d.pop("updatedByClientDuid", UNSET)

        notification = cls(
            duid=duid,
            created_at=created_at,
            user_duid=user_duid,
            event=event,
            read=read,
            updated_by_client_duid=updated_by_client_duid,
        )

        notification.additional_properties = d
        return notification

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
