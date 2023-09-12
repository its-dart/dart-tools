from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.color_name import ColorName
from ..models.theme import Theme
from ..models.user_status import UserStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_data import GoogleData


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        duid (str):
        status (UserStatus): * `PendingSubscriptionUpgrade` - PENDING_SUBSCRIPTION_UPGRADE
            * `Invited` - INVITED
            * `PendingEmailVerification` - PENDING_EMAIL_VERIFICATION
            * `Active` - ACTIVE
            * `Deactivated` - DEACTIVATED
        email (str):
        name (str):
        abrev (str):
        theme (Theme): * `System Default` - SYSTEM_DEFAULT
            * `Light` - LIGHT
            * `Dark` - DARK
        color_name (ColorName): * `Red` - RED
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
        is_admin (bool):
        updated_by_client_duid (Union[Unset, None, str]):
        image_url (Optional[str]):
        google_data (Optional[GoogleData]):
    """

    duid: str
    status: UserStatus
    email: str
    name: str
    abrev: str
    theme: Theme
    color_name: ColorName
    is_admin: bool
    image_url: Optional[str]
    google_data: Optional["GoogleData"]
    updated_by_client_duid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        status = self.status.value

        email = self.email
        name = self.name
        abrev = self.abrev
        theme = self.theme.value

        color_name = self.color_name.value

        is_admin = self.is_admin
        updated_by_client_duid = self.updated_by_client_duid
        image_url = self.image_url
        google_data = self.google_data.to_dict() if self.google_data else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "status": status,
                "email": email,
                "name": name,
                "abrev": abrev,
                "theme": theme,
                "colorName": color_name,
                "isAdmin": is_admin,
                "imageUrl": image_url,
                "googleData": google_data,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_data import GoogleData

        d = src_dict.copy()
        duid = d.pop("duid")

        status = UserStatus(d.pop("status"))

        email = d.pop("email")

        name = d.pop("name")

        abrev = d.pop("abrev")

        theme = Theme(d.pop("theme"))

        color_name = ColorName(d.pop("colorName"))

        is_admin = d.pop("isAdmin")

        updated_by_client_duid = d.pop("updatedByClientDuid", UNSET)

        image_url = d.pop("imageUrl")

        _google_data = d.pop("googleData")
        google_data: Optional[GoogleData]
        if _google_data is None:
            google_data = None
        else:
            google_data = GoogleData.from_dict(_google_data)

        user = cls(
            duid=duid,
            status=status,
            email=email,
            name=name,
            abrev=abrev,
            theme=theme,
            color_name=color_name,
            is_admin=is_admin,
            updated_by_client_duid=updated_by_client_duid,
            image_url=image_url,
            google_data=google_data,
        )

        user.additional_properties = d
        return user

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
