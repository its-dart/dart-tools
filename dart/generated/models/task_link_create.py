from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_link_kind import TaskLinkKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskLinkCreate")


@_attrs_define
class TaskLinkCreate:
    """
    Attributes:
        duid (str):
        task_duid (str):
        order (str):
        url (str):
        kind (Union[Unset, TaskLinkKind]): * `Standard` - STANDARD
            * `Source From Template` - SOURCE_FROM_TEMPLATE
            * `Source From Third Party` - SOURCE_FROM_THIRD_PARTY
            * `GitHub Branch` - GITHUB_BRANCH
            * `GitHub Pull Request` - GITHUB_PULL_REQUEST
            * `GitHub Expansion` - GITHUB_EXPANSION
            * `Notion Link` - NOTION_LINK
            * `Notion Document` - NOTION_DOCUMENT
            * `Notion Document Doesnt Exist` - NOTION_DOCUMENT_DOESNT_EXIST
            * `Notion Document Parse Failed` - NOTION_DOCUMENT_PARSE_FAILED
            * `Notion Expansion` - NOTION_EXPANSION
            * `Slack Expansion` - SLACK_EXPANSION
        title (Union[Unset, None, str]):
        icon_url (Union[Unset, None, str]):
    """

    duid: str
    task_duid: str
    order: str
    url: str
    kind: Union[Unset, TaskLinkKind] = UNSET
    title: Union[Unset, None, str] = UNSET
    icon_url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        task_duid = self.task_duid
        order = self.order
        url = self.url
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        title = self.title
        icon_url = self.icon_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "taskDuid": task_duid,
                "order": order,
                "url": url,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if title is not UNSET:
            field_dict["title"] = title
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        task_duid = d.pop("taskDuid")

        order = d.pop("order")

        url = d.pop("url")

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, TaskLinkKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = TaskLinkKind(_kind)

        title = d.pop("title", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        task_link_create = cls(
            duid=duid,
            task_duid=task_duid,
            order=order,
            url=url,
            kind=kind,
            title=title,
            icon_url=icon_url,
        )

        task_link_create.additional_properties = d
        return task_link_create

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
