from sqlalchemy.orm import Session
from typing import Optional

from ecommerce.user.models import User


async def verify_email_exist(email: str, db: Session) -> Optional[User]:
    """
    Проверяет, существует ли пользователь с указанным email.

    :param email: Email пользователя.
    :param db: Сессия базы данных.
    :return: Объект User, если найден, иначе None.
    """
    return db.query(User).filter(User.email == email).first()
