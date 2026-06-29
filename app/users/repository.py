from app.common.repositories.base import BaseRepository
from app.users.models import User


class UserRepository(BaseRepository[User]):
    model = User

    async def get_by_email(self, email: str) -> User | None:
        return await self.get(email=email)

    async def get_by_username(self, username: str) -> User | None:
        return await self.get(username=username)