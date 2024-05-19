from datetime import date
from pydantic import BaseModel
from sqlalchemy import select, insert, update, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base, async_session_maker


class Schedule(Base):
    __tablename__ = "schedule"
    id: Mapped[int] = mapped_column(primary_key=True)
    topic: Mapped[str] = mapped_column(nullable=True)
    time: Mapped[date] = mapped_column(nullable=False)
    client: Mapped[int] = mapped_column(ForeignKey("users.id"))
    is_reserved: Mapped[bool] = mapped_column(nullable=False, default=False)


class SSchedule(BaseModel):
    id: int
    topic: str
    time: date
    client: int
    is_reserved: bool

    class Config:
        from_attributes = True


class ScheduleDAO:
    @staticmethod
    async def get(**filter_by) -> list[SSchedule]:
        async with async_session_maker() as session:
            query = select(Schedule).filter_by(**filter_by)
            res = await session.execute(query)
            return res.scalars().all()

    @staticmethod
    async def add(tg_id, username=None):
        async with async_session_maker() as session:
            query = insert(Schedule).values(tg_id=tg_id, username=username)
            await session.execute(query)
            await session.commit()

    @staticmethod
    async def update(id, **kwargs):
        async with async_session_maker() as session:
            query = update(Schedule).where(Schedule.id == id).values(**kwargs)
            await session.execute(query)
            await session.commit()
