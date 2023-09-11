from enum import Enum


class IconKind(str, Enum):
    EMOJI = "Emoji"
    ICON = "Icon"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
