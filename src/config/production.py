from src.config.base import Config
import os


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    uri = os.getenv("DATABASE_URL")  # or other relevant config var
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    # rest of connection code using the connection string `uri`
