from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.theme import Theme
from ..models.user_role import UserRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserUpdate")


@_attrs_define
class UserUpdate:
    """
    Attributes:
        duid (str):
        role (Union[Unset, UserRole]): * `Admin` - ADMIN
            * `Member` - MEMBER
            * `Guest` - GUEST
            * `Technical admin` - TECHNICAL_ADMIN
            * `Financial admin` - FINANCIAL_ADMIN
        name (Union[Unset, str]):
        theme (Union[Unset, Theme]): * `System Default` - SYSTEM_DEFAULT
            * `Light` - LIGHT
            * `Dark` - DARK
        color_hex (Union[Unset, str]):
        open_in_native_app (Union[Unset, bool]):
        last_url_path (Union[None, Unset, str]):
        first_day_of_week (Union[Unset, int]):
        sections (Union[Unset, Any]):
        layout (Union[Unset, Any]):
        notification_default (Union[Unset, bool]):
        notification_in_app (Union[Unset, bool]):
        notification_email (Union[Unset, bool]):
        notification_slack (Union[Unset, bool]):
    """

    duid: str
    role: Union[Unset, UserRole] = UNSET
    name: Union[Unset, str] = UNSET
    theme: Union[Unset, Theme] = UNSET
    color_hex: Union[Unset, str] = UNSET
    open_in_native_app: Union[Unset, bool] = UNSET
    last_url_path: Union[None, Unset, str] = UNSET
    first_day_of_week: Union[Unset, int] = UNSET
    sections: Union[Unset, Any] = UNSET
    layout: Union[Unset, Any] = UNSET
    notification_default: Union[Unset, bool] = UNSET
    notification_in_app: Union[Unset, bool] = UNSET
    notification_email: Union[Unset, bool] = UNSET
    notification_slack: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        name = self.name

        theme: Union[Unset, str] = UNSET
        if not isinstance(self.theme, Unset):
            theme = self.theme.value

        color_hex = self.color_hex

        open_in_native_app = self.open_in_native_app

        last_url_path: Union[None, Unset, str]
        if isinstance(self.last_url_path, Unset):
            last_url_path = UNSET
        else:
            last_url_path = self.last_url_path

        first_day_of_week = self.first_day_of_week

        sections = self.sections

        layout = self.layout

        notification_default = self.notification_default

        notification_in_app = self.notification_in_app

        notification_email = self.notification_email

        notification_slack = self.notification_slack

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role
        if name is not UNSET:
            field_dict["name"] = name
        if theme is not UNSET:
            field_dict["theme"] = theme
        if color_hex is not UNSET:
            field_dict["colorHex"] = color_hex
        if open_in_native_app is not UNSET:
            field_dict["openInNativeApp"] = open_in_native_app
        if last_url_path is not UNSET:
            field_dict["lastUrlPath"] = last_url_path
        if first_day_of_week is not UNSET:
            field_dict["firstDayOfWeek"] = first_day_of_week
        if sections is not UNSET:
            field_dict["sections"] = sections
        if layout is not UNSET:
            field_dict["layout"] = layout
        if notification_default is not UNSET:
            field_dict["notificationDefault"] = notification_default
        if notification_in_app is not UNSET:
            field_dict["notificationInApp"] = notification_in_app
        if notification_email is not UNSET:
            field_dict["notificationEmail"] = notification_email
        if notification_slack is not UNSET:
            field_dict["notificationSlack"] = notification_slack

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        _role = d.pop("role", UNSET)
        role: Union[Unset, UserRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = UserRole(_role)

        name = d.pop("name", UNSET)

        _theme = d.pop("theme", UNSET)
        theme: Union[Unset, Theme]
        if isinstance(_theme, Unset):
            theme = UNSET
        else:
            theme = Theme(_theme)

        color_hex = d.pop("colorHex", UNSET)

        open_in_native_app = d.pop("openInNativeApp", UNSET)

        def _parse_last_url_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_url_path = _parse_last_url_path(d.pop("lastUrlPath", UNSET))

        first_day_of_week = d.pop("firstDayOfWeek", UNSET)

        sections = d.pop("sections", UNSET)

        layout = d.pop("layout", UNSET)

        notification_default = d.pop("notificationDefault", UNSET)

        notification_in_app = d.pop("notificationInApp", UNSET)

        notification_email = d.pop("notificationEmail", UNSET)

        notification_slack = d.pop("notificationSlack", UNSET)

        user_update = cls(
            duid=duid,
            role=role,
            name=name,
            theme=theme,
            color_hex=color_hex,
            open_in_native_app=open_in_native_app,
            last_url_path=last_url_path,
            first_day_of_week=first_day_of_week,
            sections=sections,
            layout=layout,
            notification_default=notification_default,
            notification_in_app=notification_in_app,
            notification_email=notification_email,
            notification_slack=notification_slack,
        )

        user_update.additional_properties = d
        return user_update

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
