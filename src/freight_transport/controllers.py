from flask import Blueprint
from flask_pydantic import validate

from .services import FreightService
from .schemas import FreightTransportBodySchema

freight = Blueprint('freight', __name__, url_prefix='/freight')


@freight.route('/new_freight', methods=['POST'])
@validate()
def new_freight_order(body: FreightTransportBodySchema):
    return FreightService.book_freight_move(body)
