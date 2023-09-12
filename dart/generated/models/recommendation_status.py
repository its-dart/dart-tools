from enum import Enum


class RecommendationStatus(str, Enum):
    ACCEPTED = "Accepted"
    DECLINED = "Declined"

    def __str__(self) -> str:
        return str(self.value)
