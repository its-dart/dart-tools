from enum import Enum


class EventActor(str, Enum):
    AN_EMAIL_USER = "An email user"
    A_FORM_USER = "A form user"
    DART_AI = "Dart AI"
    DART_DUE_DATE_BOT = "Dart Due Date Bot"
    DART_GITHUB_BOT = "Dart GitHub Bot"
    DART_METRICS_BOT = "Dart Metrics Bot"
    DART_RECURRING_TASK_BOT = "Dart Recurring Task Bot"
    DART_REMINDER_BOT = "Dart Reminder Bot"
    DART_REPORT_BOT = "Dart Report Bot"
    DART_SLACK_BOT = "Dart Slack Bot"
    DART_SPRINT_BOT = "Dart Sprint Bot"
    STRIPE_WEBHOOK = "Stripe webhook"

    def __str__(self) -> str:
        return str(self.value)
