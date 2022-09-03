from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from src.utils import generate_uuid

db = SQLAlchemy()
bcrypt = Bcrypt()


class BaseModel(db.Model):
    """
    Define a base model for other database tables to inherit
    """

    __abstract__ = True

    uuid = db.Column(db.String, primary_key=True, default=generate_uuid)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )

    def save(self):
        db.session.add(self)
        db.session.commit()
