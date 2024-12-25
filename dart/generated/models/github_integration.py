from typing import Any, TypeVar, Union, cast

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
        installation_link (Union[None, str]):
        linkback_enabled (bool):
        auto_assign (bool):
        status_on_branch_link_copy_duid (Union[None, str]):
        status_on_branch_create_duid (Union[None, str]):
        status_on_pr_draft_duid (Union[None, str]):
        status_on_pr_ready_duid (Union[None, str]):
        status_on_pr_merge_duid (Union[None, str]):
    """

    status: GithubIntegrationTenantExtensionStatus
    installation_link: Union[None, str]
    linkback_enabled: bool
    auto_assign: bool
    status_on_branch_link_copy_duid: Union[None, str]
    status_on_branch_create_duid: Union[None, str]
    status_on_pr_draft_duid: Union[None, str]
    status_on_pr_ready_duid: Union[None, str]
    status_on_pr_merge_duid: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        installation_link: Union[None, str]
        installation_link = self.installation_link

        linkback_enabled = self.linkback_enabled

        auto_assign = self.auto_assign

        status_on_branch_link_copy_duid: Union[None, str]
        status_on_branch_link_copy_duid = self.status_on_branch_link_copy_duid

        status_on_branch_create_duid: Union[None, str]
        status_on_branch_create_duid = self.status_on_branch_create_duid

        status_on_pr_draft_duid: Union[None, str]
        status_on_pr_draft_duid = self.status_on_pr_draft_duid

        status_on_pr_ready_duid: Union[None, str]
        status_on_pr_ready_duid = self.status_on_pr_ready_duid

        status_on_pr_merge_duid: Union[None, str]
        status_on_pr_merge_duid = self.status_on_pr_merge_duid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "installationLink": installation_link,
                "linkbackEnabled": linkback_enabled,
                "autoAssign": auto_assign,
                "statusOnBranchLinkCopyDuid": status_on_branch_link_copy_duid,
                "statusOnBranchCreateDuid": status_on_branch_create_duid,
                "statusOnPrDraftDuid": status_on_pr_draft_duid,
                "statusOnPrReadyDuid": status_on_pr_ready_duid,
                "statusOnPrMergeDuid": status_on_pr_merge_duid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        status = GithubIntegrationTenantExtensionStatus(d.pop("status"))

        def _parse_installation_link(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        installation_link = _parse_installation_link(d.pop("installationLink"))

        linkback_enabled = d.pop("linkbackEnabled")

        auto_assign = d.pop("autoAssign")

        def _parse_status_on_branch_link_copy_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        status_on_branch_link_copy_duid = _parse_status_on_branch_link_copy_duid(d.pop("statusOnBranchLinkCopyDuid"))

        def _parse_status_on_branch_create_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        status_on_branch_create_duid = _parse_status_on_branch_create_duid(d.pop("statusOnBranchCreateDuid"))

        def _parse_status_on_pr_draft_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        status_on_pr_draft_duid = _parse_status_on_pr_draft_duid(d.pop("statusOnPrDraftDuid"))

        def _parse_status_on_pr_ready_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        status_on_pr_ready_duid = _parse_status_on_pr_ready_duid(d.pop("statusOnPrReadyDuid"))

        def _parse_status_on_pr_merge_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        status_on_pr_merge_duid = _parse_status_on_pr_merge_duid(d.pop("statusOnPrMergeDuid"))

        github_integration = cls(
            status=status,
            installation_link=installation_link,
            linkback_enabled=linkback_enabled,
            auto_assign=auto_assign,
            status_on_branch_link_copy_duid=status_on_branch_link_copy_duid,
            status_on_branch_create_duid=status_on_branch_create_duid,
            status_on_pr_draft_duid=status_on_pr_draft_duid,
            status_on_pr_ready_duid=status_on_pr_ready_duid,
            status_on_pr_merge_duid=status_on_pr_merge_duid,
        )

        github_integration.additional_properties = d
        return github_integration

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
