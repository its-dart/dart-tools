from enum import Enum


class SlackIntegrationTenantExtensionStatus(str, Enum):
    DISABLED = "Disabled"
    ENABLED = "Enabled"
    PENDING = "Pending"

    def __str__(self) -> str:
        return str(self.value)
