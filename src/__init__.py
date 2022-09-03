from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin

# config
from config import config

# src
from src.base_model import db, bcrypt

# components
from src.mailing.controllers import mailing as MailingService
from src.account.controllers import accounts as AccountsService
from src.admin.controllers import admin as AdminService
from src.moving.controllers import moves as MoveService
from src.freight_transport.controllers import freight as FreightService

migrate = Migrate()


def create_app(def_config=config):
    flask_app = Flask(__name__)
    CORS(flask_app)

    # load configurations based on environment
    flask_app.config.from_object(def_config)

    # db orm init
    db.init_app(flask_app)
    bcrypt.init_app(flask_app)

    migrate.init_app(flask_app, db)

    # error handler
    @flask_app.errorhandler(404)
    def not_found(error):
        return {"message": "Resource not found"}, 404

    # blueprints
    flask_app.register_blueprint(AccountsService)
    flask_app.register_blueprint(AdminService)
    flask_app.register_blueprint(FreightService)
    flask_app.register_blueprint(MailingService)
    flask_app.register_blueprint(MoveService)

    with flask_app.app_context():
        db.create_all()

    return flask_app


if __name__ == "__main__":
    app = create_app()
