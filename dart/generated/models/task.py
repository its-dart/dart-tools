import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.priority import Priority
from ..models.recommendation_status import RecommendationStatus
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
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        in_trash (bool):
        dartboard_duid (str):
        order (str):
        title (str):
        description (Any):
        status_duid (str):
        assigned_to_ai (bool):
        assignee_duids (List[str]):
        subscriber_duids (List[str]):
        tag_duids (List[str]):
        links (List['TaskLink']):
        attachment_duids (List[str]):
        relationships (List['Relationship']):
        recurrence (Any):
        properties (TaskProperties):
        updated_by_client_duid (Union[Unset, None, str]):
        created_by_duid (Optional[str]):
        updated_by_duid (Optional[str]):
        drafter_duid (Optional[str]):
        recommendation_status (Optional[RecommendationStatus]): * `Accepted` - ACCEPTED
            * `Declined` - DECLINED
        notion_document (Optional[TaskNotionDocument]):
        priority (Optional[Priority]): * `Critical` - CRITICAL
            * `High` - HIGH
            * `Medium` - MEDIUM
            * `Low` - LOW
        size (Optional[int]):
        start_at (Optional[datetime.datetime]):
        due_at (Optional[datetime.datetime]):
        remind_at (Optional[datetime.datetime]):
        recurrs_next_at (Optional[datetime.datetime]):
    """

    duid: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    in_trash: bool
    dartboard_duid: str
    order: str
    title: str
    description: Any
    status_duid: str
    assigned_to_ai: bool
    assignee_duids: List[str]
    subscriber_duids: List[str]
    tag_duids: List[str]
    links: List["TaskLink"]
    attachment_duids: List[str]
    relationships: List["Relationship"]
    recurrence: Any
    properties: "TaskProperties"
    created_by_duid: Optional[str]
    updated_by_duid: Optional[str]
    drafter_duid: Optional[str]
    recommendation_status: Optional[RecommendationStatus]
    notion_document: Optional["TaskNotionDocument"]
    priority: Optional[Priority]
    size: Optional[int]
    start_at: Optional[datetime.datetime]
    due_at: Optional[datetime.datetime]
    remind_at: Optional[datetime.datetime]
    recurrs_next_at: Optional[datetime.datetime]
    updated_by_client_duid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        in_trash = self.in_trash
        dartboard_duid = self.dartboard_duid
        order = self.order
        title = self.title
        description = self.description
        status_duid = self.status_duid
        assigned_to_ai = self.assigned_to_ai
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

        recurrence = self.recurrence
        properties = self.properties.to_dict()

        updated_by_client_duid = self.updated_by_client_duid
        created_by_duid = self.created_by_duid
        updated_by_duid = self.updated_by_duid
        drafter_duid = self.drafter_duid
        recommendation_status = self.recommendation_status.value if self.recommendation_status else None

        notion_document = self.notion_document.to_dict() if self.notion_document else None

        priority = self.priority.value if self.priority else None

        size = self.size
        start_at = self.start_at.isoformat() if self.start_at else None

        due_at = self.due_at.isoformat() if self.due_at else None

        remind_at = self.remind_at.isoformat() if self.remind_at else None

        recurrs_next_at = self.recurrs_next_at.isoformat() if self.recurrs_next_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "inTrash": in_trash,
                "dartboardDuid": dartboard_duid,
                "order": order,
                "title": title,
                "description": description,
                "statusDuid": status_duid,
                "assignedToAi": assigned_to_ai,
                "assigneeDuids": assignee_duids,
                "subscriberDuids": subscriber_duids,
                "tagDuids": tag_duids,
                "links": links,
                "attachmentDuids": attachment_duids,
                "relationships": relationships,
                "recurrence": recurrence,
                "properties": properties,
                "createdByDuid": created_by_duid,
                "updatedByDuid": updated_by_duid,
                "drafterDuid": drafter_duid,
                "recommendationStatus": recommendation_status,
                "notionDocument": notion_document,
                "priority": priority,
                "size": size,
                "startAt": start_at,
                "dueAt": due_at,
                "remindAt": remind_at,
                "recurrsNextAt": recurrs_next_at,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.relationship import Relationship
        from ..models.task_link import TaskLink
        from ..models.task_notion_document import TaskNotionDocument
        from ..models.task_properties import TaskProperties

        d = src_dict.copy()
        duid = d.pop("duid")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        in_trash = d.pop("inTrash")

        dartboard_duid = d.pop("dartboardDuid")

        order = d.pop("order")

        title = d.pop("title")

        description = d.pop("description")

        status_duid = d.pop("statusDuid")

        assigned_to_ai = d.pop("assignedToAi")

        assignee_duids = cast(List[str], d.pop("assigneeDuids"))

        subscriber_duids = cast(List[str], d.pop("subscriberDuids"))

        tag_duids = cast(List[str], d.pop("tagDuids"))

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = TaskLink.from_dict(links_item_data)

            links.append(links_item)

        attachment_duids = cast(List[str], d.pop("attachmentDuids"))

        relationships = []
        _relationships = d.pop("relationships")
        for relationships_item_data in _relationships:
            relationships_item = Relationship.from_dict(relationships_item_data)

            relationships.append(relationships_item)

        recurrence = d.pop("recurrence")

        properties = TaskProperties.from_dict(d.pop("properties"))

        updated_by_client_duid = d.pop("updatedByClientDuid", UNSET)

        created_by_duid = d.pop("createdByDuid")

        updated_by_duid = d.pop("updatedByDuid")

        drafter_duid = d.pop("drafterDuid")

        _recommendation_status = d.pop("recommendationStatus")
        recommendation_status: Optional[RecommendationStatus]
        if _recommendation_status is None:
            recommendation_status = None
        else:
            recommendation_status = RecommendationStatus(_recommendation_status)

        _notion_document = d.pop("notionDocument")
        notion_document: Optional[TaskNotionDocument]
        if _notion_document is None:
            notion_document = None
        else:
            notion_document = TaskNotionDocument.from_dict(_notion_document)

        _priority = d.pop("priority")
        priority: Optional[Priority]
        if _priority is None:
            priority = None
        else:
            priority = Priority(_priority)

        size = d.pop("size")

        _start_at = d.pop("startAt")
        start_at: Optional[datetime.datetime]
        if _start_at is None:
            start_at = None
        else:
            start_at = isoparse(_start_at)

        _due_at = d.pop("dueAt")
        due_at: Optional[datetime.datetime]
        if _due_at is None:
            due_at = None
        else:
            due_at = isoparse(_due_at)

        _remind_at = d.pop("remindAt")
        remind_at: Optional[datetime.datetime]
        if _remind_at is None:
            remind_at = None
        else:
            remind_at = isoparse(_remind_at)

        _recurrs_next_at = d.pop("recurrsNextAt")
        recurrs_next_at: Optional[datetime.datetime]
        if _recurrs_next_at is None:
            recurrs_next_at = None
        else:
            recurrs_next_at = isoparse(_recurrs_next_at)

        task = cls(
            duid=duid,
            created_at=created_at,
            updated_at=updated_at,
            in_trash=in_trash,
            dartboard_duid=dartboard_duid,
            order=order,
            title=title,
            description=description,
            status_duid=status_duid,
            assigned_to_ai=assigned_to_ai,
            assignee_duids=assignee_duids,
            subscriber_duids=subscriber_duids,
            tag_duids=tag_duids,
            links=links,
            attachment_duids=attachment_duids,
            relationships=relationships,
            recurrence=recurrence,
            properties=properties,
            updated_by_client_duid=updated_by_client_duid,
            created_by_duid=created_by_duid,
            updated_by_duid=updated_by_duid,
            drafter_duid=drafter_duid,
            recommendation_status=recommendation_status,
            notion_document=notion_document,
            priority=priority,
            size=size,
            start_at=start_at,
            due_at=due_at,
            remind_at=remind_at,
            recurrs_next_at=recurrs_next_at,
        )

        task.additional_properties = d
        return task

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
