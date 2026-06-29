from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr
from pydantic import Field
from pydantic import BaseModel, ConfigDict, EmailStr

from datetime import datetime
from enum import Enum


from app.users.enums import UserRole


class UserCreate(BaseModel):
    email: EmailStr

    username: str = Field(
        min_length=3,
        max_length=40,
    )

    password: str = Field(
        min_length=8,
        max_length=128,
    )

from uuid import UUID

class UserRead(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: UUID

    email: EmailStr

    username: str

    role: UserRole

    is_active: bool

    is_verified: bool


class UserRole(str, Enum):
    ADMIN = "admin"
    HOST = "host"
    CUSTOMER = "customer"


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int

    email: EmailStr

    username: str

    role: UserRole

    created_at: datetime

    updated_at: datetime