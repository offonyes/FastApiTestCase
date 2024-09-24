from typing import List, Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result

from fastapi import HTTPException, Depends
from sqlalchemy.orm import joinedload, selectinload

from app.models.order import OrderModel, OrderStatus
from app.models.orderitem import OrderItemModel
from app.models.product import ProductModel
from app.schemas.order import OrderCreate, OrderUpdate
from app.schemas.orderitem import OrderItemCreate


async def get_orders(session: AsyncSession):
    stmt = select(OrderModel).options(selectinload(OrderModel.orderitems))
    result = await session.execute(stmt)
    orders = result.scalars().all()
    return orders


async def get_order(session: AsyncSession, order_id: int) -> OrderModel | None:
    return await session.get(OrderModel, order_id)


async def create_order(session: AsyncSession, order_in: OrderCreate) -> OrderModel:
    for item in order_in.orderitems:
        product = await session.get(ProductModel, item.product_id)
        if product is None or product.quantity < item.quantity:
            raise HTTPException(status_code=400, detail=f"Not enough product with ID {item.product_id}")

    new_order = OrderModel(status=OrderStatus.InProgress)
    session.add(new_order)
    await session.commit()
    await session.refresh(new_order)

    for item in order_in.orderitems:
        new_order_item = OrderItemModel(order_id=new_order.id, product_id=item.product_id, quantity=item.quantity)
        session.add(new_order_item)
        product.quantity -= item.quantity

    await session.commit()
    await session.refresh(new_order)
    return new_order


async def update_order(session: AsyncSession, order: OrderModel, order_in: OrderUpdate) -> OrderModel:
    order.status = order_in.status
    await session.commit()
    await session.refresh(order)
    return order
