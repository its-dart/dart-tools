from enum import Enum


class PropertyKind(str, Enum):
    CHECKBOX = "Checkbox"
    DATES = "Dates"
    DEFAULT_ASSIGNEE = "Default: Assignee"
    DEFAULT_CREATED = "Default: Created"
    DEFAULT_CREATED_BY = "Default: Created by"
    DEFAULT_DATES = "Default: Dates"
    DEFAULT_LAST_UPDATED = "Default: Last updated"
    DEFAULT_LAST_UPDATED_BY = "Default: Last updated by"
    DEFAULT_PRIORITY = "Default: Priority"
    DEFAULT_SIZE = "Default: Size"
    DEFAULT_STATUS = "Default: Status"
    DEFAULT_TAGS = "Default: Tags"
    MULTISELECT = "Multiselect"
    NUMBER = "Number"
    SELECT = "Select"
    STATUS = "Status"
    TEXT = "Text"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
