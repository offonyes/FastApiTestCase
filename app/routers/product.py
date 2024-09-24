from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.product import get_products, create_product, get_product, delete_product, update_product
from app.schemas.product import ProductResponse, ProductCreate, ProductUpdate
from app.models.database import get_async_session

router = APIRouter(
    prefix="/product",
    tags=["Product"],
)


@router.get("/", response_model=list[ProductResponse])
async def read_products(session: AsyncSession = Depends(get_async_session)):
    return await get_products(session)


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product_endpoint(product_in: ProductCreate, session: AsyncSession = Depends(get_async_session)):
    return await create_product(session, product_in)


@router.get("/{product_id}/", response_model=ProductResponse)
async def read_product(product_id: int, session: AsyncSession = Depends(get_async_session)):
    product = await get_product(session, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


@router.put("/{product_id}/", response_model=ProductResponse)
async def update_product_endpoint(product_id: int, product_in: ProductUpdate, session: AsyncSession = Depends(get_async_session)):
    product = await get_product(session, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    product = await update_product(session, product, product_in)
    return product


@router.delete("/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product_endpoint(product_id: int, session: AsyncSession = Depends(get_async_session)):
    product = await get_product(session, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    await delete_product(session, product)

