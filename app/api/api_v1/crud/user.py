from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import User


async def create_user(session: AsyncSession, username: str) -> User | None:
    user_exist = await get_user(session, username)
    if user_exist:
        return user_exist

    user = User(username=username)
    session.add(user)
    await session.commit()
    return user


async def get_user(session: AsyncSession, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    res = await session.execute(stmt)
    return res.scalars().first()
