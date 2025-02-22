from enum import Enum


class DocsListOItem(str, Enum):
    CREATED = "created"
    ORDER = "order"
    RECENT = "recent"
    TITLE = "title"
    VALUE_0 = "-created"
    VALUE_1 = "-order"
    VALUE_2 = "-recent"
    VALUE_3 = "-title"

    def __str__(self) -> str:
        return str(self.value)
