from datetime import datetime

from sqlalchemy import func, DateTime
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

from config import create_settings
settings = create_settings()

engine = create_async_engine(settings.DB_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    created: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now())
    updated: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
