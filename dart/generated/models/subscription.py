from enum import Enum


class Subscription(str, Enum):
    PERSONAL = "Personal"
    PREMIUM = "Premium"

    def __str__(self) -> str:
        return str(self.value)
