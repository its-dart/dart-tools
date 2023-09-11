from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_link_kind import TaskLinkKind

if TYPE_CHECKING:
    from ..models.task_link_adtl import TaskLinkAdtl


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
        adtl (TaskLinkAdtl):
        title (Optional[str]):
        icon_url (Optional[str]):
    """

    duid: str
    order: str
    kind: TaskLinkKind
    url: str
    adtl: "TaskLinkAdtl"
    title: Optional[str]
    icon_url: Optional[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        order = self.order
        kind = self.kind.value

        url = self.url
        adtl = self.adtl.to_dict()

        title = self.title
        icon_url = self.icon_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "order": order,
                "kind": kind,
                "url": url,
                "adtl": adtl,
                "title": title,
                "iconUrl": icon_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.task_link_adtl import TaskLinkAdtl

        d = src_dict.copy()
        duid = d.pop("duid")

        order = d.pop("order")

        kind = TaskLinkKind(d.pop("kind"))

        url = d.pop("url")

        adtl = TaskLinkAdtl.from_dict(d.pop("adtl"))

        title = d.pop("title")

        icon_url = d.pop("iconUrl")

        task_link = cls(
            duid=duid,
            order=order,
            kind=kind,
            url=url,
            adtl=adtl,
            title=title,
            icon_url=icon_url,
        )

        task_link.additional_properties = d
        return task_link

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
