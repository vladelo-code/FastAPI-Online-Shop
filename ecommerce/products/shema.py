from pydantic import BaseModel, constr, ConfigDict
from typing import Optional


class Category(BaseModel):
    name: constr(min_length=2, max_length=50)


class DisplayCategory(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class ProductBase(BaseModel):
    id: Optional[int]
    name: str
    quantity: int
    description: str
    price: float

    model_config = ConfigDict(from_attributes=True)


class Product(ProductBase):
    category_id: int


class DisplayProduct(ProductBase):
    category: DisplayCategory

    model_config = ConfigDict(from_attributes=True)


class ProductCreate(BaseModel):
    name: constr(min_length=1, max_length=50)
    quantity: int
    description: str
    price: float
    category_id: int
