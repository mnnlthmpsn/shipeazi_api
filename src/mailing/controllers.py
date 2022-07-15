from flask import Blueprint, request, jsonify

from .services import SubscriberService

# blueprint
mailing = Blueprint('mailing', __name__, url_prefix='/mailing')


# routes and functions
@mailing.route('/subscribe', methods=['POST'])
def subscribe():
    try:
        data = request.get_json()

        subscriber_service = SubscriberService(data["recipient"])
        subscriber_service.create_subscription()
        return {"message": "Subscription added successfully"}

    except Exception as err:
        # log error
        print(err)
        return {"message": "An error occurred creating subscription"}, 500
