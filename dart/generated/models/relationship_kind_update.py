from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.relationship_kind_kind import RelationshipKindKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="RelationshipKindUpdate")


@_attrs_define
class RelationshipKindUpdate:
    """
    Attributes:
        duid (str):
        kind (Union[Unset, RelationshipKindKind]): * `Parent Of` - PARENT_OF
            * `Blocks` - BLOCKS
            * `Relates To` - RELATES_TO
            * `Duplicates` - DUPLICATES
            * `Custom` - CUSTOM
        directed (Union[Unset, bool]):
        forward_text (Union[Unset, str]):
        backward_text (Union[None, Unset, str]):
    """

    duid: str
    kind: Union[Unset, RelationshipKindKind] = UNSET
    directed: Union[Unset, bool] = UNSET
    forward_text: Union[Unset, str] = UNSET
    backward_text: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        directed = self.directed

        forward_text = self.forward_text

        backward_text: Union[None, Unset, str]
        if isinstance(self.backward_text, Unset):
            backward_text = UNSET
        else:
            backward_text = self.backward_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if directed is not UNSET:
            field_dict["directed"] = directed
        if forward_text is not UNSET:
            field_dict["forwardText"] = forward_text
        if backward_text is not UNSET:
            field_dict["backwardText"] = backward_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, RelationshipKindKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = RelationshipKindKind(_kind)

        directed = d.pop("directed", UNSET)

        forward_text = d.pop("forwardText", UNSET)

        def _parse_backward_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        backward_text = _parse_backward_text(d.pop("backwardText", UNSET))

        relationship_kind_update = cls(
            duid=duid,
            kind=kind,
            directed=directed,
            forward_text=forward_text,
            backward_text=backward_text,
        )

        relationship_kind_update.additional_properties = d
        return relationship_kind_update

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
