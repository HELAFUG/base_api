from asyncio import sleep
from api.api_v1.crud.user import get_user_by_id
from core.models import db_helper
from .send_email import send_email


async def send_welcome_email(user_id: int) -> None:
    async with db_helper.session_factory() as session:
        user = await get_user_by_id(user_id=user_id, session=session)
    await sleep(5)
    await send_email(
        recipient=user.email,
        sub="new registration on site",
        body="hello man, welcome to site",
    )
