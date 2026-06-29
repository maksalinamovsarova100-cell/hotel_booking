from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr
from pydantic import Field

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