from fastapi import FastAPI

from app.routers.product import router as product_router
from app.routers.order import router as order_router

app = FastAPI(
    title="Warehouse",
    description="Warehouse Api",
    version="0.1.0",
    contact={
        "name": "By Dimitri Katranidis",
        "url": "https://t.me/dimitri_katranidis",
    },
)


app.include_router(product_router)
app.include_router(order_router)



