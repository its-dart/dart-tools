from enum import Enum


class OperationModelKind(str, Enum):
    COMMENT = "comment"
    COMMENT_REACTION = "comment_reaction"
    DARTBOARD = "dartboard"
    DOC = "doc"
    EVENT = "event"
    EVENT_SUBSCRIPTION = "event_subscription"
    FOLDER = "folder"
    LAYOUT = "layout"
    OPTION = "option"
    PROPERTY = "property"
    RELATIONSHIP = "relationship"
    RELATIONSHIP_KIND = "relationship_kind"
    SPACE = "space"
    STATUS = "status"
    TASK = "task"
    TASK_ATTACHMENT = "task_attachment"
    TASK_DOC_RELATIONSHIP = "task_doc_relationship"
    TASK_LINK = "task_link"
    TENANT = "tenant"
    USER = "user"
    USER_DARTBOARD_LAYOUT = "user_dartboard_layout"
    VIEW = "view"

    def __str__(self) -> str:
        return str(self.value)
