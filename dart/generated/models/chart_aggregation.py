from enum import Enum


class ChartAggregation(str, Enum):
    AVG = "avg"
    COUNT = "count"
    SUM = "sum"

    def __str__(self) -> str:
        return str(self.value)
