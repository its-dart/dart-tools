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
    from ..models.task_create_description import TaskCreateDescription


T = TypeVar("T", bound="TaskCreate")


@_attrs_define
class TaskCreate:
    """
    Attributes:
        duid (str):
        dartboard_duid (str):
        order (str):
        status_duid (str):
        source_user (Union[Unset, None, str]):
        source_type (Union[Unset, TaskSourceType]): * `Unknown` - UNKNOWN
            * `Import` - IMPORT
            * `Onboarding` - ONBOARDING
            * `Recommendation` - RECOMMENDATION
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
            * `AppPaste` - APP_PASTE Default: TaskSourceType.UNKNOWN.
        drafter_duid (Union[Unset, None, str]):
        in_trash (Union[Unset, bool]):
        recommendation_status (Union[Unset, None, RecommendationStatus]): * `Accepted` - ACCEPTED
            * `Declined` - DECLINED
        title (Union[Unset, str]):
        description (Union[Unset, TaskCreateDescription]):
        assignee_duids (Union[Unset, List[str]]):
        subscriber_duids (Union[Unset, List[str]]):
        tag_duids (Union[Unset, List[str]]):
        priority (Union[Unset, None, Priority]): * `Critical` - CRITICAL
            * `High` - HIGH
            * `Medium` - MEDIUM
            * `Low` - LOW
        size (Union[Unset, None, int]):
        due_at (Union[Unset, None, datetime.datetime]):
        remind_at (Union[Unset, None, datetime.datetime]):
    """

    duid: str
    dartboard_duid: str
    order: str
    status_duid: str
    source_user: Union[Unset, None, str] = UNSET
    source_type: Union[Unset, TaskSourceType] = TaskSourceType.UNKNOWN
    drafter_duid: Union[Unset, None, str] = UNSET
    in_trash: Union[Unset, bool] = UNSET
    recommendation_status: Union[Unset, None, RecommendationStatus] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, "TaskCreateDescription"] = UNSET
    assignee_duids: Union[Unset, List[str]] = UNSET
    subscriber_duids: Union[Unset, List[str]] = UNSET
    tag_duids: Union[Unset, List[str]] = UNSET
    priority: Union[Unset, None, Priority] = UNSET
    size: Union[Unset, None, int] = UNSET
    due_at: Union[Unset, None, datetime.datetime] = UNSET
    remind_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        dartboard_duid = self.dartboard_duid
        order = self.order
        status_duid = self.status_duid
        source_user = self.source_user
        source_type: Union[Unset, str] = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type.value

        drafter_duid = self.drafter_duid
        in_trash = self.in_trash
        recommendation_status: Union[Unset, None, str] = UNSET
        if not isinstance(self.recommendation_status, Unset):
            recommendation_status = self.recommendation_status.value if self.recommendation_status else None

        title = self.title
        description: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

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
        due_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.due_at, Unset):
            due_at = self.due_at.isoformat() if self.due_at else None

        remind_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.remind_at, Unset):
            remind_at = self.remind_at.isoformat() if self.remind_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "dartboardDuid": dartboard_duid,
                "order": order,
                "statusDuid": status_duid,
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
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
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
        if due_at is not UNSET:
            field_dict["dueAt"] = due_at
        if remind_at is not UNSET:
            field_dict["remindAt"] = remind_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.task_create_description import TaskCreateDescription

        d = src_dict.copy()
        duid = d.pop("duid")

        dartboard_duid = d.pop("dartboardDuid")

        order = d.pop("order")

        status_duid = d.pop("statusDuid")

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

        title = d.pop("title", UNSET)

        _description = d.pop("description", UNSET)
        description: Union[Unset, TaskCreateDescription]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = TaskCreateDescription.from_dict(_description)

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

        task_create = cls(
            duid=duid,
            dartboard_duid=dartboard_duid,
            order=order,
            status_duid=status_duid,
            source_user=source_user,
            source_type=source_type,
            drafter_duid=drafter_duid,
            in_trash=in_trash,
            recommendation_status=recommendation_status,
            title=title,
            description=description,
            assignee_duids=assignee_duids,
            subscriber_duids=subscriber_duids,
            tag_duids=tag_duids,
            priority=priority,
            size=size,
            due_at=due_at,
            remind_at=remind_at,
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
