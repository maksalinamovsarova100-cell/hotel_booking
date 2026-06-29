from app.auth.jwt import create_access_token
from app.auth.security import hash_password, verify_password

from app.users.exceptions import (
    EmailAlreadyExists,
    InvalidCredentials,
    UsernameAlreadyExists,
)

from app.users.repository import UserRepository


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def register(
        self,
        email: str,
        username: str,
        password: str,
    ):
        # Проверка email
        if await self.repository.exists(email=email):
            raise EmailAlreadyExists()

        # Проверка username
        if await self.repository.exists(username=username):
            raise UsernameAlreadyExists()

        # Хешируем пароль
        hashed_password = hash_password(password)

        # Создаем пользователя
        user = await self.repository.create(
            email=email,
            username=username,
            hashed_password=hashed_password,
        )

        return user

    async def login(
        self,
        email: str,
        password: str,
    ) -> str:

        user = await self.repository.get_by_email(email)

        if user is None:
            raise InvalidCredentials()

        if not verify_password(
            password=password,
            hashed_password=user.hashed_password,
        ):
            raise InvalidCredentials()

        access_token = create_access_token(
            user_id=user.id,
            email=user.email,
            role=user.role.value,
        )

        return access_token