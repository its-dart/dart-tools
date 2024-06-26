import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.priority import Priority
from ..models.task_source_type import TaskSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskCreate")


@_attrs_define
class TaskCreate:
    """
    Attributes:
        duid (str):
        source_type (Union[Unset, TaskSourceType]): * `Unknown` - UNKNOWN
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
            * `ExternalForm` - EXTERNAL_FORM Default: TaskSourceType.UNKNOWN.
        source_template_view_duid (Union[Unset, None, str]):
        source_template_task_duid (Union[Unset, None, str]):
        source_form_duid (Union[Unset, None, str]):
        created_by_duid (Union[Unset, None, str]):
        updated_by_duid (Union[Unset, None, str]):
        drafter_duid (Union[Unset, None, str]):
        in_trash (Union[Unset, bool]):
        dartboard_duid (Union[Unset, str]):
        order (Union[Unset, str]):
        expanded (Union[Unset, bool]):
        title (Union[Unset, str]):
        description (Union[Unset, Any]):
        description_markdown (Union[Unset, str]):
        status_duid (Union[Unset, str]):
        assigned_to_ai (Union[Unset, bool]):
        recommendation_duid (Union[Unset, None, str]):
        assignee_duids (Union[Unset, List[str]]):
        subscriber_duids (Union[Unset, List[str]]):
        tag_duids (Union[Unset, List[str]]):
        attachment_duids (Union[Unset, List[str]]):
        priority (Union[Unset, None, Priority]): * `Critical` - CRITICAL
            * `High` - HIGH
            * `Medium` - MEDIUM
            * `Low` - LOW
        size (Union[Unset, None, int]):
        start_at (Union[Unset, None, datetime.datetime]):
        due_at (Union[Unset, None, datetime.datetime]):
        remind_at (Union[Unset, None, datetime.datetime]):
        recurrence (Union[Unset, Any]):
        recurs_next_at (Union[Unset, None, datetime.datetime]):
        properties (Union[Unset, Any]):
    """

    duid: str
    source_type: Union[Unset, TaskSourceType] = TaskSourceType.UNKNOWN
    source_template_view_duid: Union[Unset, None, str] = UNSET
    source_template_task_duid: Union[Unset, None, str] = UNSET
    source_form_duid: Union[Unset, None, str] = UNSET
    created_by_duid: Union[Unset, None, str] = UNSET
    updated_by_duid: Union[Unset, None, str] = UNSET
    drafter_duid: Union[Unset, None, str] = UNSET
    in_trash: Union[Unset, bool] = UNSET
    dartboard_duid: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    expanded: Union[Unset, bool] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, Any] = UNSET
    description_markdown: Union[Unset, str] = UNSET
    status_duid: Union[Unset, str] = UNSET
    assigned_to_ai: Union[Unset, bool] = UNSET
    recommendation_duid: Union[Unset, None, str] = UNSET
    assignee_duids: Union[Unset, List[str]] = UNSET
    subscriber_duids: Union[Unset, List[str]] = UNSET
    tag_duids: Union[Unset, List[str]] = UNSET
    attachment_duids: Union[Unset, List[str]] = UNSET
    priority: Union[Unset, None, Priority] = UNSET
    size: Union[Unset, None, int] = UNSET
    start_at: Union[Unset, None, datetime.datetime] = UNSET
    due_at: Union[Unset, None, datetime.datetime] = UNSET
    remind_at: Union[Unset, None, datetime.datetime] = UNSET
    recurrence: Union[Unset, Any] = UNSET
    recurs_next_at: Union[Unset, None, datetime.datetime] = UNSET
    properties: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        source_type: Union[Unset, str] = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type.value

        source_template_view_duid = self.source_template_view_duid
        source_template_task_duid = self.source_template_task_duid
        source_form_duid = self.source_form_duid
        created_by_duid = self.created_by_duid
        updated_by_duid = self.updated_by_duid
        drafter_duid = self.drafter_duid
        in_trash = self.in_trash
        dartboard_duid = self.dartboard_duid
        order = self.order
        expanded = self.expanded
        title = self.title
        description = self.description
        description_markdown = self.description_markdown
        status_duid = self.status_duid
        assigned_to_ai = self.assigned_to_ai
        recommendation_duid = self.recommendation_duid
        assignee_duids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.assignee_duids, Unset):
            assignee_duids = self.assignee_duids

        subscriber_duids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subscriber_duids, Unset):
            subscriber_duids = self.subscriber_duids

        tag_duids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tag_duids, Unset):
            tag_duids = self.tag_duids

        attachment_duids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attachment_duids, Unset):
            attachment_duids = self.attachment_duids

        priority: Union[Unset, None, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value if self.priority else None

        size = self.size
        start_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_at, Unset):
            start_at = self.start_at.isoformat() if self.start_at else None

        due_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.due_at, Unset):
            due_at = self.due_at.isoformat() if self.due_at else None

        remind_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.remind_at, Unset):
            remind_at = self.remind_at.isoformat() if self.remind_at else None

        recurrence = self.recurrence
        recurs_next_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.recurs_next_at, Unset):
            recurs_next_at = self.recurs_next_at.isoformat() if self.recurs_next_at else None

        properties = self.properties

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type
        if source_template_view_duid is not UNSET:
            field_dict["sourceTemplateViewDuid"] = source_template_view_duid
        if source_template_task_duid is not UNSET:
            field_dict["sourceTemplateTaskDuid"] = source_template_task_duid
        if source_form_duid is not UNSET:
            field_dict["sourceFormDuid"] = source_form_duid
        if created_by_duid is not UNSET:
            field_dict["createdByDuid"] = created_by_duid
        if updated_by_duid is not UNSET:
            field_dict["updatedByDuid"] = updated_by_duid
        if drafter_duid is not UNSET:
            field_dict["drafterDuid"] = drafter_duid
        if in_trash is not UNSET:
            field_dict["inTrash"] = in_trash
        if dartboard_duid is not UNSET:
            field_dict["dartboardDuid"] = dartboard_duid
        if order is not UNSET:
            field_dict["order"] = order
        if expanded is not UNSET:
            field_dict["expanded"] = expanded
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if description_markdown is not UNSET:
            field_dict["descriptionMarkdown"] = description_markdown
        if status_duid is not UNSET:
            field_dict["statusDuid"] = status_duid
        if assigned_to_ai is not UNSET:
            field_dict["assignedToAi"] = assigned_to_ai
        if recommendation_duid is not UNSET:
            field_dict["recommendationDuid"] = recommendation_duid
        if assignee_duids is not UNSET:
            field_dict["assigneeDuids"] = assignee_duids
        if subscriber_duids is not UNSET:
            field_dict["subscriberDuids"] = subscriber_duids
        if tag_duids is not UNSET:
            field_dict["tagDuids"] = tag_duids
        if attachment_duids is not UNSET:
            field_dict["attachmentDuids"] = attachment_duids
        if priority is not UNSET:
            field_dict["priority"] = priority
        if size is not UNSET:
            field_dict["size"] = size
        if start_at is not UNSET:
            field_dict["startAt"] = start_at
        if due_at is not UNSET:
            field_dict["dueAt"] = due_at
        if remind_at is not UNSET:
            field_dict["remindAt"] = remind_at
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence
        if recurs_next_at is not UNSET:
            field_dict["recursNextAt"] = recurs_next_at
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        _source_type = d.pop("sourceType", UNSET)
        source_type: Union[Unset, TaskSourceType]
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = TaskSourceType(_source_type)

        source_template_view_duid = d.pop("sourceTemplateViewDuid", UNSET)

        source_template_task_duid = d.pop("sourceTemplateTaskDuid", UNSET)

        source_form_duid = d.pop("sourceFormDuid", UNSET)

        created_by_duid = d.pop("createdByDuid", UNSET)

        updated_by_duid = d.pop("updatedByDuid", UNSET)

        drafter_duid = d.pop("drafterDuid", UNSET)

        in_trash = d.pop("inTrash", UNSET)

        dartboard_duid = d.pop("dartboardDuid", UNSET)

        order = d.pop("order", UNSET)

        expanded = d.pop("expanded", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        description_markdown = d.pop("descriptionMarkdown", UNSET)

        status_duid = d.pop("statusDuid", UNSET)

        assigned_to_ai = d.pop("assignedToAi", UNSET)

        recommendation_duid = d.pop("recommendationDuid", UNSET)

        assignee_duids = cast(List[str], d.pop("assigneeDuids", UNSET))

        subscriber_duids = cast(List[str], d.pop("subscriberDuids", UNSET))

        tag_duids = cast(List[str], d.pop("tagDuids", UNSET))

        attachment_duids = cast(List[str], d.pop("attachmentDuids", UNSET))

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, None, Priority]
        if _priority is None:
            priority = None
        elif isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = Priority(_priority)

        size = d.pop("size", UNSET)

        _start_at = d.pop("startAt", UNSET)
        start_at: Union[Unset, None, datetime.datetime]
        if _start_at is None:
            start_at = None
        elif isinstance(_start_at, Unset):
            start_at = UNSET
        else:
            start_at = isoparse(_start_at)

        _due_at = d.pop("dueAt", UNSET)
        due_at: Union[Unset, None, datetime.datetime]
        if _due_at is None:
            due_at = None
        elif isinstance(_due_at, Unset):
            due_at = UNSET
        else:
            due_at = isoparse(_due_at)

        _remind_at = d.pop("remindAt", UNSET)
        remind_at: Union[Unset, None, datetime.datetime]
        if _remind_at is None:
            remind_at = None
        elif isinstance(_remind_at, Unset):
            remind_at = UNSET
        else:
            remind_at = isoparse(_remind_at)

        recurrence = d.pop("recurrence", UNSET)

        _recurs_next_at = d.pop("recursNextAt", UNSET)
        recurs_next_at: Union[Unset, None, datetime.datetime]
        if _recurs_next_at is None:
            recurs_next_at = None
        elif isinstance(_recurs_next_at, Unset):
            recurs_next_at = UNSET
        else:
            recurs_next_at = isoparse(_recurs_next_at)

        properties = d.pop("properties", UNSET)

        task_create = cls(
            duid=duid,
            source_type=source_type,
            source_template_view_duid=source_template_view_duid,
            source_template_task_duid=source_template_task_duid,
            source_form_duid=source_form_duid,
            created_by_duid=created_by_duid,
            updated_by_duid=updated_by_duid,
            drafter_duid=drafter_duid,
            in_trash=in_trash,
            dartboard_duid=dartboard_duid,
            order=order,
            expanded=expanded,
            title=title,
            description=description,
            description_markdown=description_markdown,
            status_duid=status_duid,
            assigned_to_ai=assigned_to_ai,
            recommendation_duid=recommendation_duid,
            assignee_duids=assignee_duids,
            subscriber_duids=subscriber_duids,
            tag_duids=tag_duids,
            attachment_duids=attachment_duids,
            priority=priority,
            size=size,
            start_at=start_at,
            due_at=due_at,
            remind_at=remind_at,
            recurrence=recurrence,
            recurs_next_at=recurs_next_at,
            properties=properties,
        )

        task_create.additional_properties = d
        return task_create

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
