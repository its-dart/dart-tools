from enum import Enum


class RelationshipKindKind(str, Enum):
    BLOCKS = "Blocks"
    CUSTOM = "Custom"
    DUPLICATES = "Duplicates"
    PARENT_OF = "Parent Of"
    RELATES_TO = "Relates To"

    def __str__(self) -> str:
        return str(self.value)
