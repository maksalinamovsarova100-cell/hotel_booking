from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.service import AuthService
from app.common.database.dependencies import get_session
from app.users.repository import UserRepository


def get_auth_service(
    session: AsyncSession = Depends(get_session),
) -> AuthService:
    repository = UserRepository(session)
    return AuthService(repository)