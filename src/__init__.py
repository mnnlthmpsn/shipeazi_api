from flask import Flask
from flask_migrate import Migrate

# config
from config import config

# src
from src.base_model import db
from src.mailing.controllers import mailing

migrate = Migrate()


def create_app(def_config=config):
    app = Flask(__name__)

    # load configurations based on environment
    app.config.from_object(def_config)

    # db orm init
    db.init_app(app)

    migrate.init_app(app, db)

    # error handler
    @app.errorhandler(404)
    def not_found(error):
        return {"message": "Resource not found"}, 404

    # blueprints
    app.register_blueprint(mailing)
    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
