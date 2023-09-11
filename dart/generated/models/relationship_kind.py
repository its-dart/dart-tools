from typing import Any, Dict, List, Optional, Type, TypeVar, Union

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
        updated_by_client_duid (Union[Unset, None, str]):
        backward_text (Optional[str]):
    """

    duid: str
    kind: RelationshipKindKind
    directed: bool
    forward_text: str
    backward_text: Optional[str]
    updated_by_client_duid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        kind = self.kind.value

        directed = self.directed
        forward_text = self.forward_text
        updated_by_client_duid = self.updated_by_client_duid
        backward_text = self.backward_text

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        kind = RelationshipKindKind(d.pop("kind"))

        directed = d.pop("directed")

        forward_text = d.pop("forwardText")

        updated_by_client_duid = d.pop("updatedByClientDuid", UNSET)

        backward_text = d.pop("backwardText")

        relationship_kind = cls(
            duid=duid,
            kind=kind,
            directed=directed,
            forward_text=forward_text,
            updated_by_client_duid=updated_by_client_duid,
            backward_text=backward_text,
        )

        relationship_kind.additional_properties = d
        return relationship_kind

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
