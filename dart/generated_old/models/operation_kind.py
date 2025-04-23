from enum import Enum


class OperationKind(str, Enum):
    CREATE = "create"
    DELETE = "delete"
    UPDATE = "update"
    UPDATE_LIST_ADD = "update_list_add"
    UPDATE_LIST_REMOVE = "update_list_remove"

    def __str__(self) -> str:
        return str(self.value)
