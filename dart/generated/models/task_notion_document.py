import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.task_notion_document_block_children_map_type_0 import TaskNotionDocumentBlockChildrenMapType0
    from ..models.task_notion_document_block_map_type_0 import TaskNotionDocumentBlockMapType0
    from ..models.task_notion_document_page_map_type_0 import TaskNotionDocumentPageMapType0


T = TypeVar("T", bound="TaskNotionDocument")


@_attrs_define
class TaskNotionDocument:
    """
    Attributes:
        page_id (str):
        refreshing (bool):
        exists_and_access_granted (Union[None, bool]):
        last_refresh_at (Union[None, datetime.datetime]):
        page_map (Union['TaskNotionDocumentPageMapType0', None]):
        block_map (Union['TaskNotionDocumentBlockMapType0', None]):
        block_children_map (Union['TaskNotionDocumentBlockChildrenMapType0', None]):
    """

    page_id: str
    refreshing: bool
    exists_and_access_granted: Union[None, bool]
    last_refresh_at: Union[None, datetime.datetime]
    page_map: Union["TaskNotionDocumentPageMapType0", None]
    block_map: Union["TaskNotionDocumentBlockMapType0", None]
    block_children_map: Union["TaskNotionDocumentBlockChildrenMapType0", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.task_notion_document_block_children_map_type_0 import TaskNotionDocumentBlockChildrenMapType0
        from ..models.task_notion_document_block_map_type_0 import TaskNotionDocumentBlockMapType0
        from ..models.task_notion_document_page_map_type_0 import TaskNotionDocumentPageMapType0

        page_id = self.page_id

        refreshing = self.refreshing

        exists_and_access_granted: Union[None, bool]
        exists_and_access_granted = self.exists_and_access_granted

        last_refresh_at: Union[None, str]
        if isinstance(self.last_refresh_at, datetime.datetime):
            last_refresh_at = self.last_refresh_at.isoformat()
        else:
            last_refresh_at = self.last_refresh_at

        page_map: Union[None, dict[str, Any]]
        if isinstance(self.page_map, TaskNotionDocumentPageMapType0):
            page_map = self.page_map.to_dict()
        else:
            page_map = self.page_map

        block_map: Union[None, dict[str, Any]]
        if isinstance(self.block_map, TaskNotionDocumentBlockMapType0):
            block_map = self.block_map.to_dict()
        else:
            block_map = self.block_map

        block_children_map: Union[None, dict[str, Any]]
        if isinstance(self.block_children_map, TaskNotionDocumentBlockChildrenMapType0):
            block_children_map = self.block_children_map.to_dict()
        else:
            block_children_map = self.block_children_map

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.task_notion_document_block_children_map_type_0 import TaskNotionDocumentBlockChildrenMapType0
        from ..models.task_notion_document_block_map_type_0 import TaskNotionDocumentBlockMapType0
        from ..models.task_notion_document_page_map_type_0 import TaskNotionDocumentPageMapType0

        d = src_dict.copy()
        page_id = d.pop("pageId")

        refreshing = d.pop("refreshing")

        def _parse_exists_and_access_granted(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        exists_and_access_granted = _parse_exists_and_access_granted(d.pop("existsAndAccessGranted"))

        def _parse_last_refresh_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_refresh_at_type_0 = isoparse(data)

                return last_refresh_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_refresh_at = _parse_last_refresh_at(d.pop("lastRefreshAt"))

        def _parse_page_map(data: object) -> Union["TaskNotionDocumentPageMapType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                page_map_type_0 = TaskNotionDocumentPageMapType0.from_dict(data)

                return page_map_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TaskNotionDocumentPageMapType0", None], data)

        page_map = _parse_page_map(d.pop("pageMap"))

        def _parse_block_map(data: object) -> Union["TaskNotionDocumentBlockMapType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                block_map_type_0 = TaskNotionDocumentBlockMapType0.from_dict(data)

                return block_map_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TaskNotionDocumentBlockMapType0", None], data)

        block_map = _parse_block_map(d.pop("blockMap"))

        def _parse_block_children_map(data: object) -> Union["TaskNotionDocumentBlockChildrenMapType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                block_children_map_type_0 = TaskNotionDocumentBlockChildrenMapType0.from_dict(data)

                return block_children_map_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TaskNotionDocumentBlockChildrenMapType0", None], data)

        block_children_map = _parse_block_children_map(d.pop("blockChildrenMap"))

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
