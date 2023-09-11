from enum import Enum


class SpaceKind(str, Enum):
    OTHER = "Other"
    PERSONAL = "Personal"
    WORKSPACE = "Workspace"

    def __str__(self) -> str:
        return str(self.value)
