from enum import Enum


class ReportKind(str, Enum):
    CHANGELOG = "Changelog"
    STANDUP = "Standup"

    def __str__(self) -> str:
        return str(self.value)
