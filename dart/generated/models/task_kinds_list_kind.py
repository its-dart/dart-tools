from enum import Enum


class TaskKindsListKind(str, Enum):
    DEFAULT = "Default"
    MILESTONE = "Milestone"

    def __str__(self) -> str:
        return str(self.value)
