import pytest
from httpx import AsyncClient, ASGITransport

from conf_test_db import app


@pytest.mark.asyncio
async def test_root():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as ac:
        response = await ac.get("/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
