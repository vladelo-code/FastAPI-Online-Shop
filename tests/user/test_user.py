from httpx import AsyncClient
from httpx import ASGITransport
from ecommerce.auth.jwt import create_access_token
import pytest
from conf_test_db import app


@pytest.mark.asyncio
async def test_all_users():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as ac:
        user_access_token = create_access_token({"sub": "vladelo@gmail.com"})
        response = await ac.get("/user/", headers={'Authorization': f'Bearer {user_access_token}'})
    assert response.status_code == 200
