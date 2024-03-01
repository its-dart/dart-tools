from enum import Enum


class SprintMode(str, Enum):
    ANBA = "ANBA"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
