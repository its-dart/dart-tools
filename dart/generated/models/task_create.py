import datetime
from typing import Any, TypeVar, Union, cast

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
        source_template_view_duid (Union[None, Unset, str]):
        source_template_task_duid (Union[None, Unset, str]):
        source_form_duid (Union[None, Unset, str]):
        created_by_duid (Union[None, Unset, str]):
        updated_by_duid (Union[None, Unset, str]):
        drafter_duid (Union[None, Unset, str]):
        in_trash (Union[Unset, bool]):
        dartboard_duid (Union[Unset, str]):
        order (Union[Unset, str]):
        expanded (Union[Unset, bool]):
        kind_duid (Union[Unset, str]):
        title (Union[Unset, str]):
        description (Union[Unset, Any]):
        description_markdown (Union[Unset, str]):
        status_duid (Union[Unset, str]):
        assigned_to_ai (Union[Unset, bool]):
        recommendation_duid (Union[None, Unset, str]):
        assignee_duids (Union[Unset, list[str]]):
        subscriber_duids (Union[Unset, list[str]]):
        tag_duids (Union[Unset, list[str]]):
        attachment_duids (Union[Unset, list[str]]):
        priority (Union[None, Priority, Unset]):
        size (Union[None, Unset, int]):
        start_at (Union[None, Unset, datetime.datetime]):
        due_at (Union[None, Unset, datetime.datetime]):
        time_tracking (Union[Unset, Any]):
        remind_at (Union[None, Unset, datetime.datetime]):
        recurrence (Union[Any, None, Unset]):
        recurs_next_at (Union[None, Unset, datetime.datetime]):
        properties (Union[Unset, Any]):
    """

    duid: str
    source_type: Union[Unset, TaskSourceType] = TaskSourceType.UNKNOWN
    source_template_view_duid: Union[None, Unset, str] = UNSET
    source_template_task_duid: Union[None, Unset, str] = UNSET
    source_form_duid: Union[None, Unset, str] = UNSET
    created_by_duid: Union[None, Unset, str] = UNSET
    updated_by_duid: Union[None, Unset, str] = UNSET
    drafter_duid: Union[None, Unset, str] = UNSET
    in_trash: Union[Unset, bool] = UNSET
    dartboard_duid: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    expanded: Union[Unset, bool] = UNSET
    kind_duid: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, Any] = UNSET
    description_markdown: Union[Unset, str] = UNSET
    status_duid: Union[Unset, str] = UNSET
    assigned_to_ai: Union[Unset, bool] = UNSET
    recommendation_duid: Union[None, Unset, str] = UNSET
    assignee_duids: Union[Unset, list[str]] = UNSET
    subscriber_duids: Union[Unset, list[str]] = UNSET
    tag_duids: Union[Unset, list[str]] = UNSET
    attachment_duids: Union[Unset, list[str]] = UNSET
    priority: Union[None, Priority, Unset] = UNSET
    size: Union[None, Unset, int] = UNSET
    start_at: Union[None, Unset, datetime.datetime] = UNSET
    due_at: Union[None, Unset, datetime.datetime] = UNSET
    time_tracking: Union[Unset, Any] = UNSET
    remind_at: Union[None, Unset, datetime.datetime] = UNSET
    recurrence: Union[Any, None, Unset] = UNSET
    recurs_next_at: Union[None, Unset, datetime.datetime] = UNSET
    properties: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        source_type: Union[Unset, str] = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type.value

        source_template_view_duid: Union[None, Unset, str]
        if isinstance(self.source_template_view_duid, Unset):
            source_template_view_duid = UNSET
        else:
            source_template_view_duid = self.source_template_view_duid

        source_template_task_duid: Union[None, Unset, str]
        if isinstance(self.source_template_task_duid, Unset):
            source_template_task_duid = UNSET
        else:
            source_template_task_duid = self.source_template_task_duid

        source_form_duid: Union[None, Unset, str]
        if isinstance(self.source_form_duid, Unset):
            source_form_duid = UNSET
        else:
            source_form_duid = self.source_form_duid

        created_by_duid: Union[None, Unset, str]
        if isinstance(self.created_by_duid, Unset):
            created_by_duid = UNSET
        else:
            created_by_duid = self.created_by_duid

        updated_by_duid: Union[None, Unset, str]
        if isinstance(self.updated_by_duid, Unset):
            updated_by_duid = UNSET
        else:
            updated_by_duid = self.updated_by_duid

        drafter_duid: Union[None, Unset, str]
        if isinstance(self.drafter_duid, Unset):
            drafter_duid = UNSET
        else:
            drafter_duid = self.drafter_duid

        in_trash = self.in_trash

        dartboard_duid = self.dartboard_duid

        order = self.order

        expanded = self.expanded

        kind_duid = self.kind_duid

        title = self.title

        description = self.description

        description_markdown = self.description_markdown

        status_duid = self.status_duid

        assigned_to_ai = self.assigned_to_ai

        recommendation_duid: Union[None, Unset, str]
        if isinstance(self.recommendation_duid, Unset):
            recommendation_duid = UNSET
        else:
            recommendation_duid = self.recommendation_duid

        assignee_duids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.assignee_duids, Unset):
            assignee_duids = self.assignee_duids

        subscriber_duids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.subscriber_duids, Unset):
            subscriber_duids = self.subscriber_duids

        tag_duids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tag_duids, Unset):
            tag_duids = self.tag_duids

        attachment_duids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.attachment_duids, Unset):
            attachment_duids = self.attachment_duids

        priority: Union[None, Unset, str]
        if isinstance(self.priority, Unset):
            priority = UNSET
        elif isinstance(self.priority, Priority):
            priority = self.priority.value
        else:
            priority = self.priority

        size: Union[None, Unset, int]
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        start_at: Union[None, Unset, str]
        if isinstance(self.start_at, Unset):
            start_at = UNSET
        elif isinstance(self.start_at, datetime.datetime):
            start_at = self.start_at.isoformat()
        else:
            start_at = self.start_at

        due_at: Union[None, Unset, str]
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        elif isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        time_tracking = self.time_tracking

        remind_at: Union[None, Unset, str]
        if isinstance(self.remind_at, Unset):
            remind_at = UNSET
        elif isinstance(self.remind_at, datetime.datetime):
            remind_at = self.remind_at.isoformat()
        else:
            remind_at = self.remind_at

        recurrence: Union[Any, None, Unset]
        if isinstance(self.recurrence, Unset):
            recurrence = UNSET
        else:
            recurrence = self.recurrence

        recurs_next_at: Union[None, Unset, str]
        if isinstance(self.recurs_next_at, Unset):
            recurs_next_at = UNSET
        elif isinstance(self.recurs_next_at, datetime.datetime):
            recurs_next_at = self.recurs_next_at.isoformat()
        else:
            recurs_next_at = self.recurs_next_at

        properties = self.properties

        field_dict: dict[str, Any] = {}
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
        if kind_duid is not UNSET:
            field_dict["kindDuid"] = kind_duid
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
        if time_tracking is not UNSET:
            field_dict["timeTracking"] = time_tracking
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        _source_type = d.pop("sourceType", UNSET)
        source_type: Union[Unset, TaskSourceType]
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = TaskSourceType(_source_type)

        def _parse_source_template_view_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_template_view_duid = _parse_source_template_view_duid(d.pop("sourceTemplateViewDuid", UNSET))

        def _parse_source_template_task_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_template_task_duid = _parse_source_template_task_duid(d.pop("sourceTemplateTaskDuid", UNSET))

        def _parse_source_form_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_form_duid = _parse_source_form_duid(d.pop("sourceFormDuid", UNSET))

        def _parse_created_by_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by_duid = _parse_created_by_duid(d.pop("createdByDuid", UNSET))

        def _parse_updated_by_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_duid = _parse_updated_by_duid(d.pop("updatedByDuid", UNSET))

        def _parse_drafter_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        drafter_duid = _parse_drafter_duid(d.pop("drafterDuid", UNSET))

        in_trash = d.pop("inTrash", UNSET)

        dartboard_duid = d.pop("dartboardDuid", UNSET)

        order = d.pop("order", UNSET)

        expanded = d.pop("expanded", UNSET)

        kind_duid = d.pop("kindDuid", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        description_markdown = d.pop("descriptionMarkdown", UNSET)

        status_duid = d.pop("statusDuid", UNSET)

        assigned_to_ai = d.pop("assignedToAi", UNSET)

        def _parse_recommendation_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        recommendation_duid = _parse_recommendation_duid(d.pop("recommendationDuid", UNSET))

        assignee_duids = cast(list[str], d.pop("assigneeDuids", UNSET))

        subscriber_duids = cast(list[str], d.pop("subscriberDuids", UNSET))

        tag_duids = cast(list[str], d.pop("tagDuids", UNSET))

        attachment_duids = cast(list[str], d.pop("attachmentDuids", UNSET))

        def _parse_priority(data: object) -> Union[None, Priority, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_0 = Priority(data)

                return priority_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Priority, Unset], data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size = _parse_size(d.pop("size", UNSET))

        def _parse_start_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_at_type_0 = isoparse(data)

                return start_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        start_at = _parse_start_at(d.pop("startAt", UNSET))

        def _parse_due_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_at_type_0 = isoparse(data)

                return due_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        due_at = _parse_due_at(d.pop("dueAt", UNSET))

        time_tracking = d.pop("timeTracking", UNSET)

        def _parse_remind_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                remind_at_type_0 = isoparse(data)

                return remind_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        remind_at = _parse_remind_at(d.pop("remindAt", UNSET))

        def _parse_recurrence(data: object) -> Union[Any, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[Any, None, Unset], data)

        recurrence = _parse_recurrence(d.pop("recurrence", UNSET))

        def _parse_recurs_next_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recurs_next_at_type_0 = isoparse(data)

                return recurs_next_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        recurs_next_at = _parse_recurs_next_at(d.pop("recursNextAt", UNSET))

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
            kind_duid=kind_duid,
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
            time_tracking=time_tracking,
            remind_at=remind_at,
            recurrence=recurrence,
            recurs_next_at=recurs_next_at,
            properties=properties,
        )

        task_create.additional_properties = d
        return task_create

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
