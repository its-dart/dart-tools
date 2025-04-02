from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_event_kind import WebhookEventKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookUpdate")


@_attrs_define
class WebhookUpdate:
    """
    Attributes:
        duid (str):
        enabled (Union[Unset, bool]):
        order (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
        event_kinds (Union[Unset, WebhookEventKind]): * `task.created` - TASK_CREATED
            * `task.deleted` - TASK_DELETED
            * `task.updated` - TASK_UPDATED
            * `doc.created` - DOC_CREATED
            * `doc.deleted` - DOC_DELETED
            * `doc.updated` - DOC_UPDATED
            * `comment.created` - COMMENT_CREATED
    """

    duid: str
    enabled: Union[Unset, bool] = UNSET
    order: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    event_kinds: Union[Unset, WebhookEventKind] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        enabled = self.enabled

        order = self.order

        title = self.title

        url = self.url

        event_kinds: Union[Unset, str] = UNSET
        if not isinstance(self.event_kinds, Unset):
            event_kinds = self.event_kinds.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if order is not UNSET:
            field_dict["order"] = order
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url
        if event_kinds is not UNSET:
            field_dict["eventKinds"] = event_kinds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duid = d.pop("duid")

        enabled = d.pop("enabled", UNSET)

        order = d.pop("order", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        _event_kinds = d.pop("eventKinds", UNSET)
        event_kinds: Union[Unset, WebhookEventKind]
        if isinstance(_event_kinds, Unset):
            event_kinds = UNSET
        else:
            event_kinds = WebhookEventKind(_event_kinds)

        webhook_update = cls(
            duid=duid,
            enabled=enabled,
            order=order,
            title=title,
            url=url,
            event_kinds=event_kinds,
        )

        webhook_update.additional_properties = d
        return webhook_update

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
