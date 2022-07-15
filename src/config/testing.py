import os
from src.config.base import Config


class TestingConfig(Config):
    DEBUG = True
    TESTING = True

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return "sqlite:///" + os.path.join(self.BASE_DIR, "test.db")
