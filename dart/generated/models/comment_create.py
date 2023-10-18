import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment_create_text import CommentCreateText


T = TypeVar("T", bound="CommentCreate")


@_attrs_define
class CommentCreate:
    """
    Attributes:
        duid (str):
        author_duid (str):
        task_duid (str):
        authored_by_ai (Union[Unset, bool]):
        root_duid (Union[Unset, None, str]):
        text (Union[Unset, CommentCreateText]):
        published_at (Union[Unset, None, datetime.datetime]):
    """

    duid: str
    author_duid: str
    task_duid: str
    authored_by_ai: Union[Unset, bool] = UNSET
    root_duid: Union[Unset, None, str] = UNSET
    text: Union[Unset, "CommentCreateText"] = UNSET
    published_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        author_duid = self.author_duid
        task_duid = self.task_duid
        authored_by_ai = self.authored_by_ai
        root_duid = self.root_duid
        text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.text, Unset):
            text = self.text.to_dict()

        published_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.published_at, Unset):
            published_at = self.published_at.isoformat() if self.published_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "authorDuid": author_duid,
                "taskDuid": task_duid,
            }
        )
        if authored_by_ai is not UNSET:
            field_dict["authoredByAi"] = authored_by_ai
        if root_duid is not UNSET:
            field_dict["rootDuid"] = root_duid
        if text is not UNSET:
            field_dict["text"] = text
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.comment_create_text import CommentCreateText

        d = src_dict.copy()
        duid = d.pop("duid")

        author_duid = d.pop("authorDuid")

        task_duid = d.pop("taskDuid")

        authored_by_ai = d.pop("authoredByAi", UNSET)

        root_duid = d.pop("rootDuid", UNSET)

        _text = d.pop("text", UNSET)
        text: Union[Unset, CommentCreateText]
        if isinstance(_text, Unset):
            text = UNSET
        else:
            text = CommentCreateText.from_dict(_text)

        _published_at = d.pop("publishedAt", UNSET)
        published_at: Union[Unset, None, datetime.datetime]
        if _published_at is None:
            published_at = None
        elif isinstance(_published_at, Unset):
            published_at = UNSET
        else:
            published_at = isoparse(_published_at)

        comment_create = cls(
            duid=duid,
            author_duid=author_duid,
            task_duid=task_duid,
            authored_by_ai=authored_by_ai,
            root_duid=root_duid,
            text=text,
            published_at=published_at,
        )

        comment_create.additional_properties = d
        return comment_create

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
