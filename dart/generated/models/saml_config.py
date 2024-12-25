from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.saml_config_tenant_extension_status import SamlConfigTenantExtensionStatus

T = TypeVar("T", bound="SamlConfig")


@_attrs_define
class SamlConfig:
    """
    Attributes:
        status (SamlConfigTenantExtensionStatus): * `Disabled` - DISABLED
            * `Enabled` - ENABLED
        idp_url (str):
        idp_xml (str):
    """

    status: SamlConfigTenantExtensionStatus
    idp_url: str
    idp_xml: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        idp_url = self.idp_url

        idp_xml = self.idp_xml

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "idpUrl": idp_url,
                "idpXml": idp_xml,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        status = SamlConfigTenantExtensionStatus(d.pop("status"))

        idp_url = d.pop("idpUrl")

        idp_xml = d.pop("idpXml")

        saml_config = cls(
            status=status,
            idp_url=idp_url,
            idp_xml=idp_xml,
        )

        saml_config.additional_properties = d
        return saml_config

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
