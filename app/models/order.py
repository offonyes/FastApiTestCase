import datetime
import enum
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.models.database import BaseModel

if TYPE_CHECKING:
    from app.models.orderitem import OrdetItemModel

class OrderStatus(enum.Enum):
    InProgress = "In Progress"
    Sent = "Sent"
    Delivered = "Delivered"


class OrderModel(BaseModel):
    __tablename__ = 'order'

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    status: Mapped[OrderStatus]

    orderitems: Mapped[list["OrderItemModel"]] = relationship(back_populates="order")
