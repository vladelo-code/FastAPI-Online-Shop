from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

from ecommerce import db
from . import shema, services, validator

router = APIRouter(tags=["Categories & products"], prefix="/products")


@router.post('/category', status_code=status.HTTP_201_CREATED)
async def create_category(request: shema.Category, database: Session = Depends(db.get_db)):
    new_category = await services.create_new_category(request, database)
    return new_category


@router.get('/category', response_model=List[shema.DisplayCategory])
async def get_all_categories(database: Session = Depends(db.get_db)):
    categories = await services.get_all_categories(database)
    return categories


@router.get('/category/{category_id}', response_model=shema.DisplayCategory)
async def get_category_by_id(category_id: int, database: Session = Depends(db.get_db)):
    category = await services.get_category_by_id(category_id, database)
    return category


@router.delete('/category/{category_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_category(category_id: int, database: Session = Depends(db.get_db)) -> None:
    return await services.delete_category_by_id(category_id, database)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_product(request: shema.Product, database: Session = Depends(db.get_db)):
    category = await validator.verify_category_exist(request.category_id, database)
    if not category:
        raise HTTPException(status_code=404, detail="You have provided invalid category id!")
    new_product = await services.create_new_product(request, database)
    return new_product


@router.get('/', response_model=List[shema.DisplayProduct])
async def get_all_products(database: Session = Depends(db.get_db)):
    products = await services.get_all_products(database)
    return products


@router.get('/{product_id}', response_model=shema.DisplayProduct)
async def get_product_by_id(product_id: int, database: Session = Depends(db.get_db)):
    product = await services.get_product_by_id(product_id, database)
    return product


@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_product(product_id: int, database: Session = Depends(db.get_db)) -> None:
    return await services.delete_product_by_id(product_id, database)
