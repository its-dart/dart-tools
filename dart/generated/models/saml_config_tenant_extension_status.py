from enum import Enum


class SamlConfigTenantExtensionStatus(str, Enum):
    DISABLED = "Disabled"
    ENABLED = "Enabled"

    def __str__(self) -> str:
        return str(self.value)
