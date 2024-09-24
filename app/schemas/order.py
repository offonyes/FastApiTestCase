from datetime import datetime
from typing import List

from pydantic import BaseModel

from app.models.order import OrderStatus
from app.schemas.orderitem import OrderItemCreate, OrderItemResponse


class OrderBase(BaseModel):
    orderitems: List[OrderItemCreate]


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    status: OrderStatus


class OrderResponse(BaseModel):
    id: int
    created_at: datetime
    status: str
    orderitems: List[OrderItemResponse]

    class ConfigDict:
        from_attributes = True
