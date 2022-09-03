from flask import Blueprint
from flask_pydantic import validate

from .services import SubscriberService
from .schema import EmailSchema

# blueprint
mailing = Blueprint('mailing', __name__, url_prefix='/mailing')


# routes and functions
@mailing.route('/subscribe', methods=['POST'])
@validate()
def subscribe(body: EmailSchema):
    return SubscriberService(body).create_subscription()
