from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import User


async def create_user(session: AsyncSession, username: str, email: str) -> User | None:
    user_exist = await get_user(session, username)
    if user_exist:
        return user_exist

    user = User(username=username, email=email)
    session.add(user)
    await session.commit()
    return user


async def get_user(session: AsyncSession, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    res = await session.execute(stmt)
    return res.scalars().first()


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    stmt = select(User).where(User.id == user_id)
    res = await session.execute(stmt)
    return res.scalars().first()


async def get_all_users(session: AsyncSession) -> list[User]:
    stmt = select(User)
    res = await session.execute(stmt)
    return res.scalars().all()
