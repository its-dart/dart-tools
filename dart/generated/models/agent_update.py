from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentUpdate")


@_attrs_define
class AgentUpdate:
    """
    Attributes:
        duid (str):
        enabled (Union[Unset, bool]):
        name (Union[Unset, str]):
        color_hex (Union[Unset, str]):
        on_assign (Union[Any, None, Unset]):
        on_subscribed_update (Union[Any, None, Unset]):
        on_at (Union[Any, None, Unset]):
    """

    duid: str
    enabled: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    color_hex: Union[Unset, str] = UNSET
    on_assign: Union[Any, None, Unset] = UNSET
    on_subscribed_update: Union[Any, None, Unset] = UNSET
    on_at: Union[Any, None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        enabled = self.enabled

        name = self.name

        color_hex = self.color_hex

        on_assign: Union[Any, None, Unset]
        if isinstance(self.on_assign, Unset):
            on_assign = UNSET
        else:
            on_assign = self.on_assign

        on_subscribed_update: Union[Any, None, Unset]
        if isinstance(self.on_subscribed_update, Unset):
            on_subscribed_update = UNSET
        else:
            on_subscribed_update = self.on_subscribed_update

        on_at: Union[Any, None, Unset]
        if isinstance(self.on_at, Unset):
            on_at = UNSET
        else:
            on_at = self.on_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if name is not UNSET:
            field_dict["name"] = name
        if color_hex is not UNSET:
            field_dict["colorHex"] = color_hex
        if on_assign is not UNSET:
            field_dict["onAssign"] = on_assign
        if on_subscribed_update is not UNSET:
            field_dict["onSubscribedUpdate"] = on_subscribed_update
        if on_at is not UNSET:
            field_dict["onAt"] = on_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duid = d.pop("duid")

        enabled = d.pop("enabled", UNSET)

        name = d.pop("name", UNSET)

        color_hex = d.pop("colorHex", UNSET)

        def _parse_on_assign(data: object) -> Union[Any, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[Any, None, Unset], data)

        on_assign = _parse_on_assign(d.pop("onAssign", UNSET))

        def _parse_on_subscribed_update(data: object) -> Union[Any, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[Any, None, Unset], data)

        on_subscribed_update = _parse_on_subscribed_update(d.pop("onSubscribedUpdate", UNSET))

        def _parse_on_at(data: object) -> Union[Any, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[Any, None, Unset], data)

        on_at = _parse_on_at(d.pop("onAt", UNSET))

        agent_update = cls(
            duid=duid,
            enabled=enabled,
            name=name,
            color_hex=color_hex,
            on_assign=on_assign,
            on_subscribed_update=on_subscribed_update,
            on_at=on_at,
        )

        agent_update.additional_properties = d
        return agent_update

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
