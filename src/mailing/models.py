from src.base_model import BaseModel, db
from sqlalchemy.sql import expression


class Subscriber(BaseModel):
    email = db.Column(db.String(255), nullable=False)
    active_status = db.Column(db.Boolean, server_default=expression.true())
    del_status = db.Column(db.Boolean, server_default=expression.true())

    def __init__(self, email):
        self.email = email
        self.active_status = True
        self.del_status = False

    def __repr__(self):
        return f"<Subscriber {self.email}"
