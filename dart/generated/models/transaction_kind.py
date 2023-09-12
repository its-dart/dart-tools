from enum import Enum


class TransactionKind(str, Enum):
    COMMENT_CREATE = "comment_create"
    COMMENT_DELETE = "comment_delete"
    COMMENT_REACTION_CREATE = "comment_reaction_create"
    COMMENT_REACTION_DELETE = "comment_reaction_delete"
    COMMENT_UPDATE = "comment_update"
    CYCLE_ROLLOVER = "cycle_rollover"
    DARTBOARD_CREATE = "dartboard_create"
    DARTBOARD_DELETE = "dartboard_delete"
    DARTBOARD_UPDATE = "dartboard_update"
    DOC_CREATE = "doc_create"
    DOC_DELETE = "doc_delete"
    DOC_UPDATE = "doc_update"
    EVENT_CREATE = "event_create"
    FOLDER_CREATE = "folder_create"
    FOLDER_DELETE = "folder_delete"
    FOLDER_UPDATE = "folder_update"
    LAYOUT_CREATE = "layout_create"
    LAYOUT_DELETE = "layout_delete"
    LAYOUT_UPDATE = "layout_update"
    RELATIONSHIP_CREATE = "relationship_create"
    RELATIONSHIP_DELETE = "relationship_delete"
    RELATIONSHIP_UPDATE = "relationship_update"
    SPACE_CREATE = "space_create"
    SPACE_DELETE = "space_delete"
    SPACE_UPDATE_OTHER = "space_update_other"
    SPACE_UPDATE_PERMS = "space_update_perms"
    STATUS_CREATE = "status_create"
    STATUS_DELETE = "status_delete"
    STATUS_UPDATE = "status_update"
    TAG_CREATE = "tag_create"
    TAG_DELETE = "tag_delete"
    TAG_UPDATE = "tag_update"
    TASK_COMPLETE = "task_complete"
    TASK_CREATE = "task_create"
    TASK_DELETE = "task_delete"
    TASK_DOC_RELATIONSHIP_CREATE = "task_doc_relationship_create"
    TASK_DOC_RELATIONSHIP_DELETE = "task_doc_relationship_delete"
    TASK_RENAME = "task_rename"
    TASK_UPDATE = "task_update"
    TENANT_UPDATE = "tenant_update"
    USER_DARTBOARD_LAYOUT_CREATE = "user_dartboard_layout_create"
    USER_DARTBOARD_LAYOUT_DELETE = "user_dartboard_layout_delete"
    USER_DARTBOARD_LAYOUT_UPDATE = "user_dartboard_layout_update"
    USER_UPDATE = "user_update"
    VIEW_CREATE = "view_create"
    VIEW_DELETE = "view_delete"
    VIEW_UPDATE = "view_update"

    def __str__(self) -> str:
        return str(self.value)
