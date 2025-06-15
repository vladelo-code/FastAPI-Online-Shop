import pytest
from httpx import AsyncClient, ASGITransport

from ecommerce.auth.jwt import create_access_token
from conf_test_db import app
from tests.shared.info import category_info, product_info


@pytest.mark.asyncio
async def test_order_processing(mocker):
    mocker.patch('ecommerce.orders.tasks.send_email', return_value=True)
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as ac:
        user_access_token = create_access_token({"sub": "vladelo@gmail.com"})
        category_obj = await category_info()
        product_id = await product_info(category_obj)

        cart_response = await ac.post(f"/cart/add",
                                     params={'product_id': product_id},
                                     headers={'Authorization': f'Bearer {user_access_token}'})

        order_response = await ac.post("/orders/", headers={'Authorization': f'Bearer {user_access_token}'})

    assert cart_response.status_code == 201
    assert order_response.status_code == 201


@pytest.mark.asyncio
async def test_order_listing():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as ac:
        user_access_token = create_access_token({"sub": "vladelo@gmail.com"})
        response = await ac.get("/orders/", headers={'Authorization': f'Bearer {user_access_token}'})

    assert response.status_code == 200
