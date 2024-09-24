from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.product import ProductModel
from app.schemas.product import ProductCreate, ProductUpdate


async def get_products(session: AsyncSession) -> List[ProductModel]:
    stmt = select(ProductModel).order_by(ProductModel.id)
    result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> ProductModel | None:
    return await session.get(ProductModel, product_id)


async def create_product(session: AsyncSession, product_in: ProductCreate) -> ProductModel:
    product = ProductModel(**product_in.model_dump())
    session.add(product)
    await session.commit()
    return product


async def update_product(session: AsyncSession, product: ProductModel, product_update: ProductUpdate,
                         partial: bool = False) -> ProductModel:
    for name, value in product_update.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)
    await session.commit()
    return product


async def delete_product(session: AsyncSession, product: ProductModel):
    await session.delete(product)
    await session.commit()
