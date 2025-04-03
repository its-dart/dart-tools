from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConciseTask")


@_attrs_define
class ConciseTask:
    """This concise task serializer is going to be used in tasks listing view only.

    Attributes:
        id (str): The ID. This can and should be null on creation and not otherwise.
        permalink (str): The permanent link, which is a URL that can be used to open the task in Dart. This can and
            should be null on creation and not otherwise.
        title (str): The title, which is a short description of what needs to be done. This cannot be null.
        parent_id (Union[None, str]): The ID of the parent task. This can be null.
        dartboard (str): The title of the dartboard, which is a project or list of tasks. Common options are Active,
            Next, and Backlog, although what is possible depends on the workspace. If the dartboard is ambiguous it may need
            to include a prefix with the name of the space, which is a folder for dartboards.
        type_ (str): The title of the type of the task. This can be null on creation and not otherwise.
        status (str): The status from the list of available statuses. Common options are To-do, Doing, and Done,
            although what is possible depends on the workspace. This can be null on creation and not otherwise.
        assignees (Union[Unset, list[str]]): The names or emails of the users that the task is assigned to. Either this
            or assignee must be included, depending on whether the workspaces allows multiple assignees or not. If included,
            this can be null on creation and not otherwise.
        assignee (Union[None, Unset, str]): The name or email of the user that the task is assigned to. Either this or
            assignees must be included, depending on whether the workspaces allows multiple assignees or not. If included,
            this can be null on creation and not otherwise.
        tags (Union[Unset, list[str]]): Any tags that should be applied to the task, which can be used to filter and
            search for tasks. Tags are also known as labels or components and are strings that can be anything, but should
            be short and descriptive. This list can be empty.
        priority (Union[None, Unset, str]): The priority, which is a string that can be one of Critical, High, Medium,
            or Low. This is used to sort tasks and determine which tasks should be done first. This can be null.
        start_at (Union[None, Unset, str]): The start date, which is a date and time that the task should be started by
            in ISO format. It should be at 9:00am in the timezone of the user. This can be null.
        due_at (Union[None, Unset, str]): The due date, which is a date and time that the task should be completed by in
            ISO format. It should be at 9:00am in the timezone of the user. This can be null.
        size (Union[None, Unset, int]): The size, which is a number that represents the amount of work that needs to be
            done. This is used to determine how long the task will take to complete. This can be null.
        time_tracking (Union[Unset, str]): The time tracking, which is a string that indicates the amount of time spent
            on the task in hh:mm:ss format (or an empty string if no time has been tracked). This can be null on creation
            and not otherwise.
    """

    id: str
    permalink: str
    title: str
    parent_id: Union[None, str]
    dartboard: str
    type_: str
    status: str
    assignees: Union[Unset, list[str]] = UNSET
    assignee: Union[None, Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    priority: Union[None, Unset, str] = UNSET
    start_at: Union[None, Unset, str] = UNSET
    due_at: Union[None, Unset, str] = UNSET
    size: Union[None, Unset, int] = UNSET
    time_tracking: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        permalink = self.permalink

        title = self.title

        parent_id: Union[None, str]
        parent_id = self.parent_id

        dartboard = self.dartboard

        type_ = self.type_

        status = self.status

        assignees: Union[Unset, list[str]] = UNSET
        if not isinstance(self.assignees, Unset):
            assignees = self.assignees

        assignee: Union[None, Unset, str]
        if isinstance(self.assignee, Unset):
            assignee = UNSET
        else:
            assignee = self.assignee

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        priority: Union[None, Unset, str]
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        start_at: Union[None, Unset, str]
        if isinstance(self.start_at, Unset):
            start_at = UNSET
        else:
            start_at = self.start_at

        due_at: Union[None, Unset, str]
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        else:
            due_at = self.due_at

        size: Union[None, Unset, int]
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        time_tracking = self.time_tracking

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "permalink": permalink,
                "title": title,
                "parentId": parent_id,
                "dartboard": dartboard,
                "type": type_,
                "status": status,
            }
        )
        if assignees is not UNSET:
            field_dict["assignees"] = assignees
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if tags is not UNSET:
            field_dict["tags"] = tags
        if priority is not UNSET:
            field_dict["priority"] = priority
        if start_at is not UNSET:
            field_dict["startAt"] = start_at
        if due_at is not UNSET:
            field_dict["dueAt"] = due_at
        if size is not UNSET:
            field_dict["size"] = size
        if time_tracking is not UNSET:
            field_dict["timeTracking"] = time_tracking

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        permalink = d.pop("permalink")

        title = d.pop("title")

        def _parse_parent_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        parent_id = _parse_parent_id(d.pop("parentId"))

        dartboard = d.pop("dartboard")

        type_ = d.pop("type")

        status = d.pop("status")

        assignees = cast(list[str], d.pop("assignees", UNSET))

        def _parse_assignee(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        assignee = _parse_assignee(d.pop("assignee", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        def _parse_priority(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_start_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        start_at = _parse_start_at(d.pop("startAt", UNSET))

        def _parse_due_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        due_at = _parse_due_at(d.pop("dueAt", UNSET))

        def _parse_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size = _parse_size(d.pop("size", UNSET))

        time_tracking = d.pop("timeTracking", UNSET)

        concise_task = cls(
            id=id,
            permalink=permalink,
            title=title,
            parent_id=parent_id,
            dartboard=dartboard,
            type_=type_,
            status=status,
            assignees=assignees,
            assignee=assignee,
            tags=tags,
            priority=priority,
            start_at=start_at,
            due_at=due_at,
            size=size,
            time_tracking=time_tracking,
        )

        concise_task.additional_properties = d
        return concise_task

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
