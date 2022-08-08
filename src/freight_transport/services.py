from src.utils.error_handler import GeneralErrorHandler

from .schemas import FreightTransportBodySchema
from src.freight_transport.models import FreightTransportModel

from src.account.services import EntityService
from src.account.models import EntityModel
from src.account.schemas.entity_schema import EntityBodySchema
from src.orders.services import OrderService


class FreightService:

    @classmethod
    def book_freight_move(cls, freight_details: FreightTransportBodySchema):
        try:
            # check if entity entity_exists
            entity_service = EntityService(freight_details.entity)
            entity_exists = entity_service.entity_exists()

            # you need a transaction here. fix this later
            if entity_exists is False:
                entity_service.create_entity()

            # get entity and create booking with entity_id
            entity_instance = EntityModel.query.filter_by(email=freight_details.entity.email).first()
            entity = EntityBodySchema(
                uuid=entity_instance.uuid,  # very important
                name=entity_instance.name, phone=entity_instance.phone,
                is_business=entity_instance.is_business, email=entity_instance.email
            )

            # update previous entity with the latest entity
            freight_details.entity = entity
            booking_instance = FreightTransportModel(freight_details)
            booking_instance.save()

        except Exception as exception:
            return throw_err(exception)
        else:
            order_service = OrderService(entity_service)
            return order_service.create_order(booking_instance.uuid)


def throw_err(exception):
    return GeneralErrorHandler(exception, "Freight Transport").throw_err
