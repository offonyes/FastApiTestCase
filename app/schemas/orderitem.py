from pydantic import BaseModel


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int


class OrderItemResponse(BaseModel):
    product_id: int
    quantity: int

    class ConfigDict:
        from_attributes = True
