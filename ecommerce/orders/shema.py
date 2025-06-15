from pydantic import BaseModel, ConfigDict
import datetime
from typing import Optional, List

from ecommerce.products.shema import DisplayProduct


class ShowOrderDetails(BaseModel):
    id: int
    order_id: int
    product_order_details: DisplayProduct

    model_config = ConfigDict(from_attributes=True)


class ShowOrder(BaseModel):
    id: Optional[int]
    order_date: datetime.datetime
    order_amount: float
    order_status: str
    shipping_address: str
    order_details: List[ShowOrderDetails] = []

    model_config = ConfigDict(from_attributes=True)
