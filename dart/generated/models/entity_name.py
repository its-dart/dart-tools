from enum import Enum


class EntityName(str, Enum):
    BRAINSTORM = "brainstorm"
    COMMENT = "comment"
    DARTBOARD = "dartboard"
    DASHBOARD = "dashboard"
    DOC = "doc"
    FOLDER = "folder"
    FORM = "form"
    PROPERTY = "property"
    SPACE = "space"
    STATUS = "status"
    TASK = "task"
    TENANT = "tenant"
    UNKNOWN = "UNKNOWN"
    USER = "user"
    VIEW = "view"

    def __str__(self) -> str:
        return str(self.value)
