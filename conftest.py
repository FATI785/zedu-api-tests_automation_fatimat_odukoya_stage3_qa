import pytest
import os
import requests
from utils.auth import get_token
from utils.helpers import generate_unique_name

BASE_URL = os.getenv("BASE_URL")


@pytest.fixture
def auth_headers():
    token = get_token()
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def organisation(auth_headers):
    payload = {
        "name": generate_unique_name(),
        "description": "automation org",
        "country": "ng",
        "type": "user default org"
    }

    response = requests.post(
        f"{BASE_URL}/organisations",
        json=payload,
        headers=auth_headers
    )

    assert response.status_code in [200, 201]

    data = response.json()
    return data["data"]["id"]