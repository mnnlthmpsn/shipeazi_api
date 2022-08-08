from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class OrderResponseSchema(BaseModel):
    message: str
    order_id: Optional[str]
    created_at: Optional[datetime]

