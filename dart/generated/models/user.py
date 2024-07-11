from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
        image_url (Union[None, str]):
        is_admin (bool):
        auth_token (Union[None, str]):
        google_data (Union['GoogleData', None]):
        updated_by_client_duid (Union[None, Unset, str]):
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
    image_url: Union[None, str]
    is_admin: bool
    auth_token: Union[None, str]
    google_data: Union["GoogleData", None]
    updated_by_client_duid: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.google_data import GoogleData

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

        image_url: Union[None, str]
        image_url = self.image_url

        is_admin = self.is_admin

        auth_token: Union[None, str]
        auth_token = self.auth_token

        google_data: Union[Dict[str, Any], None]
        if isinstance(self.google_data, GoogleData):
            google_data = self.google_data.to_dict()
        else:
            google_data = self.google_data

        updated_by_client_duid: Union[None, Unset, str]
        if isinstance(self.updated_by_client_duid, Unset):
            updated_by_client_duid = UNSET
        else:
            updated_by_client_duid = self.updated_by_client_duid

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
                "imageUrl": image_url,
                "isAdmin": is_admin,
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

        def _parse_image_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        image_url = _parse_image_url(d.pop("imageUrl"))

        is_admin = d.pop("isAdmin")

        def _parse_auth_token(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        auth_token = _parse_auth_token(d.pop("authToken"))

        def _parse_google_data(data: object) -> Union["GoogleData", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                google_data_type_0 = GoogleData.from_dict(data)

                return google_data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GoogleData", None], data)

        google_data = _parse_google_data(d.pop("googleData"))

        def _parse_updated_by_client_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_client_duid = _parse_updated_by_client_duid(d.pop("updatedByClientDuid", UNSET))

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
            image_url=image_url,
            is_admin=is_admin,
            auth_token=auth_token,
            google_data=google_data,
            updated_by_client_duid=updated_by_client_duid,
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
