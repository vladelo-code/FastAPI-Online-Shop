from sqlalchemy.orm import Session
from typing import Optional

from ecommerce.products import models


async def verify_category_exist(category_id, db_session: Session) -> Optional[models.Category]:
    category_info = db_session.query(models.Category).filter(models.Category.id == category_id).first()
    return category_info
