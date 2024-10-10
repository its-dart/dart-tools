from enum import Enum


class ChartType(str, Enum):
    BAR = "bar"
    BURNUP = "burnup"
    LINE = "line"
    NUMBER = "number"
    PIE = "pie"
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)
