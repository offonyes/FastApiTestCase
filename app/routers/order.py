from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.order import get_orders, get_order, create_order, update_order
from app.schemas.order import OrderCreate, OrderUpdate, OrderResponse
from app.models.database import get_async_session

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)


@router.get("/", response_model=List[OrderResponse])
async def read_orders(session: AsyncSession = Depends(get_async_session)):
    orders = await get_orders(session)
    return orders


@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order_endpoint(order_in: OrderCreate, session: AsyncSession = Depends(get_async_session)):
    return await create_order(session, order_in)


@router.get("/{order_id}/", response_model=OrderResponse)
async def read_order(order_id: int, session: AsyncSession = Depends(get_async_session)):
    order = await get_order(session, order_id)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order


@router.put("/{order_id}/", response_model=OrderResponse)
async def update_order_endpoint(order_id: int, order_in: OrderUpdate, session: AsyncSession = Depends(get_async_session)):
    order = await get_order(session, order_id)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return await update_order(session, order, order_in)

