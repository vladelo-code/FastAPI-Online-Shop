from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from ecommerce import db
from ecommerce.user.shema import User
from . import services, shema

router = APIRouter(tags=["Cart"], prefix="/cart")


@router.post("/add", status_code=status.HTTP_201_CREATED)
async def add_product_to_cart(product_id: int, database: Session = Depends(db.get_db)):
    result = await services.add_product_to_cart(product_id, database)
    return result


@router.get("/", response_model=shema.ShowCart)
async def get_all_cart_items(database: Session = Depends(db.get_db)):
    result = await services.get_all_items(database)
    return result


@router.delete("/{cart_item_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def remove_cart_item_by_id(cart_item_id: int, database: Session = Depends(db.get_db)):
    result = await services.remove_cart_item(cart_item_id, database)
    return result
