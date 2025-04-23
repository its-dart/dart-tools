from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.doc import Doc


T = TypeVar("T", bound="Folder")


@_attrs_define
class Folder:
    """
    Attributes:
        id (str): The universal, unique ID of the folder.
        html_url (str): The URL that can be used to open the folder in the Dart web UI.
        title (str): The title, which is a short description of the folder.
        description (str): The description, which is a longer description of the folder.
        docs (list['Doc']): The list of all of the docs in the folder.
    """

    id: str
    html_url: str
    title: str
    description: str
    docs: list["Doc"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        html_url = self.html_url

        title = self.title

        description = self.description

        docs = []
        for docs_item_data in self.docs:
            docs_item = docs_item_data.to_dict()
            docs.append(docs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "htmlUrl": html_url,
                "title": title,
                "description": description,
                "docs": docs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.doc import Doc

        d = dict(src_dict)
        id = d.pop("id")

        html_url = d.pop("htmlUrl")

        title = d.pop("title")

        description = d.pop("description")

        docs = []
        _docs = d.pop("docs")
        for docs_item_data in _docs:
            docs_item = Doc.from_dict(docs_item_data)

            docs.append(docs_item)

        folder = cls(
            id=id,
            html_url=html_url,
            title=title,
            description=description,
            docs=docs,
        )

        folder.additional_properties = d
        return folder

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
