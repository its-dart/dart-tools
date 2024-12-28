import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment_reaction import CommentReaction


T = TypeVar("T", bound="Comment")


@_attrs_define
class Comment:
    """
    Attributes:
        duid (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        task_duid (str):
        root_duid (Union[None, str]):
        authored_by_ai (bool):
        author_duid (str):
        text (Any):
        published_at (Union[None, datetime.datetime]):
        reactions (list['CommentReaction']):
        is_draft (bool):
        edited (bool):
        updated_by_client_duid (Union[None, Unset, str]):
    """

    duid: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    task_duid: str
    root_duid: Union[None, str]
    authored_by_ai: bool
    author_duid: str
    text: Any
    published_at: Union[None, datetime.datetime]
    reactions: list["CommentReaction"]
    is_draft: bool
    edited: bool
    updated_by_client_duid: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        task_duid = self.task_duid

        root_duid: Union[None, str]
        root_duid = self.root_duid

        authored_by_ai = self.authored_by_ai

        author_duid = self.author_duid

        text = self.text

        published_at: Union[None, str]
        if isinstance(self.published_at, datetime.datetime):
            published_at = self.published_at.isoformat()
        else:
            published_at = self.published_at

        reactions = []
        for reactions_item_data in self.reactions:
            reactions_item = reactions_item_data.to_dict()
            reactions.append(reactions_item)

        is_draft = self.is_draft

        edited = self.edited

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
                "createdAt": created_at,
                "updatedAt": updated_at,
                "taskDuid": task_duid,
                "rootDuid": root_duid,
                "authoredByAi": authored_by_ai,
                "authorDuid": author_duid,
                "text": text,
                "publishedAt": published_at,
                "reactions": reactions,
                "isDraft": is_draft,
                "edited": edited,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.comment_reaction import CommentReaction

        d = src_dict.copy()
        duid = d.pop("duid")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        task_duid = d.pop("taskDuid")

        def _parse_root_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        root_duid = _parse_root_duid(d.pop("rootDuid"))

        authored_by_ai = d.pop("authoredByAi")

        author_duid = d.pop("authorDuid")

        text = d.pop("text")

        def _parse_published_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_at_type_0 = isoparse(data)

                return published_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        published_at = _parse_published_at(d.pop("publishedAt"))

        reactions = []
        _reactions = d.pop("reactions")
        for reactions_item_data in _reactions:
            reactions_item = CommentReaction.from_dict(reactions_item_data)

            reactions.append(reactions_item)

        is_draft = d.pop("isDraft")

        edited = d.pop("edited")

        def _parse_updated_by_client_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_client_duid = _parse_updated_by_client_duid(d.pop("updatedByClientDuid", UNSET))

        comment = cls(
            duid=duid,
            created_at=created_at,
            updated_at=updated_at,
            task_duid=task_duid,
            root_duid=root_duid,
            authored_by_ai=authored_by_ai,
            author_duid=author_duid,
            text=text,
            published_at=published_at,
            reactions=reactions,
            is_draft=is_draft,
            edited=edited,
            updated_by_client_duid=updated_by_client_duid,
        )

        comment.additional_properties = d
        return comment

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
