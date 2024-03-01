from enum import Enum


class EventActor(str, Enum):
    AN_EMAIL_USER = "An email user"
    A_FORM_USER = "A form user"
    DART_AI = "Dart AI"
    DART_DUE_DATE_BOT = "Dart due date bot"
    DART_GITHUB_BOT = "Dart GitHub bot"
    DART_METRICS_BOT = "Dart metrics bot"
    DART_RECURRING_TASK_BOT = "Dart recurring task bot"
    DART_REMINDER_BOT = "Dart reminder bot"
    DART_REPORT_BOT = "Dart report bot"
    DART_SLACK_BOT = "Dart Slack bot"
    STRIPE_WEBHOOK = "Stripe webhook"

    def __str__(self) -> str:
        return str(self.value)
