import datetime
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import BigInteger, String, DateTime
from sqlalchemy import func


class BaseModel(AsyncAttrs, DeclarativeBase):
    pass


class User(BaseModel):
    __tablename__ = "Users"

    telegram_id: Mapped[int] = mapped_column(BigInteger,
                                             primary_key=True,
                                             unique=True,
                                             nullable=False,
                                             index=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime,
                                                          nullable=False,
                                                          server_default=func.now())
    fullname: Mapped[str | None] = mapped_column(String(200), nullable=True)
    nickname: Mapped[str | None] = mapped_column(String(200), nullable=True)

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.telegram_id=}; {self.fullname=}; {self.nickname=})"
