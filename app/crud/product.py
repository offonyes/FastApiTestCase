from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from app.models.product import ProductModel
from app.schemas.product import ProductCreate, ProductUpdate


async def get_products(session: AsyncSession):
    stmt = select(ProductModel).order_by(ProductModel.id)
    result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, product_id: int):
    return await session.get(ProductModel, product_id)


async def create_product(session: AsyncSession, product_in: ProductCreate):
    product = ProductModel(**product_in.model_dump())
    session.add(product)
    await session.commit()
    return product


async def update_product(session: AsyncSession, product: ProductModel, product_update: ProductUpdate,
                         partial: bool = False):
    for name, value in product_update.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)
    await session.commit()
    return product


async def delete_product(session: AsyncSession, product: ProductModel):
    await session.delete(product)
    await session.commit()
