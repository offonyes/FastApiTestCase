import pytest

from tests.conftest import test_client


@pytest.mark.asyncio(loop_scope='session')
async def test_create_product(test_client):
    new_product = {
        "name": "Some name",
        "description": "eaeawea",
        "price": 10,
        "quantity": 10,
    }
    response = await test_client.post("/products/", json=new_product)
    assert response.status_code == 201
    res = response.json()
    del res["id"]
    assert res == new_product


@pytest.mark.asyncio(loop_scope='session')
async def test_get_all_products(test_client):
    response = await test_client.get('/products/')
    assert response.status_code == 200
    print(response.json())


@pytest.mark.asyncio(loop_scope='session')
async def test_get_product(test_client):
    response = await test_client.get('/products/1/')
    assert response.status_code == 200
    print(response.json())


@pytest.mark.asyncio(loop_scope='session')
async def test_update_product(test_client):
    new_product = {
        "name": "Some name NEW",
        "description": "eaeaeaweawea",
        "price": 101,
        "quantity": 101,
    }
    response = await test_client.put('/products/1/', json=new_product)
    assert response.status_code == 200
    res = response.json()
    del res["id"]
    assert res == new_product


@pytest.mark.asyncio(loop_scope='session')
async def test_delete_product(test_client):
    response = await test_client.delete('/products/1/')
    assert response.status_code == 204
    response = await test_client.get('/products/1/')
    assert response.status_code == 404

