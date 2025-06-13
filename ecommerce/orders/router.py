from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ecommerce import db
from . import shema
from . import services

router = APIRouter(tags=["Orders"], prefix="/orders")


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=shema.ShowOrder)
async def initiate_order_processing(database: Session = Depends(db.get_db)):
    result = await services.initiate_order(database)
    return result
