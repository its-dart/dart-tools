from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.relationship_kind_kind import RelationshipKindKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="RelationshipKindCreate")


@_attrs_define
class RelationshipKindCreate:
    """
    Attributes:
        duid (str):
        directed (bool):
        forward_text (str):
        kind (Union[Unset, RelationshipKindKind]): * `Parent Of` - PARENT_OF
            * `Blocks` - BLOCKS
            * `Relates To` - RELATES_TO
            * `Duplicates` - DUPLICATES
            * `Custom` - CUSTOM
        backward_text (Union[Unset, None, str]):
    """

    duid: str
    directed: bool
    forward_text: str
    kind: Union[Unset, RelationshipKindKind] = UNSET
    backward_text: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        directed = self.directed
        forward_text = self.forward_text
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        backward_text = self.backward_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "directed": directed,
                "forwardText": forward_text,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if backward_text is not UNSET:
            field_dict["backwardText"] = backward_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        directed = d.pop("directed")

        forward_text = d.pop("forwardText")

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, RelationshipKindKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = RelationshipKindKind(_kind)

        backward_text = d.pop("backwardText", UNSET)

        relationship_kind_create = cls(
            duid=duid,
            directed=directed,
            forward_text=forward_text,
            kind=kind,
            backward_text=backward_text,
        )

        relationship_kind_create.additional_properties = d
        return relationship_kind_create

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
