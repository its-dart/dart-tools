from enum import Enum


class DartboardKind(str, Enum):
    ACTIVE = "Active"
    BACKLOG = "Backlog"
    CUSTOM = "Custom"
    FINISHED = "Finished"
    NEXT = "Next"

    def __str__(self) -> str:
        return str(self.value)
