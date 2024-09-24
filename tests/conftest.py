import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.fixture(scope='session')
async def test_client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url='http://localhost') as ac:
        yield ac
        