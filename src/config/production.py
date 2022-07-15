from src.config.base import Config
import os


class ProductionConfig(Config):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
