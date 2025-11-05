from .send_email import send_email
from core.models import User
from api.api_v1.crud.user import get_user_dy_id
from asyncio import sleep


async def send_welcome_email(user_id: int) -> None:
    user = await get_user_dy_id(user_id)
    await sleep(5)
    await send_email(
        recipient=user.email,
        sub="new registration on site",
        body="hello man, welcome to site",
    )
