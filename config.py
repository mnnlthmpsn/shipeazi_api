import os
from src.config import get_config

print(os.environ.get('FLASK_ENV'))

config = get_config(os.environ.get("FLASK_ENV"))
