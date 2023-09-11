from enum import Enum


class Theme(str, Enum):
    DARK = "Dark"
    LIGHT = "Light"
    SYSTEM_DEFAULT = "System Default"

    def __str__(self) -> str:
        return str(self.value)
