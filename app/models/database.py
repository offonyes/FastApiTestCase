from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from contextlib import asynccontextmanager

from app.config import URL_DATABASE

engine = create_async_engine(URL_DATABASE)


# new_session = async_sessionmaker(engine, expire_on_commit=False)

async_session_maker = sessionmaker(bind=engine, class_=AsyncSession, autoflush=True, autocommit=False, expire_on_commit=False)


class BaseModel(DeclarativeBase):
    pass


async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session

