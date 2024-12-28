from enum import Enum


class ChartType(str, Enum):
    BAR = "bar"
    BURN_UP = "burn-up"
    LINE = "line"
    NUMBER = "number"
    PIE = "pie"
    TABLE = "table"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
