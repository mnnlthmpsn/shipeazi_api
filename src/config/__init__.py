import os
from src.config.testing import TestingConfig
from src.config.production import ProductionConfig
from src.config.development import DevelopmentConfig


def get_config(env):
    if env == "development":
        return DevelopmentConfig()
    elif env == "production":
        return ProductionConfig()
    else:
        return TestingConfig()
