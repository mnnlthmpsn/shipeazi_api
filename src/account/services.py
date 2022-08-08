from src.account.schemas.entity_schema import EntityBodySchema, EntityResponseSchema
from src.account.models import EntityModel
from src.utils.error_handler import GeneralErrorHandler


class EntityService:
    def __init__(self, entity: EntityBodySchema):
        self._entity = entity

    def create_entity(self):
        try:
            new_entity = EntityModel(self._entity)
            new_entity.save()
        except Exception as exception:
            return GeneralErrorHandler(exception, "Entity").throw_err
        else:
            data = EntityBodySchema(
                uuid=new_entity.uuid, name=new_entity.name,
                phone=new_entity.phone, email=new_entity.email, is_business=new_entity.is_business
            )
            return EntityResponseSchema(message="Entity added successfully", data=data)

    def entity_exists(self):
        try:
            entity = EntityModel.query.filter_by(email=self._entity.email).first()
        except Exception as exception:
            return GeneralErrorHandler(exception, "Entity").throw_err
        else:
            return False if entity is None else True

    def get_entity(self):
        return self._entity
