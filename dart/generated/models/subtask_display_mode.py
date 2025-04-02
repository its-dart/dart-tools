from enum import IntEnum


class SubtaskDisplayMode(IntEnum):
    INDENTED = 1
    COLLAPSED = 2
    FLAT = 3

    def __str__(self) -> str:
        return str(self.value)
