from enum import Enum


class UserRole(str, Enum):
    ADMIN = "Admin"
    GUEST = "Guest"
    MEMBER = "Member"

    def __str__(self) -> str:
        return str(self.value)
