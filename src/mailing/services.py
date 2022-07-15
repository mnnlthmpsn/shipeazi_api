from .models import Subscriber
from src.base_model import db


class SubscriberService:
    def __init__(self, recipient):
        self._recipient = recipient

    def get_recipient(self):
        return self._recipient

    def create_subscription(self):
        try:
            new_subscriber = Subscriber(self._recipient)
            db.session.add(new_subscriber)
            db.session.commit()
        except Exception as err:
            return err

    def cancel_subscription(self):
        try:
            subscriber = Subscriber.query.filter_by(email=self._recipient).first_or_404
            subscriber.update({"active_status": False, "del_status": True})
            db.session.commit()
        except Exception as err:
            return err
