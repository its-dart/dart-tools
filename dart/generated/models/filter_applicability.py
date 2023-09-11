from enum import Enum


class FilterApplicability(str, Enum):
    ARE_NOT_SET = "are not set"
    CONTAIN = "contain"
    CONTAINS = "contains"
    DONT_INCLUDE = "don't include"
    EXIST = "exist"
    EXISTS = "exists"
    INCLUDE = "include"
    IS = "is"
    IS_AFTER = "is after"
    IS_BEFORE = "is before"
    IS_BETWEEN = "is between"
    IS_NOT = "is not"
    IS_NOT_SET = "is not set"

    def __str__(self) -> str:
        return str(self.value)
