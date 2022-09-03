from flask import Blueprint
from flask_pydantic import validate

from src.moving.schemas import MoveBookingBodySchema
from src.moving.services import MoveService
from src.orders.services import OrderService

moves = Blueprint('moves', __name__, url_prefix='/moves')


@moves.route('/new_move', methods=['POST'])
@validate()
def book_move(body: MoveBookingBodySchema):
    return MoveService.book_a_move(body)
