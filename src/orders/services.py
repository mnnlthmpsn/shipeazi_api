from src.utils.error_handler import GeneralErrorHandler

from src.account.services import EntityService
from src.mailing.services import EmailService
from src.mailing.schema import EmailBodySchema

from .models import OrderModel
from .schemas import OrderResponseSchema


class OrderService:
    def __init__(self, entity_service: EntityService):
        self.entity_service = entity_service

    def create_order(self, booking_id):
        try:
            order_instance = OrderModel(booking_id)
            order_instance.save()
        except Exception as exception:
            return throw_err(exception)
        else:
            # send email
            email_details = EmailBodySchema(
                recipient=self.entity_service.get_entity().email, subject="SHIPEAZI MOVING ORDER",
                message=f"Dear {self.entity_service.get_entity().name}, \n\n"
                        f"An order with ID:{order_instance.order_id} has been created in your name.\n"
                        "Our Customer Representative will reach out to you shortly with an invoice.\n"
                        "Contact us with this Order ID if a representative doesn't reach out within an hour \n\n"
                        "Thank you for doing business with us.\n\n"
                        "Shipeazi\n"
                        "(233) 54 060 9437"
            )

            EmailService(email_details).send_email()

            return OrderResponseSchema(
                message="Your order has been created", created_at=order_instance.created_at,
                order_id=order_instance.order_id
            )


def throw_err(exception):
    return GeneralErrorHandler(exception, 'Order').throw_err
