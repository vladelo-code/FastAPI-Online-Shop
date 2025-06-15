from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from ecommerce.user import models
from ecommerce.user import shema


async def new_user_register(request: shema.User, database: Session) -> models.User:
    """
    Создаёт нового пользователя на основе переданных данных.

    :param request: Объект с данными нового пользователя.
    :param database: Сессия базы данных.
    :return: Созданный пользователь (модель).
    """
    new_user = models.User(name=request.name, email=request.email, password=request.password)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user


async def all_users(database: Session) -> List[shema.DisplayUser]:
    """
    Возвращает список всех пользователей.

    :param database: Сессия базы данных.
    :return: Список пользователей (Pydantic-схемы).
    """
    users = database.query(models.User).all()
    return users


async def get_user_by_id(user_id: int, database: Session) -> Optional[models.User]:
    """
    Получает пользователя по ID. Бросает исключение, если пользователь не найден.

    :param user_id: Идентификатор пользователя.
    :param database: Сессия базы данных.
    :return: Объект пользователя.
    """
    user_info = database.query(models.User).get(user_id)
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user_info


async def delete_user_by_id(user_id: int, database: Session) -> None:
    """
    Удаляет пользователя по ID. Бросает исключение, если пользователь не найден.

    :param user_id: Идентификатор пользователя.
    :param database: Сессия базы данных.
    """
    database.query(models.User).filter(models.User.id == user_id).delete()
    database.commit()
