import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def get_token():
    """
    Logs in a user and returns the access token.
    """

    url = f"{BASE_URL}/auth/login"

    payload = {
        "email": os.getenv("EMAIL"),
        "password": os.getenv("PASSWORD")
    }

    response = requests.post(url, json=payload)
    response_data = response.json()

    # Safety check: fail loudly if structure changes
    if "data" not in response_data or "access_token" not in response_data["data"]:
        raise Exception(f"Token not found in response: {response_data}")

    return response_data["data"]["access_token"]