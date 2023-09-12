from enum import Enum


class CycleMode(str, Enum):
    ANBA = "ANBA"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
