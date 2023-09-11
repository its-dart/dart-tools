from typing import Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.slack_integration_tenant_extension_status import SlackIntegrationTenantExtensionStatus

T = TypeVar("T", bound="SlackIntegration")


@_attrs_define
class SlackIntegration:
    """
    Attributes:
        status (SlackIntegrationTenantExtensionStatus): * `Disabled` - DISABLED
            * `Pending` - PENDING
            * `Enabled` - ENABLED
        workspace_name (Optional[str]):
        workspace_icon (Optional[str]):
    """

    status: SlackIntegrationTenantExtensionStatus
    workspace_name: Optional[str]
    workspace_icon: Optional[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        workspace_name = self.workspace_name
        workspace_icon = self.workspace_icon

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "workspaceName": workspace_name,
                "workspaceIcon": workspace_icon,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = SlackIntegrationTenantExtensionStatus(d.pop("status"))

        workspace_name = d.pop("workspaceName")

        workspace_icon = d.pop("workspaceIcon")

        slack_integration = cls(
            status=status,
            workspace_name=workspace_name,
            workspace_icon=workspace_icon,
        )

        slack_integration.additional_properties = d
        return slack_integration

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
