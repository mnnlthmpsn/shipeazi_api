from flask import Blueprint
from flask_pydantic import validate

from src.account.schemas.entity_schema import EntityBodySchema
from src.account.services import EntityService

accounts = Blueprint('accounts', __name__, url_prefix='/accounts')


# routes and functions
@accounts.route('/new_entity', methods=['POST'])
@validate()
def create_entity(body: EntityBodySchema):
    return EntityService(body).create_entity()
