from enum import StrEnum


class UserRole(StrEnum):
    CUSTOMER = "customer"
    HOST = "host"
    ADMIN = "admin"