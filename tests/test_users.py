import requests
import os
from dotenv import load_dotenv
from utils.auth import get_token

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


# GET USER ORGANISATIONS

def test_retrieve_user_organisations(auth_headers):

    response = requests.get(
        f"{BASE_URL}/users/organisations",
        headers=auth_headers
    )

    data = response.json()

    print(response.status_code)
    print(data)

    assert response.status_code == 200
    assert "data" in data


# GET USER STATUS

def test_get_user_status(auth_headers):

    user_id = "me"

    response = requests.get(
        f"{BASE_URL}/users/{user_id}/status",
        headers=auth_headers
    )

    data = response.json()

    print(response.status_code)
    print(data)

    assert response.status_code == 200
    assert "status" in data or "data" in data



# NEGATIVE TEST - NO TOKEN

def test_user_endpoint_without_token_fails():

    response = requests.get(f"{BASE_URL}/users/organisations")

    data = response.json()

    print(response.status_code)
    print(data)

    assert response.status_code in [401, 403]