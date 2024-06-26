from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.color_name import ColorName
from ..models.theme import Theme
from ..models.user_role import UserRole
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
        role (UserRole): * `Admin` - ADMIN
            * `Member` - MEMBER
            * `Guest` - GUEST
        email (str):
        name (str):
        abrev (str):
        theme (Theme): * `System Default` - SYSTEM_DEFAULT
            * `Light` - LIGHT
            * `Dark` - DARK
        color_hex (str):
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
        sections (Any):
        layout (Any):
        is_admin (bool):
        updated_by_client_duid (Union[Unset, None, str]):
        image_url (Optional[str]):
        auth_token (Optional[str]):
        google_data (Optional[GoogleData]):
    """

    duid: str
    status: UserStatus
    role: UserRole
    email: str
    name: str
    abrev: str
    theme: Theme
    color_hex: str
    color_name: ColorName
    sections: Any
    layout: Any
    is_admin: bool
    image_url: Optional[str]
    auth_token: Optional[str]
    google_data: Optional["GoogleData"]
    updated_by_client_duid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        status = self.status.value

        role = self.role.value

        email = self.email
        name = self.name
        abrev = self.abrev
        theme = self.theme.value

        color_hex = self.color_hex
        color_name = self.color_name.value

        sections = self.sections
        layout = self.layout
        is_admin = self.is_admin
        updated_by_client_duid = self.updated_by_client_duid
        image_url = self.image_url
        auth_token = self.auth_token
        google_data = self.google_data.to_dict() if self.google_data else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "status": status,
                "role": role,
                "email": email,
                "name": name,
                "abrev": abrev,
                "theme": theme,
                "colorHex": color_hex,
                "colorName": color_name,
                "sections": sections,
                "layout": layout,
                "isAdmin": is_admin,
                "imageUrl": image_url,
                "authToken": auth_token,
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

        role = UserRole(d.pop("role"))

        email = d.pop("email")

        name = d.pop("name")

        abrev = d.pop("abrev")

        theme = Theme(d.pop("theme"))

        color_hex = d.pop("colorHex")

        color_name = ColorName(d.pop("colorName"))

        sections = d.pop("sections")

        layout = d.pop("layout")

        is_admin = d.pop("isAdmin")

        updated_by_client_duid = d.pop("updatedByClientDuid", UNSET)

        image_url = d.pop("imageUrl")

        auth_token = d.pop("authToken")

        _google_data = d.pop("googleData")
        google_data: Optional[GoogleData]
        if _google_data is None:
            google_data = None
        else:
            google_data = GoogleData.from_dict(_google_data)

        user = cls(
            duid=duid,
            status=status,
            role=role,
            email=email,
            name=name,
            abrev=abrev,
            theme=theme,
            color_hex=color_hex,
            color_name=color_name,
            sections=sections,
            layout=layout,
            is_admin=is_admin,
            updated_by_client_duid=updated_by_client_duid,
            image_url=image_url,
            auth_token=auth_token,
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
