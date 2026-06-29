from typing import Any
from typing import Generic
from typing import TypeVar

from sqlalchemy import delete
from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy import update

from sqlalchemy.ext.asyncio import AsyncSession

from app.common.database.base import Base


Model = TypeVar("Model", bound=Base)


class BaseRepository(Generic[Model]):

    model: type[Model]

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, **filters) -> Model | None:
        stmt = select(self.model).filter_by(**filters)

        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_all(self) -> list[Model]:
        stmt = select(self.model)

        result = await self.session.execute(stmt)

        return list(result.scalars().all())

    async def create(self, **values) -> Model:
        obj = self.model(**values)

        self.session.add(obj)

        await self.session.flush()

        return obj

    async def delete(self, **filters) -> None:
        stmt = delete(self.model).filter_by(**filters)

        await self.session.execute(stmt)

    async def exists(self, **filters) -> bool:
        stmt = (
            select(func.count())
            .select_from(self.model)
            .filter_by(**filters)
        )

        result = await self.session.execute(stmt)

        return result.scalar() > 0