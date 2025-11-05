from pydantic import BaseModel


class User(BaseModel):
    username: str


class UserRead(User):
    id: int
