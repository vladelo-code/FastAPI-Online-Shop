from pydantic import BaseModel, constr
from typing import Optional


class Category(BaseModel):
    name: constr(min_length=2, max_length=50)


class DisplayCategory(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    id: Optional[int]
    name: str
    quantity: int
    description: str
    price: float

    class Config:
        from_attributes = True

class Product(ProductBase):
    category_id: int