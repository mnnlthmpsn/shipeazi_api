from pydantic import BaseModel, EmailStr
from typing import Optional


class EntityBodySchema(BaseModel):
    uuid: Optional[str]
    name: str
    phone: str
    email: EmailStr
    is_business: bool


class EntityResponseSchema(BaseModel):
    message: str
    data: EntityBodySchema
