import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="CommentReaction")


@_attrs_define
class CommentReaction:
    """
    Attributes:
        duid (str):
        created_at (datetime.datetime):
        author_duid (str):
        emoji (str):
    """

    duid: str
    created_at: datetime.datetime
    author_duid: str
    emoji: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        created_at = self.created_at.isoformat()

        author_duid = self.author_duid
        emoji = self.emoji

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "createdAt": created_at,
                "authorDuid": author_duid,
                "emoji": emoji,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        created_at = isoparse(d.pop("createdAt"))

        author_duid = d.pop("authorDuid")

        emoji = d.pop("emoji")

        comment_reaction = cls(
            duid=duid,
            created_at=created_at,
            author_duid=author_duid,
            emoji=emoji,
        )

        comment_reaction.additional_properties = d
        return comment_reaction

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
