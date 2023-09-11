from enum import Enum


class GithubIntegrationTenantExtensionStatus(str, Enum):
    DISABLED = "Disabled"
    ENABLED = "Enabled"
    PENDING = "Pending"
    SUSPENDED = "Suspended"

    def __str__(self) -> str:
        return str(self.value)
