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


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: int
    quantity: int

    class Config:
        from_attributes = True

