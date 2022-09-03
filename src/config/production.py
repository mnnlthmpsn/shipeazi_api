from src.config.base import Config


class ProductionConfig(Config):
    DEBUG = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        conString = "postgresql://shipeazi_user:shipeazi_pwd@161.35.54.129:5432/shipeazi_db"
        return conString

    