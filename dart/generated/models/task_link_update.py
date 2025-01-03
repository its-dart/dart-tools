from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_link_kind import TaskLinkKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskLinkUpdate")


@_attrs_define
class TaskLinkUpdate:
    """
    Attributes:
        duid (str):
        task_duid (Union[Unset, str]):
        order (Union[Unset, str]):
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
        url (Union[Unset, str]):
        title (Union[None, Unset, str]):
        icon_url (Union[None, Unset, str]):
    """

    duid: str
    task_duid: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    kind: Union[Unset, TaskLinkKind] = UNSET
    url: Union[Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    icon_url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        task_duid = self.task_duid

        order = self.order

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        url = self.url

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        icon_url: Union[None, Unset, str]
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if task_duid is not UNSET:
            field_dict["taskDuid"] = task_duid
        if order is not UNSET:
            field_dict["order"] = order
        if kind is not UNSET:
            field_dict["kind"] = kind
        if url is not UNSET:
            field_dict["url"] = url
        if title is not UNSET:
            field_dict["title"] = title
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        task_duid = d.pop("taskDuid", UNSET)

        order = d.pop("order", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, TaskLinkKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = TaskLinkKind(_kind)

        url = d.pop("url", UNSET)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_icon_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        icon_url = _parse_icon_url(d.pop("iconUrl", UNSET))

        task_link_update = cls(
            duid=duid,
            task_duid=task_duid,
            order=order,
            kind=kind,
            url=url,
            title=title,
            icon_url=icon_url,
        )

        task_link_update.additional_properties = d
        return task_link_update

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
