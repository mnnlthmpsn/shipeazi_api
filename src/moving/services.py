from src.moving.schemas import MoveBookingBodySchema
from src.utils.error_handler import GeneralErrorHandler

from src.account.services import EntityService
from src.account.models import EntityModel
from src.account.schemas.entity_schema import EntityBodySchema
from src.orders.services import OrderService

from src.moving.models import MoveBookingModel


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
            order_service = OrderService(entity_service)
            return order_service.create_order(booking_instance.uuid)


def throw_err(exception):
    return GeneralErrorHandler(exception, "Move").throw_err
