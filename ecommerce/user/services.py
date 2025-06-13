from fastapi import HTTPException, status
from typing import List, Optional

from . import models
from . import shema


async def new_user_register(request, database) -> models.User:
    new_user = models.User(name=request.name, email=request.email, password=request.password)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user


async def all_users(database) -> List[shema.DisplayUser]:
    users = database.query(models.User).all()
    return users


async def get_user_by_id(user_id, database) -> Optional[models.User]:
    user_info = database.query(models.User).get(user_id)
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user_info


async def delete_user_by_id(user_id, database) -> None:
    database.query(models.User).filter(models.User.id == user_id).delete()
    database.commit()
