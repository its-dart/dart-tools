import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.priority import Priority
from ..models.task_source_type import TaskSourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.relationship import Relationship
    from ..models.task_link import TaskLink
    from ..models.task_notion_document import TaskNotionDocument
    from ..models.task_properties import TaskProperties


T = TypeVar("T", bound="Task")


@_attrs_define
class Task:
    """
    Attributes:
        duid (str):
        source_type (TaskSourceType): * `Unknown` - UNKNOWN
            * `Import` - IMPORT
            * `Onboarding` - ONBOARDING
            * `Recommendation` - RECOMMENDATION
            * `Recurrence` - RECURRENCE
            * `Template` - TEMPLATE
            * `ChatGPT` - CHAT_GPT
            * `Email` - EMAIL
            * `Slack` - SLACK
            * `API` - API
            * `CLI` - CLI
            * `Application` - APPLICATION
            * `AppTcm` - APP_TCM
            * `AppInternalForm` - APP_INTERNAL_FORM
            * `AppQuickAdd` - APP_QUICK_ADD
            * `AppBoard` - APP_BOARD
            * `AppSubtask` - APP_SUBTASK
            * `AppRelationship` - APP_RELATIONSHIP
            * `AppEnter` - APP_ENTER
            * `AppReplicate` - APP_REPLICATE
            * `AppPaste` - APP_PASTE
            * `AppRoadmapList` - APP_ROADMAP_LIST
            * `AppRoadmapTimeline` - APP_ROADMAP_TIMELINE
            * `ExternalForm` - EXTERNAL_FORM
        created_at (datetime.datetime):
        created_by_duid (Union[None, str]):
        updated_at (datetime.datetime):
        updated_by_duid (Union[None, str]):
        drafter_duid (Union[None, str]):
        in_trash (bool):
        dartboard_duid (str):
        order (str):
        expanded (bool):
        kind_duid (str):
        title (str):
        description (Any):
        notion_document (Union['TaskNotionDocument', None]):
        status_duid (str):
        assigned_to_ai (bool):
        recommendation_duid (Union[None, str]):
        assignee_duids (list[str]):
        subscriber_duids (list[str]):
        tag_duids (list[str]):
        links (list['TaskLink']):
        attachment_duids (list[str]):
        relationships (list['Relationship']):
        priority (Union[None, Priority]):
        size (Union[None, int]):
        start_at (Union[None, datetime.datetime]):
        due_at (Union[None, datetime.datetime]):
        time_tracking (Any):
        remind_at (Union[None, datetime.datetime]):
        recurrence (Union[Any, None]):
        recurs_next_at (Union[None, datetime.datetime]):
        properties (TaskProperties):
        updated_by_client_duid (Union[None, Unset, str]):
    """

    duid: str
    source_type: TaskSourceType
    created_at: datetime.datetime
    created_by_duid: Union[None, str]
    updated_at: datetime.datetime
    updated_by_duid: Union[None, str]
    drafter_duid: Union[None, str]
    in_trash: bool
    dartboard_duid: str
    order: str
    expanded: bool
    kind_duid: str
    title: str
    description: Any
    notion_document: Union["TaskNotionDocument", None]
    status_duid: str
    assigned_to_ai: bool
    recommendation_duid: Union[None, str]
    assignee_duids: list[str]
    subscriber_duids: list[str]
    tag_duids: list[str]
    links: list["TaskLink"]
    attachment_duids: list[str]
    relationships: list["Relationship"]
    priority: Union[None, Priority]
    size: Union[None, int]
    start_at: Union[None, datetime.datetime]
    due_at: Union[None, datetime.datetime]
    time_tracking: Any
    remind_at: Union[None, datetime.datetime]
    recurrence: Union[Any, None]
    recurs_next_at: Union[None, datetime.datetime]
    properties: "TaskProperties"
    updated_by_client_duid: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.task_notion_document import TaskNotionDocument

        duid = self.duid

        source_type = self.source_type.value

        created_at = self.created_at.isoformat()

        created_by_duid: Union[None, str]
        created_by_duid = self.created_by_duid

        updated_at = self.updated_at.isoformat()

        updated_by_duid: Union[None, str]
        updated_by_duid = self.updated_by_duid

        drafter_duid: Union[None, str]
        drafter_duid = self.drafter_duid

        in_trash = self.in_trash

        dartboard_duid = self.dartboard_duid

        order = self.order

        expanded = self.expanded

        kind_duid = self.kind_duid

        title = self.title

        description = self.description

        notion_document: Union[None, dict[str, Any]]
        if isinstance(self.notion_document, TaskNotionDocument):
            notion_document = self.notion_document.to_dict()
        else:
            notion_document = self.notion_document

        status_duid = self.status_duid

        assigned_to_ai = self.assigned_to_ai

        recommendation_duid: Union[None, str]
        recommendation_duid = self.recommendation_duid

        assignee_duids = self.assignee_duids

        subscriber_duids = self.subscriber_duids

        tag_duids = self.tag_duids

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        attachment_duids = self.attachment_duids

        relationships = []
        for relationships_item_data in self.relationships:
            relationships_item = relationships_item_data.to_dict()
            relationships.append(relationships_item)

        priority: Union[None, str]
        if isinstance(self.priority, Priority):
            priority = self.priority.value
        else:
            priority = self.priority

        size: Union[None, int]
        size = self.size

        start_at: Union[None, str]
        if isinstance(self.start_at, datetime.datetime):
            start_at = self.start_at.isoformat()
        else:
            start_at = self.start_at

        due_at: Union[None, str]
        if isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        time_tracking = self.time_tracking

        remind_at: Union[None, str]
        if isinstance(self.remind_at, datetime.datetime):
            remind_at = self.remind_at.isoformat()
        else:
            remind_at = self.remind_at

        recurrence: Union[Any, None]
        recurrence = self.recurrence

        recurs_next_at: Union[None, str]
        if isinstance(self.recurs_next_at, datetime.datetime):
            recurs_next_at = self.recurs_next_at.isoformat()
        else:
            recurs_next_at = self.recurs_next_at

        properties = self.properties.to_dict()

        updated_by_client_duid: Union[None, Unset, str]
        if isinstance(self.updated_by_client_duid, Unset):
            updated_by_client_duid = UNSET
        else:
            updated_by_client_duid = self.updated_by_client_duid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "sourceType": source_type,
                "createdAt": created_at,
                "createdByDuid": created_by_duid,
                "updatedAt": updated_at,
                "updatedByDuid": updated_by_duid,
                "drafterDuid": drafter_duid,
                "inTrash": in_trash,
                "dartboardDuid": dartboard_duid,
                "order": order,
                "expanded": expanded,
                "kindDuid": kind_duid,
                "title": title,
                "description": description,
                "notionDocument": notion_document,
                "statusDuid": status_duid,
                "assignedToAi": assigned_to_ai,
                "recommendationDuid": recommendation_duid,
                "assigneeDuids": assignee_duids,
                "subscriberDuids": subscriber_duids,
                "tagDuids": tag_duids,
                "links": links,
                "attachmentDuids": attachment_duids,
                "relationships": relationships,
                "priority": priority,
                "size": size,
                "startAt": start_at,
                "dueAt": due_at,
                "timeTracking": time_tracking,
                "remindAt": remind_at,
                "recurrence": recurrence,
                "recursNextAt": recurs_next_at,
                "properties": properties,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.relationship import Relationship
        from ..models.task_link import TaskLink
        from ..models.task_notion_document import TaskNotionDocument
        from ..models.task_properties import TaskProperties

        d = src_dict.copy()
        duid = d.pop("duid")

        source_type = TaskSourceType(d.pop("sourceType"))

        created_at = isoparse(d.pop("createdAt"))

        def _parse_created_by_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        created_by_duid = _parse_created_by_duid(d.pop("createdByDuid"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_updated_by_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        updated_by_duid = _parse_updated_by_duid(d.pop("updatedByDuid"))

        def _parse_drafter_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        drafter_duid = _parse_drafter_duid(d.pop("drafterDuid"))

        in_trash = d.pop("inTrash")

        dartboard_duid = d.pop("dartboardDuid")

        order = d.pop("order")

        expanded = d.pop("expanded")

        kind_duid = d.pop("kindDuid")

        title = d.pop("title")

        description = d.pop("description")

        def _parse_notion_document(data: object) -> Union["TaskNotionDocument", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                notion_document_type_0 = TaskNotionDocument.from_dict(data)

                return notion_document_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TaskNotionDocument", None], data)

        notion_document = _parse_notion_document(d.pop("notionDocument"))

        status_duid = d.pop("statusDuid")

        assigned_to_ai = d.pop("assignedToAi")

        def _parse_recommendation_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        recommendation_duid = _parse_recommendation_duid(d.pop("recommendationDuid"))

        assignee_duids = cast(list[str], d.pop("assigneeDuids"))

        subscriber_duids = cast(list[str], d.pop("subscriberDuids"))

        tag_duids = cast(list[str], d.pop("tagDuids"))

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = TaskLink.from_dict(links_item_data)

            links.append(links_item)

        attachment_duids = cast(list[str], d.pop("attachmentDuids"))

        relationships = []
        _relationships = d.pop("relationships")
        for relationships_item_data in _relationships:
            relationships_item = Relationship.from_dict(relationships_item_data)

            relationships.append(relationships_item)

        def _parse_priority(data: object) -> Union[None, Priority]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_0 = Priority(data)

                return priority_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Priority], data)

        priority = _parse_priority(d.pop("priority"))

        def _parse_size(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        size = _parse_size(d.pop("size"))

        def _parse_start_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_at_type_0 = isoparse(data)

                return start_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        start_at = _parse_start_at(d.pop("startAt"))

        def _parse_due_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_at_type_0 = isoparse(data)

                return due_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        due_at = _parse_due_at(d.pop("dueAt"))

        time_tracking = d.pop("timeTracking")

        def _parse_remind_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                remind_at_type_0 = isoparse(data)

                return remind_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        remind_at = _parse_remind_at(d.pop("remindAt"))

        def _parse_recurrence(data: object) -> Union[Any, None]:
            if data is None:
                return data
            return cast(Union[Any, None], data)

        recurrence = _parse_recurrence(d.pop("recurrence"))

        def _parse_recurs_next_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recurs_next_at_type_0 = isoparse(data)

                return recurs_next_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        recurs_next_at = _parse_recurs_next_at(d.pop("recursNextAt"))

        properties = TaskProperties.from_dict(d.pop("properties"))

        def _parse_updated_by_client_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_client_duid = _parse_updated_by_client_duid(d.pop("updatedByClientDuid", UNSET))

        task = cls(
            duid=duid,
            source_type=source_type,
            created_at=created_at,
            created_by_duid=created_by_duid,
            updated_at=updated_at,
            updated_by_duid=updated_by_duid,
            drafter_duid=drafter_duid,
            in_trash=in_trash,
            dartboard_duid=dartboard_duid,
            order=order,
            expanded=expanded,
            kind_duid=kind_duid,
            title=title,
            description=description,
            notion_document=notion_document,
            status_duid=status_duid,
            assigned_to_ai=assigned_to_ai,
            recommendation_duid=recommendation_duid,
            assignee_duids=assignee_duids,
            subscriber_duids=subscriber_duids,
            tag_duids=tag_duids,
            links=links,
            attachment_duids=attachment_duids,
            relationships=relationships,
            priority=priority,
            size=size,
            start_at=start_at,
            due_at=due_at,
            time_tracking=time_tracking,
            remind_at=remind_at,
            recurrence=recurrence,
            recurs_next_at=recurs_next_at,
            properties=properties,
            updated_by_client_duid=updated_by_client_duid,
        )

        task.additional_properties = d
        return task

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
