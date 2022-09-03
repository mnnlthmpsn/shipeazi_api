from src.account.services import EntityService
from src.account.models import EntityModel
from src.account.schemas.entity_schema import EntityBodySchema


def test_create_entity_service(app):
    new_entity = EntityBodySchema(
        name="Emmanuel Thompson", phone="0540609437", email="mnnlthmpsn@outlook.com", is_business=False
    )

    entity_service = EntityService(new_entity)
    entity_service.create_entity()

    created_entity: EntityBodySchema = EntityModel.query.filter_by(phone=new_entity.phone).first()

    assert created_entity.uuid is not None
    assert created_entity.phone.__eq__("0540609437")
    assert created_entity.email.__eq__("mnnlthmpsn@outlook.com")
    assert created_entity.is_business.__eq__(False)


