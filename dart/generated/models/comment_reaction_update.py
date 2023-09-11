from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommentReactionUpdate")


@_attrs_define
class CommentReactionUpdate:
    """
    Attributes:
        duid (str):
        author_duid (Union[Unset, str]):
        comment_duid (Union[Unset, str]):
        emoji (Union[Unset, str]):
    """

    duid: str
    author_duid: Union[Unset, str] = UNSET
    comment_duid: Union[Unset, str] = UNSET
    emoji: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        author_duid = self.author_duid
        comment_duid = self.comment_duid
        emoji = self.emoji

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if author_duid is not UNSET:
            field_dict["authorDuid"] = author_duid
        if comment_duid is not UNSET:
            field_dict["commentDuid"] = comment_duid
        if emoji is not UNSET:
            field_dict["emoji"] = emoji

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        author_duid = d.pop("authorDuid", UNSET)

        comment_duid = d.pop("commentDuid", UNSET)

        emoji = d.pop("emoji", UNSET)

        comment_reaction_update = cls(
            duid=duid,
            author_duid=author_duid,
            comment_duid=comment_duid,
            emoji=emoji,
        )

        comment_reaction_update.additional_properties = d
        return comment_reaction_update

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
