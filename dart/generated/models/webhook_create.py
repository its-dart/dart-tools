from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_event_kind import WebhookEventKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookCreate")


@_attrs_define
class WebhookCreate:
    """
    Attributes:
        duid (str):
        enabled (bool):
        order (str):
        url (str):
        event_kinds (WebhookEventKind): * `task.created` - TASK_CREATED
            * `task.deleted` - TASK_DELETED
            * `task.updated` - TASK_UPDATED
            * `doc.created` - DOC_CREATED
            * `doc.deleted` - DOC_DELETED
            * `doc.updated` - DOC_UPDATED
            * `comment.created` - COMMENT_CREATED
        title (Union[Unset, str]):
    """

    duid: str
    enabled: bool
    order: str
    url: str
    event_kinds: WebhookEventKind
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        enabled = self.enabled

        order = self.order

        url = self.url

        event_kinds = self.event_kinds.value

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "enabled": enabled,
                "order": order,
                "url": url,
                "eventKinds": event_kinds,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duid = d.pop("duid")

        enabled = d.pop("enabled")

        order = d.pop("order")

        url = d.pop("url")

        event_kinds = WebhookEventKind(d.pop("eventKinds"))

        title = d.pop("title", UNSET)

        webhook_create = cls(
            duid=duid,
            enabled=enabled,
            order=order,
            url=url,
            event_kinds=event_kinds,
            title=title,
        )

        webhook_create.additional_properties = d
        return webhook_create

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
