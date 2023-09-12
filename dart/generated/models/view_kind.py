from enum import Enum


class ViewKind(str, Enum):
    CUSTOM = "Custom"
    MY_TASKS = "My tasks"
    SEARCH = "Search"
    TRASH = "Trash"

    def __str__(self) -> str:
        return str(self.value)
