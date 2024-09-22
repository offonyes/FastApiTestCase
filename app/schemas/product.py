from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str
    price: int
    quantity: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductCreate):
    pass


class ProductOut(ProductBase):
    id: int

