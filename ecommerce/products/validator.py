from sqlalchemy.orm import Session
from typing import Optional

from ecommerce.products import models


async def verify_category_exist(category_id, db_session: Session) -> Optional[models.Category]:
    """
    Проверяет существование категории по её ID.

    :param category_id: Идентификатор категории.
    :param db_session: Сессия SQLAlchemy.
    :return: Объект Category, если найден, иначе None.
    """
    category_info = db_session.query(models.Category).filter(models.Category.id == category_id).first()
    return category_info
