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
    from ..models.task_attachment import TaskAttachment
    from ..models.task_description import TaskDescription
    from ..models.task_link import TaskLink
    from ..models.task_notion_document import TaskNotionDocument


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
        description (TaskDescription):
        status_duid (str):
        assignee_duids (List[str]):
        subscriber_duids (List[str]):
        tag_duids (List[str]):
        links (List['TaskLink']):
        attachments (List['TaskAttachment']):
        relationships (List['Relationship']):
        updated_by_client_duid (Union[Unset, None, str]):
        drafter_duid (Optional[str]):
        recommendation_status (Optional[RecommendationStatus]): * `Accepted` - ACCEPTED
            * `Declined` - DECLINED
        priority (Optional[Priority]): * `Critical` - CRITICAL
            * `High` - HIGH
            * `Medium` - MEDIUM
            * `Low` - LOW
        size (Optional[int]):
        due_at (Optional[datetime.datetime]):
        remind_at (Optional[datetime.datetime]):
        notion_document (Optional[TaskNotionDocument]):
    """

    duid: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    in_trash: bool
    dartboard_duid: str
    order: str
    title: str
    description: "TaskDescription"
    status_duid: str
    assignee_duids: List[str]
    subscriber_duids: List[str]
    tag_duids: List[str]
    links: List["TaskLink"]
    attachments: List["TaskAttachment"]
    relationships: List["Relationship"]
    drafter_duid: Optional[str]
    recommendation_status: Optional[RecommendationStatus]
    priority: Optional[Priority]
    size: Optional[int]
    due_at: Optional[datetime.datetime]
    remind_at: Optional[datetime.datetime]
    notion_document: Optional["TaskNotionDocument"]
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
        description = self.description.to_dict()

        status_duid = self.status_duid
        assignee_duids = self.assignee_duids

        subscriber_duids = self.subscriber_duids

        tag_duids = self.tag_duids

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()

            links.append(links_item)

        attachments = []
        for attachments_item_data in self.attachments:
            attachments_item = attachments_item_data.to_dict()

            attachments.append(attachments_item)

        relationships = []
        for relationships_item_data in self.relationships:
            relationships_item = relationships_item_data.to_dict()

            relationships.append(relationships_item)

        updated_by_client_duid = self.updated_by_client_duid
        drafter_duid = self.drafter_duid
        recommendation_status = self.recommendation_status.value if self.recommendation_status else None

        priority = self.priority.value if self.priority else None

        size = self.size
        due_at = self.due_at.isoformat() if self.due_at else None

        remind_at = self.remind_at.isoformat() if self.remind_at else None

        notion_document = self.notion_document.to_dict() if self.notion_document else None

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
                "assigneeDuids": assignee_duids,
                "subscriberDuids": subscriber_duids,
                "tagDuids": tag_duids,
                "links": links,
                "attachments": attachments,
                "relationships": relationships,
                "drafterDuid": drafter_duid,
                "recommendationStatus": recommendation_status,
                "priority": priority,
                "size": size,
                "dueAt": due_at,
                "remindAt": remind_at,
                "notionDocument": notion_document,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.relationship import Relationship
        from ..models.task_attachment import TaskAttachment
        from ..models.task_description import TaskDescription
        from ..models.task_link import TaskLink
        from ..models.task_notion_document import TaskNotionDocument

        d = src_dict.copy()
        duid = d.pop("duid")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        in_trash = d.pop("inTrash")

        dartboard_duid = d.pop("dartboardDuid")

        order = d.pop("order")

        title = d.pop("title")

        description = TaskDescription.from_dict(d.pop("description"))

        status_duid = d.pop("statusDuid")

        assignee_duids = cast(List[str], d.pop("assigneeDuids"))

        subscriber_duids = cast(List[str], d.pop("subscriberDuids"))

        tag_duids = cast(List[str], d.pop("tagDuids"))

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = TaskLink.from_dict(links_item_data)

            links.append(links_item)

        attachments = []
        _attachments = d.pop("attachments")
        for attachments_item_data in _attachments:
            attachments_item = TaskAttachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        relationships = []
        _relationships = d.pop("relationships")
        for relationships_item_data in _relationships:
            relationships_item = Relationship.from_dict(relationships_item_data)

            relationships.append(relationships_item)

        updated_by_client_duid = d.pop("updatedByClientDuid", UNSET)

        drafter_duid = d.pop("drafterDuid")

        _recommendation_status = d.pop("recommendationStatus")
        recommendation_status: Optional[RecommendationStatus]
        if _recommendation_status is None:
            recommendation_status = None
        else:
            recommendation_status = RecommendationStatus(_recommendation_status)

        _priority = d.pop("priority")
        priority: Optional[Priority]
        if _priority is None:
            priority = None
        else:
            priority = Priority(_priority)

        size = d.pop("size")

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

        _notion_document = d.pop("notionDocument")
        notion_document: Optional[TaskNotionDocument]
        if _notion_document is None:
            notion_document = None
        else:
            notion_document = TaskNotionDocument.from_dict(_notion_document)

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
            assignee_duids=assignee_duids,
            subscriber_duids=subscriber_duids,
            tag_duids=tag_duids,
            links=links,
            attachments=attachments,
            relationships=relationships,
            updated_by_client_duid=updated_by_client_duid,
            drafter_duid=drafter_duid,
            recommendation_status=recommendation_status,
            priority=priority,
            size=size,
            due_at=due_at,
            remind_at=remind_at,
            notion_document=notion_document,
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
