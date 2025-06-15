from typing import List
from fastapi import HTTPException

from ecommerce.products import models


async def create_new_category(request, database) -> models.Category:
    """
    Создаёт новую категорию товаров.

    :param request: Объект с полем name для новой категории.
    :param database: Сессия базы данных.
    :return: Созданная категория.
    """
    new_category = models.Category(name=request.name)
    database.add(new_category)
    database.commit()
    database.refresh(new_category)
    return new_category


async def get_all_categories(database) -> List[models.Category]:
    """
    Возвращает список всех категорий товаров.

    :param database: Сессия базы данных.
    :return: Список объектов категорий.
    """
    all_categories = database.query(models.Category).all()
    return all_categories


async def get_category_by_id(category_id, database) -> models.Category:
    """
    Возвращает категорию по её ID.

    :param category_id: Идентификатор категории.
    :param database: Сессия базы данных.
    :raises HTTPException: Если категория не найдена.
    :return: Объект категории.
    """
    category_info = database.get(models.Category, category_id)
    if not category_info:
        raise HTTPException(status_code=404, detail="Category not found!")
    return category_info


async def delete_category_by_id(category_id, database) -> None:
    """
    Удаляет категорию по ID.

    :param category_id: Идентификатор категории.
    :param database: Сессия базы данных.
    """
    database.query(models.Category).filter(models.Category.id == category_id).delete()
    database.commit()


async def create_new_product(request, database) -> models.Product:
    """
    Создаёт новый товар (продукт).

    :param request: Объект с полями name, quantity, description, price, category_id.
    :param database: Сессия базы данных.
    :return: Созданный объект товара.
    """
    new_product = models.Product(name=request.name,
                                 quantity=request.quantity,
                                 description=request.description,
                                 price=request.price,
                                 category_id=request.category_id
                                 )
    database.add(new_product)
    database.commit()
    database.refresh(new_product)
    return new_product


async def get_all_products(database) -> List[models.Product]:
    """
    Возвращает список всех товаров.

    :param database: Сессия базы данных.
    :return: Список объектов товаров.
    """
    all_products = database.query(models.Product).all()
    return all_products


async def get_product_by_id(product_id, database) -> models.Product:
    """
    Возвращает товар по его ID.

    :param product_id: Идентификатор товара.
    :param database: Сессия базы данных.
    :raises HTTPException: Если товар не найден.
    :return: Объект товара.
    """
    product_info = database.query(models.Product).get(product_id)
    if not product_info:
        raise HTTPException(status_code=404, detail="Product not found!")
    return product_info


async def delete_product_by_id(product_id, database) -> None:
    """
    Удаляет товар по его ID.

    :param product_id: Идентификатор товара.
    :param database: Сессия базы данных.
    """
    database.query(models.Product).filter(models.Product.id == product_id).delete()
    database.commit()
