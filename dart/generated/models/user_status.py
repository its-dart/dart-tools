from enum import Enum


class UserStatus(str, Enum):
    ACTIVE = "Active"
    DEACTIVATED = "Deactivated"
    INVITED = "Invited"
    PENDINGEMAILVERIFICATION = "PendingEmailVerification"
    PENDINGSUBSCRIPTIONUPGRADE = "PendingSubscriptionUpgrade"

    def __str__(self) -> str:
        return str(self.value)
