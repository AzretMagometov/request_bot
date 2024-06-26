from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import select, insert
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base, async_session_maker


class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=True)


class SUsers(BaseModel):
    id: int
    username: str
    created: datetime
    updated: datetime

    class Config:
        from_attributes = True


class UsersDAO:
    @staticmethod
    async def get(**filter_by) -> list[SUsers]:
        async with async_session_maker() as session:
            query = select(Users).filter_by(**filter_by)
            res = await session.execute(query)
            return res.scalars().all()

    @staticmethod
    async def add(id, username=None):
        async with async_session_maker() as session:
            query = insert(Users).values(id=id, username=username)
            await session.execute(query)
            await session.commit()
