from enum import Enum


class OperationModelKind(str, Enum):
    ATTACHMENT = "attachment"
    BRAINSTORM = "brainstorm"
    COMMENT = "comment"
    COMMENT_REACTION = "comment_reaction"
    DARTBOARD = "dartboard"
    DASHBOARD = "dashboard"
    DOC = "doc"
    EVENT = "event"
    EVENT_SUBSCRIPTION = "event_subscription"
    FOLDER = "folder"
    FORM = "form"
    FORM_FIELD = "form_field"
    LAYOUT = "layout"
    NOTIFICATION = "notification"
    OPTION = "option"
    PROPERTY = "property"
    RELATIONSHIP = "relationship"
    RELATIONSHIP_KIND = "relationship_kind"
    SPACE = "space"
    STATUS = "status"
    TASK = "task"
    TASK_DOC_RELATIONSHIP = "task_doc_relationship"
    TASK_KIND = "task_kind"
    TASK_LINK = "task_link"
    TENANT = "tenant"
    USER = "user"
    USER_DARTBOARD_LAYOUT = "user_dartboard_layout"
    VIEW = "view"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
