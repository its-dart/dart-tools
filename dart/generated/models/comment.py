from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Comment")


@_attrs_define
class Comment:
    """
    Attributes:
        id (str): The ID. This can and should be null on creation and not otherwise.
        permalink (Union[None, str]): The permanent link, which is a URL that can be used to open the comment in Dart.
            This can and should be null on creation and not otherwise.
        task_id (str): The ID of the task that the comment is associated with. This cannot be null.
        author (str): The name or email of the user that authored the comment. This can and should be null on creation
            and not otherwise.
        text (str): The full content of the comment, which can include markdown formatting. This cannot be null.
    """

    id: str
    permalink: Union[None, str]
    task_id: str
    author: str
    text: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        permalink: Union[None, str]
        permalink = self.permalink

        task_id = self.task_id

        author = self.author

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "permalink": permalink,
                "taskId": task_id,
                "author": author,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_permalink(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        permalink = _parse_permalink(d.pop("permalink"))

        task_id = d.pop("taskId")

        author = d.pop("author")

        text = d.pop("text")

        comment = cls(
            id=id,
            permalink=permalink,
            task_id=task_id,
            author=author,
            text=text,
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
