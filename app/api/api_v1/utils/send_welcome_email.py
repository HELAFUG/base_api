from .send_email import send_email
from core.models import User
from asyncio import sleep


async def send_welcome_email(user: User):
    await sleep(5)
    await send_email(
        recipient=user.email,
        sub="new registration on site",
        body="hello man, welcome to site",
    )
