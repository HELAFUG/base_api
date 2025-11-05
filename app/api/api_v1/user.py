from typing import Annotated
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from core.schemas.user import User, UserRead
from .crud import user as user_crud


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=UserRead)
async def get_user(
    session: Annotated[AsyncSession, Depends(db_helper.get_session)],
    username: str,
):
    user = await user_crud.get_user(session, username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserRead)
async def create_user(
    session: Annotated[AsyncSession, Depends(db_helper.get_session)],
    user: User,
):
    return await user_crud.create_user(session, user.username)
