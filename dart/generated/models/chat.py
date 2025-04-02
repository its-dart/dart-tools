import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Chat")


@_attrs_define
class Chat:
    """
    Attributes:
        duid (str):
        updated_at (datetime.datetime):
        messages (Any):
        draft (Union[Any, None]):
        updated_by_client_duid (Union[None, Unset, str]):
    """

    duid: str
    updated_at: datetime.datetime
    messages: Any
    draft: Union[Any, None]
    updated_by_client_duid: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        updated_at = self.updated_at.isoformat()

        messages = self.messages

        draft: Union[Any, None]
        draft = self.draft

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
                "updatedAt": updated_at,
                "messages": messages,
                "draft": draft,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duid = d.pop("duid")

        updated_at = isoparse(d.pop("updatedAt"))

        messages = d.pop("messages")

        def _parse_draft(data: object) -> Union[Any, None]:
            if data is None:
                return data
            return cast(Union[Any, None], data)

        draft = _parse_draft(d.pop("draft"))

        def _parse_updated_by_client_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_client_duid = _parse_updated_by_client_duid(d.pop("updatedByClientDuid", UNSET))

        chat = cls(
            duid=duid,
            updated_at=updated_at,
            messages=messages,
            draft=draft,
            updated_by_client_duid=updated_by_client_duid,
        )

        chat.additional_properties = d
        return chat

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
