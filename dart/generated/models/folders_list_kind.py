from enum import Enum


class FoldersListKind(str, Enum):
    DEFAULT = "Default"
    OTHER = "Other"
    REPORTS = "Reports"

    def __str__(self) -> str:
        return str(self.value)
