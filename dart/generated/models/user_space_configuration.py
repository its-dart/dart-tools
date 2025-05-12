import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.user import User


T = TypeVar("T", bound="UserSpaceConfiguration")


@_attrs_define
class UserSpaceConfiguration:
    """
    Attributes:
        today (datetime.date):
        user (User):
        dartboards (list[str]):
        folders (list[str]):
        types (list[str]):
        statuses (list[str]):
        assignees (list['User']):
        tags (list[str]):
        priorities (list[str]):
        sizes (Union[list[Union[int, str]], str]):
    """

    today: datetime.date
    user: "User"
    dartboards: list[str]
    folders: list[str]
    types: list[str]
    statuses: list[str]
    assignees: list["User"]
    tags: list[str]
    priorities: list[str]
    sizes: Union[list[Union[int, str]], str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        today = self.today.isoformat()

        user = self.user.to_dict()

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

        sizes: Union[list[Union[int, str]], str]
        if isinstance(self.sizes, list):
            sizes = []
            for sizes_type_1_item_data in self.sizes:
                sizes_type_1_item: Union[int, str]
                sizes_type_1_item = sizes_type_1_item_data
                sizes.append(sizes_type_1_item)

        else:
            sizes = self.sizes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "today": today,
                "user": user,
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
        from ..models.user import User

        d = dict(src_dict)
        today = isoparse(d.pop("today")).date()

        user = User.from_dict(d.pop("user"))

        dartboards = cast(list[str], d.pop("dartboards"))

        folders = cast(list[str], d.pop("folders"))

        types = cast(list[str], d.pop("types"))

        statuses = cast(list[str], d.pop("statuses"))

        assignees = []
        _assignees = d.pop("assignees")
        for assignees_item_data in _assignees:
            assignees_item = User.from_dict(assignees_item_data)

            assignees.append(assignees_item)

        tags = cast(list[str], d.pop("tags"))

        priorities = cast(list[str], d.pop("priorities"))

        def _parse_sizes(data: object) -> Union[list[Union[int, str]], str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sizes_type_1 = []
                _sizes_type_1 = data
                for sizes_type_1_item_data in _sizes_type_1:

                    def _parse_sizes_type_1_item(data: object) -> Union[int, str]:
                        return cast(Union[int, str], data)

                    sizes_type_1_item = _parse_sizes_type_1_item(sizes_type_1_item_data)

                    sizes_type_1.append(sizes_type_1_item)

                return sizes_type_1
            except:  # noqa: E722
                pass
            return cast(Union[list[Union[int, str]], str], data)

        sizes = _parse_sizes(d.pop("sizes"))

        user_space_configuration = cls(
            today=today,
            user=user,
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
