import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.task_notion_document_block_children_map import TaskNotionDocumentBlockChildrenMap
    from ..models.task_notion_document_block_map import TaskNotionDocumentBlockMap
    from ..models.task_notion_document_page_map import TaskNotionDocumentPageMap


T = TypeVar("T", bound="TaskNotionDocument")


@_attrs_define
class TaskNotionDocument:
    """
    Attributes:
        page_id (str):
        refreshing (bool):
        exists_and_access_granted (Optional[bool]):
        last_refresh_at (Optional[datetime.datetime]):
        page_map (Optional[TaskNotionDocumentPageMap]):
        block_map (Optional[TaskNotionDocumentBlockMap]):
        block_children_map (Optional[TaskNotionDocumentBlockChildrenMap]):
    """

    page_id: str
    refreshing: bool
    exists_and_access_granted: Optional[bool]
    last_refresh_at: Optional[datetime.datetime]
    page_map: Optional["TaskNotionDocumentPageMap"]
    block_map: Optional["TaskNotionDocumentBlockMap"]
    block_children_map: Optional["TaskNotionDocumentBlockChildrenMap"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page_id = self.page_id
        refreshing = self.refreshing
        exists_and_access_granted = self.exists_and_access_granted
        last_refresh_at = self.last_refresh_at.isoformat() if self.last_refresh_at else None

        page_map = self.page_map.to_dict() if self.page_map else None

        block_map = self.block_map.to_dict() if self.block_map else None

        block_children_map = self.block_children_map.to_dict() if self.block_children_map else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pageId": page_id,
                "refreshing": refreshing,
                "existsAndAccessGranted": exists_and_access_granted,
                "lastRefreshAt": last_refresh_at,
                "pageMap": page_map,
                "blockMap": block_map,
                "blockChildrenMap": block_children_map,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.task_notion_document_block_children_map import TaskNotionDocumentBlockChildrenMap
        from ..models.task_notion_document_block_map import TaskNotionDocumentBlockMap
        from ..models.task_notion_document_page_map import TaskNotionDocumentPageMap

        d = src_dict.copy()
        page_id = d.pop("pageId")

        refreshing = d.pop("refreshing")

        exists_and_access_granted = d.pop("existsAndAccessGranted")

        _last_refresh_at = d.pop("lastRefreshAt")
        last_refresh_at: Optional[datetime.datetime]
        if _last_refresh_at is None:
            last_refresh_at = None
        else:
            last_refresh_at = isoparse(_last_refresh_at)

        _page_map = d.pop("pageMap")
        page_map: Optional[TaskNotionDocumentPageMap]
        if _page_map is None:
            page_map = None
        else:
            page_map = TaskNotionDocumentPageMap.from_dict(_page_map)

        _block_map = d.pop("blockMap")
        block_map: Optional[TaskNotionDocumentBlockMap]
        if _block_map is None:
            block_map = None
        else:
            block_map = TaskNotionDocumentBlockMap.from_dict(_block_map)

        _block_children_map = d.pop("blockChildrenMap")
        block_children_map: Optional[TaskNotionDocumentBlockChildrenMap]
        if _block_children_map is None:
            block_children_map = None
        else:
            block_children_map = TaskNotionDocumentBlockChildrenMap.from_dict(_block_children_map)

        task_notion_document = cls(
            page_id=page_id,
            refreshing=refreshing,
            exists_and_access_granted=exists_and_access_granted,
            last_refresh_at=last_refresh_at,
            page_map=page_map,
            block_map=block_map,
            block_children_map=block_children_map,
        )

        task_notion_document.additional_properties = d
        return task_notion_document

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
