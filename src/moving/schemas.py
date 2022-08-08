from pydantic import BaseModel

from src.account.schemas.entity_schema import EntityBodySchema


class MoveBookingBodySchema(BaseModel):
    entity: EntityBodySchema
    move_category: str
    destination: str
    origin: str
    mov_date: str
    mov_reason: str
    mov_size: str
    move_to_building_type: str
    move_from_building_type: str
    items_to_move: str
    is_packaging_required: bool
    is_dismantling_required: bool
    is_storage_required: bool


class MoveBookingResponseSchema(BaseModel):
    message: str
