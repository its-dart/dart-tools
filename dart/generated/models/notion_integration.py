from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notion_integration_tenant_extension_status import NotionIntegrationTenantExtensionStatus

T = TypeVar("T", bound="NotionIntegration")


@_attrs_define
class NotionIntegration:
    """
    Attributes:
        status (NotionIntegrationTenantExtensionStatus): * `Disabled` - DISABLED
            * `Pending` - PENDING
            * `Enabled` - ENABLED
        workspace_name (Union[None, str]):
        workspace_icon (Union[None, str]):
    """

    status: NotionIntegrationTenantExtensionStatus
    workspace_name: Union[None, str]
    workspace_icon: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        workspace_name: Union[None, str]
        workspace_name = self.workspace_name

        workspace_icon: Union[None, str]
        workspace_icon = self.workspace_icon

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        status = NotionIntegrationTenantExtensionStatus(d.pop("status"))

        def _parse_workspace_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        workspace_name = _parse_workspace_name(d.pop("workspaceName"))

        def _parse_workspace_icon(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        workspace_icon = _parse_workspace_icon(d.pop("workspaceIcon"))

        notion_integration = cls(
            status=status,
            workspace_name=workspace_name,
            workspace_icon=workspace_icon,
        )

        notion_integration.additional_properties = d
        return notion_integration

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
