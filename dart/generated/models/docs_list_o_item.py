from enum import Enum


class DocsListOItem(str, Enum):
    RECENT = "recent"
    TITLE = "title"
    VALUE_0 = "-recent"
    VALUE_1 = "-title"

    def __str__(self) -> str:
        return str(self.value)
