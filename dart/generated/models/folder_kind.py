from enum import Enum


class FolderKind(str, Enum):
    DEFAULT = "Default"
    OTHER = "Other"
    REPORTS = "Reports"

    def __str__(self) -> str:
        return str(self.value)
