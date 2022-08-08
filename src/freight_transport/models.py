from src.base_model import BaseModel, db
from src.freight_transport.schemas import FreightTransportBodySchema


class FreightTransportModel(BaseModel):
    __tablename__ = 'freight_transport_bookings'

    entity_id = db.Column(db.String(200), db.ForeignKey("entities.uuid"), nullable=False)
    destination = db.Column(db.String(255), nullable=False)
    origin = db.Column(db.String(255), nullable=False)
    mov_date = db.Column(db.String(255), nullable=False)
    size_unit = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(100), nullable=False)
    weight_unit = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.String(100), nullable=False)

    def __init__(self, freight: FreightTransportBodySchema):
        self.entity_id = freight.entity.uuid
        self.destination = freight.destination
        self.origin = freight.origin
        self.mov_date = freight.mov_date
        self.size_unit = freight.size_unit
        self.size = freight.size
        self.weight_unit = freight.weight_unit
        self.weight = freight.weight

    def __repr__(self):
        return f"<Freight {self.entity_id} [Origin: {self.origin} - Destination: {self.destination}]>"
