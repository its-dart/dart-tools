from enum import Enum


class TaskDetailMode(str, Enum):
    FULLSCREEN = "Fullscreen"
    OVERLAY = "Overlay"
    RIGHTBAR = "Rightbar"

    def __str__(self) -> str:
        return str(self.value)
