import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommentUpdate")


@_attrs_define
class CommentUpdate:
    """
    Attributes:
        duid (str):
        authored_by_ai (Union[Unset, bool]):
        author_duid (Union[Unset, str]):
        task_duid (Union[Unset, str]):
        root_duid (Union[None, Unset, str]):
        text (Union[Unset, Any]):
        published_at (Union[None, Unset, datetime.datetime]):
    """

    duid: str
    authored_by_ai: Union[Unset, bool] = UNSET
    author_duid: Union[Unset, str] = UNSET
    task_duid: Union[Unset, str] = UNSET
    root_duid: Union[None, Unset, str] = UNSET
    text: Union[Unset, Any] = UNSET
    published_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        authored_by_ai = self.authored_by_ai

        author_duid = self.author_duid

        task_duid = self.task_duid

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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        authored_by_ai = d.pop("authoredByAi", UNSET)

        author_duid = d.pop("authorDuid", UNSET)

        task_duid = d.pop("taskDuid", UNSET)

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
