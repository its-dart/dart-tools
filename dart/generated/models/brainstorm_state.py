from enum import Enum


class BrainstormState(str, Enum):
    PAUSED = "Paused"
    RUNNING = "Running"
    STOPPED = "Stopped"

    def __str__(self) -> str:
        return str(self.value)
