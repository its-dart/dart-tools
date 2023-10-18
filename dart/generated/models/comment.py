import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment_reaction import CommentReaction
    from ..models.comment_text import CommentText


T = TypeVar("T", bound="Comment")


@_attrs_define
class Comment:
    """
    Attributes:
        duid (str):
        updated_at (datetime.datetime):
        task_duid (str):
        authored_by_ai (bool):
        author_duid (str):
        text (CommentText):
        reactions (List['CommentReaction']):
        is_draft (bool):
        edited (bool):
        updated_by_client_duid (Union[Unset, None, str]):
        root_duid (Optional[str]):
        published_at (Optional[datetime.datetime]):
    """

    duid: str
    updated_at: datetime.datetime
    task_duid: str
    authored_by_ai: bool
    author_duid: str
    text: "CommentText"
    reactions: List["CommentReaction"]
    is_draft: bool
    edited: bool
    root_duid: Optional[str]
    published_at: Optional[datetime.datetime]
    updated_by_client_duid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        updated_at = self.updated_at.isoformat()

        task_duid = self.task_duid
        authored_by_ai = self.authored_by_ai
        author_duid = self.author_duid
        text = self.text.to_dict()

        reactions = []
        for reactions_item_data in self.reactions:
            reactions_item = reactions_item_data.to_dict()

            reactions.append(reactions_item)

        is_draft = self.is_draft
        edited = self.edited
        updated_by_client_duid = self.updated_by_client_duid
        root_duid = self.root_duid
        published_at = self.published_at.isoformat() if self.published_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "updatedAt": updated_at,
                "taskDuid": task_duid,
                "authoredByAi": authored_by_ai,
                "authorDuid": author_duid,
                "text": text,
                "reactions": reactions,
                "isDraft": is_draft,
                "edited": edited,
                "rootDuid": root_duid,
                "publishedAt": published_at,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.comment_reaction import CommentReaction
        from ..models.comment_text import CommentText

        d = src_dict.copy()
        duid = d.pop("duid")

        updated_at = isoparse(d.pop("updatedAt"))

        task_duid = d.pop("taskDuid")

        authored_by_ai = d.pop("authoredByAi")

        author_duid = d.pop("authorDuid")

        text = CommentText.from_dict(d.pop("text"))

        reactions = []
        _reactions = d.pop("reactions")
        for reactions_item_data in _reactions:
            reactions_item = CommentReaction.from_dict(reactions_item_data)

            reactions.append(reactions_item)

        is_draft = d.pop("isDraft")

        edited = d.pop("edited")

        updated_by_client_duid = d.pop("updatedByClientDuid", UNSET)

        root_duid = d.pop("rootDuid")

        _published_at = d.pop("publishedAt")
        published_at: Optional[datetime.datetime]
        if _published_at is None:
            published_at = None
        else:
            published_at = isoparse(_published_at)

        comment = cls(
            duid=duid,
            updated_at=updated_at,
            task_duid=task_duid,
            authored_by_ai=authored_by_ai,
            author_duid=author_duid,
            text=text,
            reactions=reactions,
            is_draft=is_draft,
            edited=edited,
            updated_by_client_duid=updated_by_client_duid,
            root_duid=root_duid,
            published_at=published_at,
        )

        comment.additional_properties = d
        return comment

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
