from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.common.database.base import Base
from app.core.config import settings

DATABASE_URL = settings.database_url


engine = create_async_engine(
    DATABASE_URL,
    echo=settings.DATABASE_ECHO,
    pool_pre_ping=True,
)

SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
)


async def get_db():
    async with SessionLocal() as session:
        yield session