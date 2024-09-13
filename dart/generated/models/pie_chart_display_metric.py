from enum import Enum


class PieChartDisplayMetric(str, Enum):
    COUNT = "count"
    PCT = "pct"

    def __str__(self) -> str:
        return str(self.value)
