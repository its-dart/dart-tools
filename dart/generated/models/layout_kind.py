from enum import Enum


class LayoutKind(str, Enum):
    BOARD = "board"
    CALENDAR = "calendar"
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
