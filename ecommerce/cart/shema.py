from typing import List
from pydantic import BaseModel
import datetime

from ecommerce.products.shema import Product


class ShowCartItems(BaseModel):
    id: int
    products: Product
    created_date: datetime.datetime

    class Config:
        from_attributes = True


class ShowCart(BaseModel):
    id: int
    cart_items: List[ShowCartItems] = []

    class Config:
        from_attributes = True
