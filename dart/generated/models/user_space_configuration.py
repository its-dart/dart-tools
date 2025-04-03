import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.assignee import Assignee


T = TypeVar("T", bound="UserSpaceConfiguration")


@_attrs_define
class UserSpaceConfiguration:
    """
    Attributes:
        today (datetime.date):
        dartboards (list[str]):
        folders (list[str]):
        types (list[str]):
        statuses (list[str]):
        assignees (list['Assignee']):
        tags (list[str]):
        priorities (list[str]):
        sizes (list[int]):
    """

    today: datetime.date
    dartboards: list[str]
    folders: list[str]
    types: list[str]
    statuses: list[str]
    assignees: list["Assignee"]
    tags: list[str]
    priorities: list[str]
    sizes: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        today = self.today.isoformat()

        dartboards = self.dartboards

        folders = self.folders

        types = self.types

        statuses = self.statuses

        assignees = []
        for assignees_item_data in self.assignees:
            assignees_item = assignees_item_data.to_dict()
            assignees.append(assignees_item)

        tags = self.tags

        priorities = self.priorities

        sizes = self.sizes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "today": today,
                "dartboards": dartboards,
                "folders": folders,
                "types": types,
                "statuses": statuses,
                "assignees": assignees,
                "tags": tags,
                "priorities": priorities,
                "sizes": sizes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assignee import Assignee

        d = dict(src_dict)
        today = isoparse(d.pop("today")).date()

        dartboards = cast(list[str], d.pop("dartboards"))

        folders = cast(list[str], d.pop("folders"))

        types = cast(list[str], d.pop("types"))

        statuses = cast(list[str], d.pop("statuses"))

        assignees = []
        _assignees = d.pop("assignees")
        for assignees_item_data in _assignees:
            assignees_item = Assignee.from_dict(assignees_item_data)

            assignees.append(assignees_item)

        tags = cast(list[str], d.pop("tags"))

        priorities = cast(list[str], d.pop("priorities"))

        sizes = cast(list[int], d.pop("sizes"))

        user_space_configuration = cls(
            today=today,
            dartboards=dartboards,
            folders=folders,
            types=types,
            statuses=statuses,
            assignees=assignees,
            tags=tags,
            priorities=priorities,
            sizes=sizes,
        )

        user_space_configuration.additional_properties = d
        return user_space_configuration

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
