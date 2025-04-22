from enum import Enum


class ListDocsOItem(str, Enum):
    CREATED_AT = "created_at"
    ORDER = "order"
    TITLE = "title"
    UPDATED_AT = "updated_at"
    VALUE_0 = "-created_at"
    VALUE_1 = "-order"
    VALUE_2 = "-title"
    VALUE_3 = "-updated_at"

    def __str__(self) -> str:
        return str(self.value)
