from enum import Enum


class TaskSourceType(str, Enum):
    API = "API"
    APPBOARD = "AppBoard"
    APPENTER = "AppEnter"
    APPLICATION = "Application"
    APPPASTE = "AppPaste"
    APPQUICKADD = "AppQuickAdd"
    APPRELATIONSHIP = "AppRelationship"
    APPREPLICATE = "AppReplicate"
    APPROADMAPLIST = "AppRoadmapList"
    APPROADMAPTIMELINE = "AppRoadmapTimeline"
    APPSUBTASK = "AppSubtask"
    APPTCM = "AppTcm"
    CHATGPT = "ChatGPT"
    CLI = "CLI"
    EMAIL = "Email"
    IMPORT = "Import"
    ONBOARDING = "Onboarding"
    RECOMMENDATION = "Recommendation"
    RECURRENCE = "Recurrence"
    SLACK = "Slack"
    TEMPLATE = "Template"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
