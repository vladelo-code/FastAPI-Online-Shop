from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

from ecommerce import db

from . import shema
from . import services
from . import validator

router = APIRouter(tags=["Products"], prefix="/products")


@router.post('/category', status_code=status.HTTP_201_CREATED)
async def create_category(request: shema.Category, database: Session = Depends(db.get_db)):
    new_category = await services.create_new_category(request, database)
    return new_category
