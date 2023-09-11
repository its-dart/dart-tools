from typing import Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GoogleData")


@_attrs_define
class GoogleData:
    """
    Attributes:
        name (str):
        email (str):
        picture_url (Optional[str]):
        organization_domain (Optional[str]):
    """

    name: str
    email: str
    picture_url: Optional[str]
    organization_domain: Optional[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        email = self.email
        picture_url = self.picture_url
        organization_domain = self.organization_domain

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "email": email,
                "pictureUrl": picture_url,
                "organizationDomain": organization_domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        email = d.pop("email")

        picture_url = d.pop("pictureUrl")

        organization_domain = d.pop("organizationDomain")

        google_data = cls(
            name=name,
            email=email,
            picture_url=picture_url,
            organization_domain=organization_domain,
        )

        google_data.additional_properties = d
        return google_data

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
