from typing import Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_integration_tenant_extension_status import GithubIntegrationTenantExtensionStatus

T = TypeVar("T", bound="GithubIntegration")


@_attrs_define
class GithubIntegration:
    """
    Attributes:
        status (GithubIntegrationTenantExtensionStatus): * `Disabled` - DISABLED
            * `Pending` - PENDING
            * `Suspended` - SUSPENDED
            * `Enabled` - ENABLED
        linkback_enabled (bool):
        installation_link (Optional[str]):
        status_on_branch_link_copy_duid (Optional[str]):
        status_on_branch_create_duid (Optional[str]):
        status_on_pr_draft_duid (Optional[str]):
        status_on_pr_ready_duid (Optional[str]):
        status_on_pr_merge_duid (Optional[str]):
    """

    status: GithubIntegrationTenantExtensionStatus
    linkback_enabled: bool
    installation_link: Optional[str]
    status_on_branch_link_copy_duid: Optional[str]
    status_on_branch_create_duid: Optional[str]
    status_on_pr_draft_duid: Optional[str]
    status_on_pr_ready_duid: Optional[str]
    status_on_pr_merge_duid: Optional[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        linkback_enabled = self.linkback_enabled
        installation_link = self.installation_link
        status_on_branch_link_copy_duid = self.status_on_branch_link_copy_duid
        status_on_branch_create_duid = self.status_on_branch_create_duid
        status_on_pr_draft_duid = self.status_on_pr_draft_duid
        status_on_pr_ready_duid = self.status_on_pr_ready_duid
        status_on_pr_merge_duid = self.status_on_pr_merge_duid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "linkbackEnabled": linkback_enabled,
                "installationLink": installation_link,
                "statusOnBranchLinkCopyDuid": status_on_branch_link_copy_duid,
                "statusOnBranchCreateDuid": status_on_branch_create_duid,
                "statusOnPrDraftDuid": status_on_pr_draft_duid,
                "statusOnPrReadyDuid": status_on_pr_ready_duid,
                "statusOnPrMergeDuid": status_on_pr_merge_duid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = GithubIntegrationTenantExtensionStatus(d.pop("status"))

        linkback_enabled = d.pop("linkbackEnabled")

        installation_link = d.pop("installationLink")

        status_on_branch_link_copy_duid = d.pop("statusOnBranchLinkCopyDuid")

        status_on_branch_create_duid = d.pop("statusOnBranchCreateDuid")

        status_on_pr_draft_duid = d.pop("statusOnPrDraftDuid")

        status_on_pr_ready_duid = d.pop("statusOnPrReadyDuid")

        status_on_pr_merge_duid = d.pop("statusOnPrMergeDuid")

        github_integration = cls(
            status=status,
            linkback_enabled=linkback_enabled,
            installation_link=installation_link,
            status_on_branch_link_copy_duid=status_on_branch_link_copy_duid,
            status_on_branch_create_duid=status_on_branch_create_duid,
            status_on_pr_draft_duid=status_on_pr_draft_duid,
            status_on_pr_ready_duid=status_on_pr_ready_duid,
            status_on_pr_merge_duid=status_on_pr_merge_duid,
        )

        github_integration.additional_properties = d
        return github_integration

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
