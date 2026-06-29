from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.common.database.session import SessionLocal


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session