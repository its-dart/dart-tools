from enum import Enum


class NumberChartAggregation(str, Enum):
    AVG = "avg"
    COUNT = "count"
    SUM = "sum"

    def __str__(self) -> str:
        return str(self.value)
