from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_link_kind import TaskLinkKind

T = TypeVar("T", bound="TaskLink")


@_attrs_define
class TaskLink:
    """
    Attributes:
        duid (str):
        order (str):
        kind (TaskLinkKind): * `Standard` - STANDARD
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
        url (str):
        title (Union[None, str]):
        icon_url (Union[None, str]):
        adtl (Any):
    """

    duid: str
    order: str
    kind: TaskLinkKind
    url: str
    title: Union[None, str]
    icon_url: Union[None, str]
    adtl: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        order = self.order

        kind = self.kind.value

        url = self.url

        title: Union[None, str]
        title = self.title

        icon_url: Union[None, str]
        icon_url = self.icon_url

        adtl = self.adtl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "order": order,
                "kind": kind,
                "url": url,
                "title": title,
                "iconUrl": icon_url,
                "adtl": adtl,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        order = d.pop("order")

        kind = TaskLinkKind(d.pop("kind"))

        url = d.pop("url")

        def _parse_title(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        title = _parse_title(d.pop("title"))

        def _parse_icon_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        icon_url = _parse_icon_url(d.pop("iconUrl"))

        adtl = d.pop("adtl")

        task_link = cls(
            duid=duid,
            order=order,
            kind=kind,
            url=url,
            title=title,
            icon_url=icon_url,
            adtl=adtl,
        )

        task_link.additional_properties = d
        return task_link

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
