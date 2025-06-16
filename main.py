import uvicorn
from fastapi import FastAPI

from ecommerce.auth.router import router as auth_router
from ecommerce.user.router import router as user_router
from ecommerce.products.router import router as product_router
from ecommerce.cart.router import router as cart_router
from ecommerce.orders.router import router as order_router

description = '''Полнофункциональный онлайн-магазин, построенный на современном стеке технологий. 
Проект поддерживает регистрацию пользователей, управление товарами и категориями, корзину, оформление заказов и отправку email-уведомлений. 
Реализована полноценная аутентификация, асинхронные API, фоновая отправка писем через Celery и Redis, а также покрытие тестами.
'''

app = FastAPI(title='Vladelo Online Shop',
              description=description,
              contact={
                  "name": "Vladislav Lakhtionov",
                  "url": "https://t.me/vladelo",
              },
              )

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(product_router)
app.include_router(cart_router)
app.include_router(order_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
