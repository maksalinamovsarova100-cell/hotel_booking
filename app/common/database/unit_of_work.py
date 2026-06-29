from sqlalchemy.ext.asyncio import AsyncSession

from app.common.database.session import SessionLocal


class UnitOfWork:
    def __init__(self):
        self.session: AsyncSession | None = None

    async def __aenter__(self):
        self.session = SessionLocal()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
        else:
            await self.commit()

        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()