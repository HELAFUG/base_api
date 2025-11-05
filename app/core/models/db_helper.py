from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from core.config import settings


class DBHelper:
    def __init__(self, url: str, echo: bool, max_overflow: int):
        self.engine = create_async_engine(
            url,
            echo=echo,
            max_overflow=max_overflow,
        )

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False,
        )

    async def dispose(self):
        await self.engine.dispose()

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


db_helper = DBHelper(
    url=settings.db.url,
    echo=settings.db.echo,
    max_overflow=settings.db.max_overflow,
)
