import datetime
from typing import List

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.types import BigInteger, String, DateTime, Integer
from sqlalchemy import func, ForeignKey


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

    actions: Mapped[List["Action"]] = relationship(back_populates="user", cascade="all, delete")

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.telegram_id=}; {self.fullname=}; {self.nickname=})"


class Action(BaseModel):

    __tablename__ = "Actions"

    id: Mapped[int] = mapped_column(Integer,
                                    primary_key=True,
                                    autoincrement=True,
                                    unique=True,
                                    index=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now(),
        server_default=func.now()
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("Users.telegram_id",
                                                    ondelete="CASCADE"))
    message: Mapped[str] = mapped_column(String, nullable=False, index=True)
    details: Mapped[str | None] = mapped_column(String, nullable=True)
    user: Mapped["User"] = relationship(back_populates="actions")

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.created_at=} ; {self.user_id=} ; {self.message=} ; {self.details=})"
