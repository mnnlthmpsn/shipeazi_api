import sendgrid
from flask import jsonify
from src.utils.app_constants import AppConstants
from src.base_model import db
from src.utils.error_handler import GeneralErrorHandler
from .models import SubscriberModel
from .schema import EmailSchema, EmailBodySchema

from sendgrid.helpers.mail import *


class SubscriberService:
    def __init__(self, subscriber: EmailSchema):
        self._recipient = subscriber.email

    def get_recipient(self):
        return self._recipient

    def create_subscription(self):
        try:
            new_subscriber = SubscriberModel(self._recipient)
            new_subscriber.save()
            print(new_subscriber.email)
        except Exception as exception:
            return GeneralErrorHandler(exception, 'Subscriber').throw_err
        else:
            return jsonify({"message": "Subscription added successfully"})

    def cancel_subscription(self):
        try:
            subscriber = SubscriberModel.query.filter_by(email=self._recipient).first_or_404
            subscriber.update({"active_status": False, "del_status": True})
            db.session.commit()
        except Exception as err:
            return err


class EmailService:
    def __init__(self, email_details: EmailBodySchema):
        self._email = email_details

    def send_email(self):
        try:
            sg = sendgrid.SendGridAPIClient(api_key="SG.Bt3FMeH7SxW4hhio-ZzoHw"
                                                    ".GUZMTmMgujhXi9B6CmzsMdhYuHc0jgwdO8H1X_bR8Ok")
            client_service_email = Email(AppConstants.no_reply_mail)
            email_recipient = To(self._email.recipient)
            email_subject = self._email.subject
            email_content = self._email.message

            mail_payload = Mail(client_service_email, email_recipient, email_subject, email_content)
            res = sg.client.mail.send.post(request_body=mail_payload.get())
        except Exception as exception:
            return GeneralErrorHandler(exception, "Email").throw_err
        else:
            print(res.status_code)
            print("Email Generated and sent") if res.status_code == 202 else print("An error occurred sending email")
            return True if res.status_code == 202 else False
