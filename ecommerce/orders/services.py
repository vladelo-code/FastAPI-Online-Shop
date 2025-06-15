from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ecommerce.cart.models import Cart, CartItems
from ecommerce.orders.models import Order, OrderDetails
from ecommerce.user.models import User
from ecommerce.orders import tasks


async def initiate_order(current_user, database: Session):
    """
    Инициирует создание нового заказа для текущего пользователя.

    Проверяет наличие пользователя и его корзины. Если корзина отсутствует,
    создаётся новая. Подсчитывает общую сумму заказа, создаёт запись заказа
    и детали заказа для каждого товара из корзины. Отправляет email с подтверждением
    заказа асинхронно через Celery. Очищает корзину после создания заказа.

    :param current_user: Объект текущего аутентифицированного пользователя с полем email.
    :param database: Сессия SQLAlchemy для работы с БД.
    :raises HTTPException: Если пользователь или товары в корзине не найдены.
    :return: Объект созданного заказа (Order).
    """
    user_info = database.query(User).filter(User.email == current_user.email).first()
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    cart = database.query(Cart).filter(Cart.user_id == user_info.id).first()
    if not cart:
        cart = Cart(user_id=user_info.id)
        database.add(cart)
        database.commit()
        database.refresh(cart)

    cart_items_objects = database.query(CartItems).filter(CartItems.cart_id == cart.id)
    if not cart_items_objects.count():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No items found in the cart!")

    total_amount: float = 0.0
    for item in cart_items_objects:
        total_amount += item.products.price

    new_order = Order(order_amount=total_amount, customer_id=user_info.id,
                      shipping_address='Москва, улица Тверская, дом 1')
    database.add(new_order)
    database.commit()
    database.refresh(new_order)

    bulk_order_details_objects = list()
    for item in cart_items_objects:
        new_order_details = OrderDetails(order_id=new_order.id, product_id=item.products.id)
        bulk_order_details_objects.append(new_order_details)

    database.bulk_save_objects(bulk_order_details_objects)
    database.commit()

    # Отправка Email покупателю об успешном заказе
    tasks.send_order_confirmation.delay(current_user.email)

    # Очистка корзины (удаления всех позиций из нее)
    database.query(CartItems).filter(CartItems.cart_id == cart.id).delete()
    database.commit()

    return new_order


async def get_order_listing(current_user, database: Session) -> List[Order]:
    """
    Получает список всех заказов текущего пользователя.

    :param current_user: Объект текущего аутентифицированного пользователя с полем email.
    :param database: Сессия SQLAlchemy для работы с БД.
    :return: Список заказов (List[Order]) пользователя.
    """
    user_info = database.query(User).filter(User.email == current_user.email).first()
    orders = database.query(Order).filter(Order.customer_id == user_info.id).all()
    return orders
