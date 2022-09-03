import random
import string
import uuid
from datetime import date


def generate_uuid():
    return str(uuid.uuid4())


def generate_order_id():
    today = date.today()
    dt = today.strftime("%d/%m/%Y")
    chars = string.digits
    invoice_num = ''.join(random.choice(chars) for _ in range(5))
    return f"SHPZ/{invoice_num}/{dt}"  # SHP-12345
