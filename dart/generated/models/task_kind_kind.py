from enum import Enum


class TaskKindKind(str, Enum):
    DEFAULT = "Default"
    MILESTONE = "Milestone"

    def __str__(self) -> str:
        return str(self.value)
