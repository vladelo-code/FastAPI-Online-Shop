from typing import List

from fastapi import HTTPException, status

from . import models
from . import shema


async def new_user_register(request, database) -> models.User:
    new_user = models.User(name=request.name, email=request.email, password=request.password)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user


async def all_users(db_session) -> List[shema.DisplayUser]:
    users = db_session.query(models.User).all()
    return users
