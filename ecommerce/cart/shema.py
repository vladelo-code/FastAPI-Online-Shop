from typing import List
from pydantic import BaseModel, ConfigDict
import datetime

from ecommerce.products.shema import Product


class ShowCartItems(BaseModel):
    id: int
    products: Product
    created_date: datetime.datetime

    model_config = ConfigDict(from_attributes=True)


class ShowCart(BaseModel):
    id: int
    cart_items: List[ShowCartItems] = []

    model_config = ConfigDict(from_attributes=True)
