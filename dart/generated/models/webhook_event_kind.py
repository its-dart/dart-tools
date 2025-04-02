from enum import Enum


class WebhookEventKind(str, Enum):
    COMMENT_CREATED = "comment.created"
    DOC_CREATED = "doc.created"
    DOC_DELETED = "doc.deleted"
    DOC_UPDATED = "doc.updated"
    TASK_CREATED = "task.created"
    TASK_DELETED = "task.deleted"
    TASK_UPDATED = "task.updated"

    def __str__(self) -> str:
        return str(self.value)
