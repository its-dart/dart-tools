import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.priority import Priority
from ..models.recommendation_status import RecommendationStatus
from ..models.task_source_type import TaskSourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_update_description import TaskUpdateDescription
    from ..models.task_update_recurrence import TaskUpdateRecurrence


T = TypeVar("T", bound="TaskUpdate")


@_attrs_define
class TaskUpdate:
    """
    Attributes:
        duid (str):
        source_user (Union[Unset, None, str]):
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
            * `AppQuickAdd` - APP_QUICK_ADD
            * `AppBoard` - APP_BOARD
            * `AppSubtask` - APP_SUBTASK
            * `AppRelationship` - APP_RELATIONSHIP
            * `AppEnter` - APP_ENTER
            * `AppReplicate` - APP_REPLICATE
            * `AppPaste` - APP_PASTE
            * `AppRoadmapList` - APP_ROADMAP_LIST
            * `AppRoadmapTimeline` - APP_ROADMAP_TIMELINE Default: TaskSourceType.UNKNOWN.
        drafter_duid (Union[Unset, None, str]):
        in_trash (Union[Unset, bool]):
        recommendation_status (Union[Unset, None, RecommendationStatus]): * `Accepted` - ACCEPTED
            * `Declined` - DECLINED
        dartboard_duid (Union[Unset, str]):
        order (Union[Unset, str]):
        title (Union[Unset, str]):
        description (Union[Unset, TaskUpdateDescription]):
        status_duid (Union[Unset, str]):
        assigned_to_ai (Union[Unset, bool]):
        assignee_duids (Union[Unset, List[str]]):
        subscriber_duids (Union[Unset, List[str]]):
        tag_duids (Union[Unset, List[str]]):
        priority (Union[Unset, None, Priority]): * `Critical` - CRITICAL
            * `High` - HIGH
            * `Medium` - MEDIUM
            * `Low` - LOW
        size (Union[Unset, None, int]):
        start_at (Union[Unset, None, datetime.datetime]):
        due_at (Union[Unset, None, datetime.datetime]):
        remind_at (Union[Unset, None, datetime.datetime]):
        recurrence (Union[Unset, None, TaskUpdateRecurrence]):
        recurrs_next_at (Union[Unset, None, datetime.datetime]):
    """

    duid: str
    source_user: Union[Unset, None, str] = UNSET
    source_type: Union[Unset, TaskSourceType] = TaskSourceType.UNKNOWN
    drafter_duid: Union[Unset, None, str] = UNSET
    in_trash: Union[Unset, bool] = UNSET
    recommendation_status: Union[Unset, None, RecommendationStatus] = UNSET
    dartboard_duid: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, "TaskUpdateDescription"] = UNSET
    status_duid: Union[Unset, str] = UNSET
    assigned_to_ai: Union[Unset, bool] = UNSET
    assignee_duids: Union[Unset, List[str]] = UNSET
    subscriber_duids: Union[Unset, List[str]] = UNSET
    tag_duids: Union[Unset, List[str]] = UNSET
    priority: Union[Unset, None, Priority] = UNSET
    size: Union[Unset, None, int] = UNSET
    start_at: Union[Unset, None, datetime.datetime] = UNSET
    due_at: Union[Unset, None, datetime.datetime] = UNSET
    remind_at: Union[Unset, None, datetime.datetime] = UNSET
    recurrence: Union[Unset, None, "TaskUpdateRecurrence"] = UNSET
    recurrs_next_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        source_user = self.source_user
        source_type: Union[Unset, str] = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type.value

        drafter_duid = self.drafter_duid
        in_trash = self.in_trash
        recommendation_status: Union[Unset, None, str] = UNSET
        if not isinstance(self.recommendation_status, Unset):
            recommendation_status = self.recommendation_status.value if self.recommendation_status else None

        dartboard_duid = self.dartboard_duid
        order = self.order
        title = self.title
        description: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        status_duid = self.status_duid
        assigned_to_ai = self.assigned_to_ai
        assignee_duids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.assignee_duids, Unset):
            assignee_duids = self.assignee_duids

        subscriber_duids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subscriber_duids, Unset):
            subscriber_duids = self.subscriber_duids

        tag_duids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tag_duids, Unset):
            tag_duids = self.tag_duids

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

        recurrence: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.recurrence, Unset):
            recurrence = self.recurrence.to_dict() if self.recurrence else None

        recurrs_next_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.recurrs_next_at, Unset):
            recurrs_next_at = self.recurrs_next_at.isoformat() if self.recurrs_next_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if source_user is not UNSET:
            field_dict["sourceUser"] = source_user
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type
        if drafter_duid is not UNSET:
            field_dict["drafterDuid"] = drafter_duid
        if in_trash is not UNSET:
            field_dict["inTrash"] = in_trash
        if recommendation_status is not UNSET:
            field_dict["recommendationStatus"] = recommendation_status
        if dartboard_duid is not UNSET:
            field_dict["dartboardDuid"] = dartboard_duid
        if order is not UNSET:
            field_dict["order"] = order
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if status_duid is not UNSET:
            field_dict["statusDuid"] = status_duid
        if assigned_to_ai is not UNSET:
            field_dict["assignedToAi"] = assigned_to_ai
        if assignee_duids is not UNSET:
            field_dict["assigneeDuids"] = assignee_duids
        if subscriber_duids is not UNSET:
            field_dict["subscriberDuids"] = subscriber_duids
        if tag_duids is not UNSET:
            field_dict["tagDuids"] = tag_duids
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
        if recurrs_next_at is not UNSET:
            field_dict["recurrsNextAt"] = recurrs_next_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.task_update_description import TaskUpdateDescription
        from ..models.task_update_recurrence import TaskUpdateRecurrence

        d = src_dict.copy()
        duid = d.pop("duid")

        source_user = d.pop("sourceUser", UNSET)

        _source_type = d.pop("sourceType", UNSET)
        source_type: Union[Unset, TaskSourceType]
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = TaskSourceType(_source_type)

        drafter_duid = d.pop("drafterDuid", UNSET)

        in_trash = d.pop("inTrash", UNSET)

        _recommendation_status = d.pop("recommendationStatus", UNSET)
        recommendation_status: Union[Unset, None, RecommendationStatus]
        if _recommendation_status is None:
            recommendation_status = None
        elif isinstance(_recommendation_status, Unset):
            recommendation_status = UNSET
        else:
            recommendation_status = RecommendationStatus(_recommendation_status)

        dartboard_duid = d.pop("dartboardDuid", UNSET)

        order = d.pop("order", UNSET)

        title = d.pop("title", UNSET)

        _description = d.pop("description", UNSET)
        description: Union[Unset, TaskUpdateDescription]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = TaskUpdateDescription.from_dict(_description)

        status_duid = d.pop("statusDuid", UNSET)

        assigned_to_ai = d.pop("assignedToAi", UNSET)

        assignee_duids = cast(List[str], d.pop("assigneeDuids", UNSET))

        subscriber_duids = cast(List[str], d.pop("subscriberDuids", UNSET))

        tag_duids = cast(List[str], d.pop("tagDuids", UNSET))

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

        _recurrence = d.pop("recurrence", UNSET)
        recurrence: Union[Unset, None, TaskUpdateRecurrence]
        if _recurrence is None:
            recurrence = None
        elif isinstance(_recurrence, Unset):
            recurrence = UNSET
        else:
            recurrence = TaskUpdateRecurrence.from_dict(_recurrence)

        _recurrs_next_at = d.pop("recurrsNextAt", UNSET)
        recurrs_next_at: Union[Unset, None, datetime.datetime]
        if _recurrs_next_at is None:
            recurrs_next_at = None
        elif isinstance(_recurrs_next_at, Unset):
            recurrs_next_at = UNSET
        else:
            recurrs_next_at = isoparse(_recurrs_next_at)

        task_update = cls(
            duid=duid,
            source_user=source_user,
            source_type=source_type,
            drafter_duid=drafter_duid,
            in_trash=in_trash,
            recommendation_status=recommendation_status,
            dartboard_duid=dartboard_duid,
            order=order,
            title=title,
            description=description,
            status_duid=status_duid,
            assigned_to_ai=assigned_to_ai,
            assignee_duids=assignee_duids,
            subscriber_duids=subscriber_duids,
            tag_duids=tag_duids,
            priority=priority,
            size=size,
            start_at=start_at,
            due_at=due_at,
            remind_at=remind_at,
            recurrence=recurrence,
            recurrs_next_at=recurrs_next_at,
        )

        task_update.additional_properties = d
        return task_update

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
