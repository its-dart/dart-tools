from enum import Enum


class UserRole(str, Enum):
    ADMIN = "Admin"
    FINANCIAL_ADMIN = "Financial admin"
    GUEST = "Guest"
    MEMBER = "Member"
    TECHNICAL_ADMIN = "Technical admin"

    def __str__(self) -> str:
        return str(self.value)
