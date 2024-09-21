from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_async_engine(
    # "sqlite+aiosqlite:///database.sqlite3",
    "postgresql+asyncpg://postgres:adminGrisha@localhost:5432/FastApi"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)
# URL_DATABASE = "sqlite+aiosqlite:///database.sqlite3"

# engine = create_engine(URL_DATABASE)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()


class BaseModel(DeclarativeBase):
    pass
