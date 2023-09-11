from enum import Enum


class StatusKind(str, Enum):
    BLOCKED = "Blocked"
    CANCELED = "Canceled"
    FINISHED = "Finished"
    STARTED = "Started"
    UNSTARTED = "Unstarted"

    def __str__(self) -> str:
        return str(self.value)
