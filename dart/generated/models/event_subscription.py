from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EventSubscription")


@_attrs_define
class EventSubscription:
    """
    Attributes:
        in_app (bool):
        email (bool):
        slack (bool):
    """

    in_app: bool
    email: bool
    slack: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        in_app = self.in_app

        email = self.email

        slack = self.slack

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inApp": in_app,
                "email": email,
                "slack": slack,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        in_app = d.pop("inApp")

        email = d.pop("email")

        slack = d.pop("slack")

        event_subscription = cls(
            in_app=in_app,
            email=email,
            slack=slack,
        )

        event_subscription.additional_properties = d
        return event_subscription

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
