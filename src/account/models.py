from src.base_model import BaseModel, db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from .schemas.entity_schema import EntityBodySchema


class EntityModel(BaseModel):

    __tablename__ = 'entities'

    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(128), nullable=False)
    is_business = db.Column(db.Boolean, nullable=False)

    def __init__(self, entity: EntityBodySchema):
        self.name = entity.name
        self.email = entity.email
        self.phone = entity.phone
        self.is_business = entity.is_business

    def __repr__(self):
        return f"<Entity {self.name}>"


class AccountModel(BaseModel):

    __tablename__ = 'accounts'

    entity_id = db.Column(db.String(200), db.ForeignKey("entities.uuid"), nullable=False, unique=True)
    recovery_email = db.Column(db.String(255), nullable=False)
    _password = db.Column(db.String(200))

    def __init__(self, account):
        self.entity_id = account["entity_id"]
        self.recovery_email = account["recovery_email"]

    def __repr__(self):
        return f"<Account {self.uuid}>"

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plain_password):
        self._password = bcrypt.generate_password_hash(plain_password)

    def is_correct_password(self, plain_password):
        if bcrypt.check_password_hash(self._password, plain_password):
            return True
        return False
