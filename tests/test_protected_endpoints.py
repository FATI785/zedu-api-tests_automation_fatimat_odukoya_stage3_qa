import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


# VALID TOKEN ACCESS

def test_access_protected_endpoint_with_valid_token(auth_headers):

    response = requests.get(
        f"{BASE_URL}/auth/onboard-status",
        headers=auth_headers
    )

    data = response.json()

    print(response.status_code)
    print(data)

    assert response.status_code == 200
    assert "status" in data or "data" in data


# NO TOKEN ACCESS (NEGATIVE)

def test_access_protected_endpoint_without_token_fails():

    response = requests.get(
        f"{BASE_URL}/auth/onboard-status"
    )

    data = response.json()

    print(response.status_code)
    print(data)

    assert response.status_code in [401, 403]


# INVALID TOKEN ACCESS (NEGATIVE)

def test_access_protected_endpoint_with_invalid_token_fails():

    headers = {
        "Authorization": "Bearer invalid_token_123"
    }

    response = requests.get(
        f"{BASE_URL}/auth/onboard-status",
        headers=headers
    )

    data = response.json()

    print(response.status_code)
    print(data)

    assert response.status_code in [401, 403]