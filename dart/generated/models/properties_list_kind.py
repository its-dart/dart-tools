from enum import Enum


class PropertiesListKind(str, Enum):
    CHECKBOX = "Checkbox"
    DATES = "Dates"
    DEFAULT_ASSIGNEES = "Default: Assignees"
    DEFAULT_ATTACHMENTS = "Default: Attachments"
    DEFAULT_CREATED = "Default: Created"
    DEFAULT_CREATED_BY = "Default: Created by"
    DEFAULT_DARTBOARD = "Default: Dartboard"
    DEFAULT_DATES = "Default: Dates"
    DEFAULT_DESCRIPTION = "Default: Description"
    DEFAULT_LAST_UPDATED = "Default: Last updated"
    DEFAULT_LAST_UPDATED_BY = "Default: Last updated by"
    DEFAULT_PRIORITY = "Default: Priority"
    DEFAULT_SIZE = "Default: Size"
    DEFAULT_STATUS = "Default: Status"
    DEFAULT_TAGS = "Default: Tags"
    DEFAULT_TIME_TRACKING = "Default: Time tracking"
    DEFAULT_TITLE = "Default: Title"
    DEFAULT_TYPE = "Default: Type"
    MULTISELECT = "Multiselect"
    NUMBER = "Number"
    SELECT = "Select"
    STATUS = "Status"
    TEXT = "Text"
    TIME_TRACKING = "Time tracking"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
