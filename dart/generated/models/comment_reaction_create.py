from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CommentReactionCreate")


@_attrs_define
class CommentReactionCreate:
    """
    Attributes:
        duid (str):
        author_duid (str):
        comment_duid (str):
        emoji (str):
    """

    duid: str
    author_duid: str
    comment_duid: str
    emoji: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        author_duid = self.author_duid

        comment_duid = self.comment_duid

        emoji = self.emoji

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "authorDuid": author_duid,
                "commentDuid": comment_duid,
                "emoji": emoji,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        author_duid = d.pop("authorDuid")

        comment_duid = d.pop("commentDuid")

        emoji = d.pop("emoji")

        comment_reaction_create = cls(
            duid=duid,
            author_duid=author_duid,
            comment_duid=comment_duid,
            emoji=emoji,
        )

        comment_reaction_create.additional_properties = d
        return comment_reaction_create

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
