from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.color_name import ColorName
from ..models.theme import Theme
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserCreate")


@_attrs_define
class UserCreate:
    """
    Attributes:
        duid (str):
        name (Union[Unset, str]):
        theme (Union[Unset, Theme]): * `System Default` - SYSTEM_DEFAULT
            * `Light` - LIGHT
            * `Dark` - DARK
        color_name (Union[Unset, ColorName]): * `Red` - RED
            * `Dark Blue` - DARK_BLUE
            * `Dark Orange` - DARK_ORANGE
            * `Dark Green` - DARK_GREEN
            * `Purple` - PURPLE
            * `Dark Teal` - DARK_TEAL
            * `Pink` - PINK
            * `Orange` - ORANGE
            * `Green` - GREEN
            * `Yellow` - YELLOW
            * `Brown` - BROWN
            * `Dark Red` - DARK_RED
            * `Flat Green` - FLAT_GREEN
            * `Red Orange` - RED_ORANGE
            * `Teal` - TEAL
            * `Light Green` - LIGHT_GREEN
            * `Light Blue` - LIGHT_BLUE
            * `Light Purple` - LIGHT_PURPLE
            * `Light Orange` - LIGHT_ORANGE
            * `Light Pink` - LIGHT_PINK
            * `Tan` - TAN
            * `Dark Gray` - DARK_GRAY
            * `Light Brown` - LIGHT_BROWN
            * `Light Gray` - LIGHT_GRAY
        open_in_native_app (Union[Unset, bool]):
        notification_default (Union[Unset, bool]):
        notification_email (Union[Unset, bool]):
        notification_slack (Union[Unset, bool]):
    """

    duid: str
    name: Union[Unset, str] = UNSET
    theme: Union[Unset, Theme] = UNSET
    color_name: Union[Unset, ColorName] = UNSET
    open_in_native_app: Union[Unset, bool] = UNSET
    notification_default: Union[Unset, bool] = UNSET
    notification_email: Union[Unset, bool] = UNSET
    notification_slack: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        name = self.name
        theme: Union[Unset, str] = UNSET
        if not isinstance(self.theme, Unset):
            theme = self.theme.value

        color_name: Union[Unset, str] = UNSET
        if not isinstance(self.color_name, Unset):
            color_name = self.color_name.value

        open_in_native_app = self.open_in_native_app
        notification_default = self.notification_default
        notification_email = self.notification_email
        notification_slack = self.notification_slack

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if theme is not UNSET:
            field_dict["theme"] = theme
        if color_name is not UNSET:
            field_dict["colorName"] = color_name
        if open_in_native_app is not UNSET:
            field_dict["openInNativeApp"] = open_in_native_app
        if notification_default is not UNSET:
            field_dict["notificationDefault"] = notification_default
        if notification_email is not UNSET:
            field_dict["notificationEmail"] = notification_email
        if notification_slack is not UNSET:
            field_dict["notificationSlack"] = notification_slack

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        name = d.pop("name", UNSET)

        _theme = d.pop("theme", UNSET)
        theme: Union[Unset, Theme]
        if isinstance(_theme, Unset):
            theme = UNSET
        else:
            theme = Theme(_theme)

        _color_name = d.pop("colorName", UNSET)
        color_name: Union[Unset, ColorName]
        if isinstance(_color_name, Unset):
            color_name = UNSET
        else:
            color_name = ColorName(_color_name)

        open_in_native_app = d.pop("openInNativeApp", UNSET)

        notification_default = d.pop("notificationDefault", UNSET)

        notification_email = d.pop("notificationEmail", UNSET)

        notification_slack = d.pop("notificationSlack", UNSET)

        user_create = cls(
            duid=duid,
            name=name,
            theme=theme,
            color_name=color_name,
            open_in_native_app=open_in_native_app,
            notification_default=notification_default,
            notification_email=notification_email,
            notification_slack=notification_slack,
        )

        user_create.additional_properties = d
        return user_create

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
