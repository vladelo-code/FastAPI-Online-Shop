import pytest
from faker import Faker
from httpx import AsyncClient
from httpx import ASGITransport

from conf_test_db import app


@pytest.mark.asyncio
async def test_registration():
    fake = Faker()
    data = {
        "name": fake.name(),
        "email": fake.email(),
        "password": fake.password()
    }

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as ac:
        response = await ac.post("/user/", json=data)

    assert response.status_code == 201
