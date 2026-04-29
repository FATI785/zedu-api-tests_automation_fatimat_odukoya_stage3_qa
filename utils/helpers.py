import time
import uuid


def generate_unique_email():
    unique_id = uuid.uuid4().hex[:6]
    return f"solange_{unique_id}_{int(time.time())}@mail.com"


def generate_unique_name():
    unique_id = uuid.uuid4().hex[:6]
    return f"solange_{unique_id}_{int(time.time())}"