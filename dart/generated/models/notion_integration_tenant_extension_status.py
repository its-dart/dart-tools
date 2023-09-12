from enum import Enum


class NotionIntegrationTenantExtensionStatus(str, Enum):
    DISABLED = "Disabled"
    ENABLED = "Enabled"
    PENDING = "Pending"

    def __str__(self) -> str:
        return str(self.value)
