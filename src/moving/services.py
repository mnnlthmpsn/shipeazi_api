from src.moving.schemas.move_schema import MoveBookingBodySchema, MoveBookingResponseSchema
from src.utils.error_handler import GeneralErrorHandler

from src.account.services import EntityService
from src.account.models import EntityModel
from src.account.schemas.entity_schema import EntityBodySchema

from src.moving.schemas.order_schema import OrderResponseSchema
from src.moving.models import MoveBookingModel, OrderModel

from src.mailing.services import EmailService
from src.mailing.schema import EmailBodySchema


class MoveService:

    @classmethod
    def book_a_move(cls, move_details: MoveBookingBodySchema):
        try:
            # check if entity entity_exists
            entity_service = EntityService(move_details.entity)
            entity_exists = entity_service.entity_exists()

            # you need a transaction here. fix this later
            if entity_exists is False:
                entity_service.create_entity()

            # get entity and create booking with entity_id
            entity_instance = EntityModel.query.filter_by(email=move_details.entity.email).first()
            entity = EntityBodySchema(
                uuid=entity_instance.uuid,  # very important
                name=entity_instance.name, phone=entity_instance.phone,
                is_business=entity_instance.is_business, email=entity_instance.email
            )

            # update previous entity with the latest entity
            move_details.entity = entity
            booking_instance = MoveBookingModel(move_details)
            booking_instance.save()

        except Exception as exception:
            return throw_err(exception)
        else:
            # create an order
            return cls._create_order(booking_instance.uuid, entity)

    @classmethod
    def _create_order(cls, booking_id, entity: EntityBodySchema):
        try:
            order_instance = OrderModel(booking_id)
            order_instance.save()
        except Exception as exception:
            return throw_err(exception)
        else:
            # send email
            email_details = EmailBodySchema(
                recipient=entity.email, subject="SHIPEAZI MOVING ORDER",
                message=f"Dear {entity.name}, \n\n"
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
    return GeneralErrorHandler(exception, "Move").throw_err
