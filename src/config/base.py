import os


class Config(object):
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_CONNECT_OPTIONS = {}

    # Enable protection against *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"

    BCRYPT_LOG_ROUNDS = 12
