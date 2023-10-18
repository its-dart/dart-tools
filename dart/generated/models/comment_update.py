import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment_update_text import CommentUpdateText


T = TypeVar("T", bound="CommentUpdate")


@_attrs_define
class CommentUpdate:
    """
    Attributes:
        duid (str):
        authored_by_ai (Union[Unset, bool]):
        author_duid (Union[Unset, str]):
        task_duid (Union[Unset, str]):
        root_duid (Union[Unset, None, str]):
        text (Union[Unset, CommentUpdateText]):
        published_at (Union[Unset, None, datetime.datetime]):
    """

    duid: str
    authored_by_ai: Union[Unset, bool] = UNSET
    author_duid: Union[Unset, str] = UNSET
    task_duid: Union[Unset, str] = UNSET
    root_duid: Union[Unset, None, str] = UNSET
    text: Union[Unset, "CommentUpdateText"] = UNSET
    published_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        authored_by_ai = self.authored_by_ai
        author_duid = self.author_duid
        task_duid = self.task_duid
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
            }
        )
        if authored_by_ai is not UNSET:
            field_dict["authoredByAi"] = authored_by_ai
        if author_duid is not UNSET:
            field_dict["authorDuid"] = author_duid
        if task_duid is not UNSET:
            field_dict["taskDuid"] = task_duid
        if root_duid is not UNSET:
            field_dict["rootDuid"] = root_duid
        if text is not UNSET:
            field_dict["text"] = text
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.comment_update_text import CommentUpdateText

        d = src_dict.copy()
        duid = d.pop("duid")

        authored_by_ai = d.pop("authoredByAi", UNSET)

        author_duid = d.pop("authorDuid", UNSET)

        task_duid = d.pop("taskDuid", UNSET)

        root_duid = d.pop("rootDuid", UNSET)

        _text = d.pop("text", UNSET)
        text: Union[Unset, CommentUpdateText]
        if isinstance(_text, Unset):
            text = UNSET
        else:
            text = CommentUpdateText.from_dict(_text)

        _published_at = d.pop("publishedAt", UNSET)
        published_at: Union[Unset, None, datetime.datetime]
        if _published_at is None:
            published_at = None
        elif isinstance(_published_at, Unset):
            published_at = UNSET
        else:
            published_at = isoparse(_published_at)

        comment_update = cls(
            duid=duid,
            authored_by_ai=authored_by_ai,
            author_duid=author_duid,
            task_duid=task_duid,
            root_duid=root_duid,
            text=text,
            published_at=published_at,
        )

        comment_update.additional_properties = d
        return comment_update

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
