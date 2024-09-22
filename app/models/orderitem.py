from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer

from app.models.database import BaseModel

if TYPE_CHECKING:
    from app.models.order import OrderModel


class OrderItemModel(BaseModel):
    __tablename__ = 'orderitem'

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey('order.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
    quantity: Mapped[int]

    order: Mapped["OrderModel"] = relationship(back_populates="orderitems")