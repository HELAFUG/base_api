from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from os import getenv


class DBSettings(BaseModel):
    url: str = getenv(
        "DB_URL", "postgresql+asyncpg://postgres:qwerty@localhost:5431/base_api_db"
    )
    echo: bool = False
    max_overflow: int = 10


class APIV1(BaseModel):
    prefix: str = "/v1"


class APISettings(BaseModel):
    prefix: str = "/api"
    v1: APIV1 = APIV1()


class Settings(BaseModel):
    db: DBSettings = DBSettings()
    api: APISettings = APISettings()


settings = Settings()
