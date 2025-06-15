from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from ecommerce import db
from ecommerce.user.shema import User
from ecommerce.auth import jwt
from ecommerce.orders import shema
from ecommerce.orders import services

router = APIRouter(tags=["Orders"], prefix="/orders")


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=shema.ShowOrder)
async def initiate_order_processing(database: Session = Depends(db.get_db),
                                    current_user: User = Depends(jwt.get_current_user)):
    result = await services.initiate_order(current_user, database)
    return result


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[shema.ShowOrder])
async def get_order_list(database: Session = Depends(db.get_db), current_user: User = Depends(jwt.get_current_user)):
    result = await services.get_order_listing(current_user, database)
    return result
