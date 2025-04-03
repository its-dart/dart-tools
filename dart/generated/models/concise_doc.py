from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConciseDoc")


@_attrs_define
class ConciseDoc:
    """This concise doc serializer is going to be used in docs listing view only.

    Attributes:
        id (str): The ID. This can and should be null on creation and not otherwise.
        permalink (str): The permanent link, which is a URL that can be used to open the doc in Dart. This can and
            should be null on creation and not otherwise.
        title (str): The title, which is a short description of the document. This cannot be null.
        folder (str): The title of the folder, which is a project or list of docs. One common option is Docs, although
            what is possible depends on the workspace. If the folder is ambiguous it may need to include a prefix with the
            name of the space, which is a folder for folders.
    """

    id: str
    permalink: str
    title: str
    folder: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        permalink = self.permalink

        title = self.title

        folder = self.folder

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "permalink": permalink,
                "title": title,
                "folder": folder,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        permalink = d.pop("permalink")

        title = d.pop("title")

        folder = d.pop("folder")

        concise_doc = cls(
            id=id,
            permalink=permalink,
            title=title,
            folder=folder,
        )

        concise_doc.additional_properties = d
        return concise_doc

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
