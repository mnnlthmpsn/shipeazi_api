from pydantic import BaseModel
from src.account.schemas.entity_schema import EntityBodySchema


class FreightTransportBodySchema(BaseModel):
    entity: EntityBodySchema
    destination: str
    origin: str
    mov_date: str
    size_unit: str
    size: str
    weight_unit: str
    weight: str
