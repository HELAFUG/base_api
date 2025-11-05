from sqlalchemy.orm import Mapped, mapped_column
from .mixins import IdIntMixin
from .base import Base


class User(IdIntMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)
