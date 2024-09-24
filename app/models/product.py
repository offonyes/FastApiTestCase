from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from app.database import BaseModel


class ProductModel(BaseModel):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), index=True)
    description: Mapped[str | None]
    price: Mapped[int]
    quantity: Mapped[int] = mapped_column(index=True)
