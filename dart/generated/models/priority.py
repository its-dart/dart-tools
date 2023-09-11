from enum import Enum


class Priority(str, Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    LOW = "Low"
    MEDIUM = "Medium"

    def __str__(self) -> str:
        return str(self.value)
