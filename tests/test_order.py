import pytest

from tests.conftest import test_client


@pytest.mark.asyncio(loop_scope='session')
async def test_create_order(test_client):
    new_product = {
        "name": "Some name",
        "description": "eaeawea",
        "price": 10,
        "quantity": 10,
    }
    response_product = await test_client.post("/products/", json=new_product)
    assert response_product.status_code == 201

    new_order = {
            "orderitems": [
                {
                    "product_id": response_product.json()["id"],
                    "quantity": 1
                }
            ]
        }

    response = await test_client.post("/orders/", json=new_order)
    assert response.status_code == 201
    print(response.json())


@pytest.mark.asyncio(loop_scope='session')
async def test_get_orders(test_client):
    response = await test_client.get("/orders/")
    assert response.status_code == 200
    print(response.json())


@pytest.mark.asyncio(loop_scope='session')
async def test_get_order(test_client):
    response = await test_client.get("/orders/1/")
    assert response.status_code == 200
    print(response.json())


@pytest.mark.asyncio(loop_scope='session')
async def test_update_order(test_client):
    new_product = {
        "status": "Delivered"
    }
    response = await test_client.put("/orders/3/", json=new_product)
    assert response.status_code == 200
    print(response.json())
