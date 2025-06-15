from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends

from ecommerce import db
from ecommerce.cart import shema
from ecommerce.products.models import Product
from ecommerce.user.models import User
from ecommerce.cart.models import Cart, CartItems


async def add_items(cart_id: int, product_id: int, database: Session = Depends(db.get_db)) -> None:
    """
    Добавляет товар в корзину.

    :param cart_id: ID корзины, в которую добавляется товар.
    :param product_id: ID добавляемого товара.
    :param database: Сессия базы данных.
    """
    cart_items = CartItems(cart_id=cart_id, product_id=product_id)
    database.add(cart_items)
    database.commit()
    database.refresh(cart_items)


async def add_product_to_cart(product_id: int, current_user, database: Session = Depends(db.get_db)) -> dict:
    """
    Добавляет товар в корзину текущего пользователя.
    Если корзина отсутствует, создаётся новая.

    :param product_id: ID добавляемого товара.
    :param current_user: Текущий аутентифицированный пользователь с полем email.
    :param database: Сессия базы данных.
    :raises HTTPException: При отсутствии товара или отсутствии доступного количества.
    :return: Словарь со статусом успешного добавления.
    """
    product_info = database.get(Product, product_id)

    if not product_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found!")

    if product_info.quantity < 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item out of stock!")

    user_info = database.query(User).filter(User.email == current_user.email).first()

    cart_info = database.query(Cart).filter(Cart.user_id == user_info.id).first()

    if not cart_info:
        new_cart = Cart(user_id=user_info.id)
        database.add(new_cart)
        database.commit()
        database.refresh(new_cart)
        await add_items(new_cart.id, product_info.id, database)
    else:
        await add_items(cart_info.id, product_info.id, database)

    return {"status": "Item added to cart!"}


async def get_all_items(current_user, database: Session) -> shema.ShowCart:
    """
    Получает корзину текущего пользователя.

    :param current_user: Текущий аутентифицированный пользователь с полем email.
    :param database: Сессия базы данных.
    :return: Объект корзины пользователя.
    """adding docstring in defs in orders module
    user_info = database.query(User).filter(User.email == current_user.email).first()
    cart = database.query(Cart).filter(Cart.user_id == user_info.id).first()
    return cart


async def remove_cart_item(cart_item_id: int, current_user, database: Session) -> None:
    """
    Удаляет товар из корзины текущего пользователя.

    :param cart_item_id: ID позиции в корзине, которую нужно удалить.
    :param current_user: Текущий аутентифицированный пользователь с полем email.
    :param database: Сессия базы данных.
    """
    user_info = database.query(User).filter(User.email == current_user.email).first()
    cart_id = database.query(Cart).filter(User.id == user_info.id).first()
    database.query(CartItems).filter(CartItems.id == cart_item_id, CartItems.cart_id == cart_id.id).delete()
    database.commit()
    return None
