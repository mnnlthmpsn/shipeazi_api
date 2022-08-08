from src.base_model import BaseModel, db
from src.utils import generate_order_id


class OrderModel(BaseModel):
    __tablename__ = 'orders'

    moving_book_id = db.Column(db.String(200), db.ForeignKey("move_bookings.uuid"), nullable=False)
    order_id = db.Column(db.String(200), nullable=False, default=generate_order_id)
    fulfilled = db.Column(db.Boolean(), nullable=False, default=False)

    def __init__(self, booking_id: str):
        self.moving_book_id = booking_id
