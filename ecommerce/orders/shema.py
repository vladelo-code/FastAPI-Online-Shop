from pydantic import BaseModel
import datetime
from typing import Optional, List

from ecommerce.products.shema import DisplayProduct


class ShowOrderDetails(BaseModel):
    id: int
    order_id: int
    product_order_details: DisplayProduct

    class Config:
        from_attributes = True


class ShowOrder(BaseModel):
    id: Optional[int]
    order_date: datetime.datetime
    order_amount: float
    order_status: str
    shipping_address: str
    order_details: List[ShowOrderDetails] = []

    class Config:
        from_attributes = True
