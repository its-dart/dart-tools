from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.relationship_kind_kind import RelationshipKindKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="RelationshipKind")


@_attrs_define
class RelationshipKind:
    """
    Attributes:
        duid (str):
        kind (RelationshipKindKind): * `Parent Of` - PARENT_OF
            * `Blocks` - BLOCKS
            * `Relates To` - RELATES_TO
            * `Duplicates` - DUPLICATES
            * `Custom` - CUSTOM
        directed (bool):
        forward_text (str):
        backward_text (Union[None, str]):
        updated_by_client_duid (Union[None, Unset, str]):
    """

    duid: str
    kind: RelationshipKindKind
    directed: bool
    forward_text: str
    backward_text: Union[None, str]
    updated_by_client_duid: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        kind = self.kind.value

        directed = self.directed

        forward_text = self.forward_text

        backward_text: Union[None, str]
        backward_text = self.backward_text

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
                "directed": directed,
                "forwardText": forward_text,
                "backwardText": backward_text,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        kind = RelationshipKindKind(d.pop("kind"))

        directed = d.pop("directed")

        forward_text = d.pop("forwardText")

        def _parse_backward_text(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        backward_text = _parse_backward_text(d.pop("backwardText"))

        def _parse_updated_by_client_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_client_duid = _parse_updated_by_client_duid(d.pop("updatedByClientDuid", UNSET))

        relationship_kind = cls(
            duid=duid,
            kind=kind,
            directed=directed,
            forward_text=forward_text,
            backward_text=backward_text,
            updated_by_client_duid=updated_by_client_duid,
        )

        relationship_kind.additional_properties = d
        return relationship_kind

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
