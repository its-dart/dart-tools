import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommentCreate")


@_attrs_define
class CommentCreate:
    """
    Attributes:
        duid (str):
        author_duid (str):
        task_duid (str):
        authored_by_ai (Union[Unset, bool]):
        root_duid (Union[None, Unset, str]):
        text (Union[Unset, Any]):
        published_at (Union[None, Unset, datetime.datetime]):
    """

    duid: str
    author_duid: str
    task_duid: str
    authored_by_ai: Union[Unset, bool] = UNSET
    root_duid: Union[None, Unset, str] = UNSET
    text: Union[Unset, Any] = UNSET
    published_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        author_duid = self.author_duid

        task_duid = self.task_duid

        authored_by_ai = self.authored_by_ai

        root_duid: Union[None, Unset, str]
        if isinstance(self.root_duid, Unset):
            root_duid = UNSET
        else:
            root_duid = self.root_duid

        text = self.text

        published_at: Union[None, Unset, str]
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        elif isinstance(self.published_at, datetime.datetime):
            published_at = self.published_at.isoformat()
        else:
            published_at = self.published_at

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        author_duid = d.pop("authorDuid")

        task_duid = d.pop("taskDuid")

        authored_by_ai = d.pop("authoredByAi", UNSET)

        def _parse_root_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        root_duid = _parse_root_duid(d.pop("rootDuid", UNSET))

        text = d.pop("text", UNSET)

        def _parse_published_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_at_type_0 = isoparse(data)

                return published_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        published_at = _parse_published_at(d.pop("publishedAt", UNSET))

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
