from flask import Blueprint
from flask_pydantic import validate

from src.moving.schemas.move_schema import MoveBookingBodySchema
from src.moving.services import MoveService

moves = Blueprint('moves', __name__, url_prefix='/moves')


@moves.route('/new_move', methods=['POST'])
@validate()
def book_move(body: MoveBookingBodySchema):
    return MoveService.book_a_move(body)
