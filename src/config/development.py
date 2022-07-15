import os
from src.config.base import Config


class DevelopmentConfig(Config):
    DEBUG = True

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return "sqlite:///" + os.path.join(self.BASE_DIR, "sqlite.db")
