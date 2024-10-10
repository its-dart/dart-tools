from enum import Enum


class UserDataEntityRetrieveEntityKind(str, Enum):
    ATTACHMENTS = "attachments"
    COMMENTS = "comments"
    DARTBOARDS = "dartboards"
    DASHBOARDS = "dashboards"
    DOCS = "docs"
    FOLDERS = "folders"
    FORMS = "forms"
    FORM_FIELDS = "form-fields"
    LAYOUTS = "layouts"
    LINKS = "links"
    OPTIONS = "options"
    PROPERTIES = "properties"
    REACTIONS = "reactions"
    RELATIONSHIPS = "relationships"
    RELATIONSHIP_KINDS = "relationship-kinds"
    SPACES = "spaces"
    STATUSES = "statuses"
    TASKS = "tasks"
    TASK_DOC_RELATIONSHIPS = "task-doc-relationships"
    TASK_KINDS = "task-kinds"
    TENANTS = "tenants"
    USERS = "users"
    USER_DARTBOARD_LAYOUTS = "user-dartboard-layouts"
    VIEWS = "views"
    WEBHOOKS = "webhooks"

    def __str__(self) -> str:
        return str(self.value)
