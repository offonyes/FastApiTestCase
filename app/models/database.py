from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from app.config import URL_DATABASE

engine = create_async_engine(URL_DATABASE)

new_session = async_sessionmaker(engine, expire_on_commit=False)


class BaseModel(DeclarativeBase):
    pass
