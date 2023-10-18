from enum import Enum


class DocSourceType(str, Enum):
    APPLICATION = "Application"
    ONBOARDING = "Onboarding"
    RECOMMENDATION = "Recommendation"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
