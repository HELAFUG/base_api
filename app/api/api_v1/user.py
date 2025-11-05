from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from api.api_v1.utils.send_welcome_email import send_welcome_email
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


@router.post("/")
async def create_user(
    session: Annotated[AsyncSession, Depends(db_helper.get_session)],
    user: User,
    background_tasks: BackgroundTasks,
):
    new_user = await user_crud.create_user(session, user.username, user.email)

    user = await user_crud.get_user(session, user.username)

    background_tasks.add_task(send_welcome_email, user.id)
    return new_user


@router.get("/all")
async def get_all_users(
    session: Annotated[AsyncSession, Depends(db_helper.get_session)], username: str
):
    if username != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")
    return await user_crud.get_all_users(session)
