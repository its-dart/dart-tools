from enum import Enum


class SummaryStatisticKind(str, Enum):
    COMPLETEDPERCENT = "CompletedPercent"
    COMPLETEDPERCENTPOINTS = "CompletedPercentPoints"
    INCOMPLETECOUNT = "IncompleteCount"
    INCOMPLETECOUNTPOINTS = "IncompleteCountPoints"
    NONE = "None"
    TOTALCOUNT = "TotalCount"
    TOTALCOUNTPOINTS = "TotalCountPoints"

    def __str__(self) -> str:
        return str(self.value)
