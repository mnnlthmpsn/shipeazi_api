import pytest
from src.mailing.services import SubscriberService
from src.mailing.models import Subscriber


def test_create_subscription(app):
    subscriber_service = SubscriberService("etntiamoah@st.ug.edu.gh")
    subscriber_service.create_subscription()

    created_subscriber = Subscriber.query.filter_by(email=subscriber_service.get_recipient()).first()

    assert created_subscriber.email == "etntiamoah@st.ug.edu.gh"
