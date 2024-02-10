from enum import Enum


class DocSourceType(str, Enum):
    APPLICATION = "Application"
    CHATGPT = "ChatGPT"
    GENERATEDREPORT = "GeneratedReport"
    ONBOARDING = "Onboarding"
    RECOMMENDATION = "Recommendation"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
