import pytest
import logging
from src.config import TestingConfig

from src import create_app
from src.base_model import db

logger = logging.getLogger("faker")
logger.setLevel(logging.ERROR)


@pytest.fixture()
def app():
    app = create_app(def_config=TestingConfig())
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
