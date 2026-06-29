from app.users.repository import UserRepository
from app.users.exceptions import (
    EmailAlreadyExists,
    UsernameAlreadyExists,
)

class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def create_user(
        self,
        email: str,
        username: str,
        hashed_password: str,
    ):

        if await self.repository.exists(email=email):
            raise EmailAlreadyExists()

        if await self.repository.exists(username=username):
            raise UsernameAlreadyExists()

        return await self.repository.create(
            email=email,
            username=username,
            hashed_password=hashed_password,
        )