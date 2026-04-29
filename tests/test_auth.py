import requests
import os
from dotenv import load_dotenv
from utils.helpers import generate_unique_email

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


# REGISTER USER (POSITIVE)

def test_register_user_successfully():

    url = f"{BASE_URL}/auth/register"

    payload = {
        "email": generate_unique_email(),
        "password": "Password123!",
        "first_name": "Solange",
        "last_name": "Tester"
    }

    response = requests.post(url, json=payload)

    data = response.json()

    print(response.status_code)
    print(data)

    assert response.status_code in [200, 201]
    assert data["status"] == "success"
    assert "data" in data


# LOGIN SUCCESSFULLY

def test_login_success():

    url = f"{BASE_URL}/auth/login"

    payload = {
        "email": os.getenv("EMAIL"),
        "password": os.getenv("PASSWORD")
    }

    response = requests.post(url, json=payload)

    data = response.json()

    print(response.status_code)
    print(data)

    assert response.status_code == 200
    assert "data" in data
    assert "access_token" in data["data"]


# LOGIN INVALID PASSWORD

def test_login_invalid_password():

    url = f"{BASE_URL}/auth/login"

    payload = {
        "email": os.getenv("EMAIL"),
        "password": "WrongPassword123!"
    }

    response = requests.post(url, json=payload)

    data = response.json()

    print(response.status_code)
    print(data)

    assert response.status_code in [400, 401]
    assert "message" in data



# LOGIN MISSING EMAIL

def test_login_missing_email():

    url = f"{BASE_URL}/auth/login"

    payload = {
        "password": os.getenv("PASSWORD")
    }

    response = requests.post(url, json=payload)

    data = response.json()

    print(response.status_code)
    print(data)

    assert response.status_code in [400, 422]
    assert "message" in data


# LOGIN MISSING PASSWORD

def test_login_missing_password():

    url = f"{BASE_URL}/auth/login"

    payload = {
        "email": os.getenv("EMAIL")
    }

    response = requests.post(url, json=payload)

    data = response.json()

    print(response.status_code)
    print(data)

    assert response.status_code in [400, 422]
    assert "message" in data


# LOGIN INVALID EMAIL FORMAT

def test_login_invalid_email_format():

    url = f"{BASE_URL}/auth/login"

    payload = {
        "email": "invalid-email-format",
        "password": os.getenv("PASSWORD")
    }

    response = requests.post(url, json=payload)

    data = response.json()

    print(response.status_code)
    print(data)

    assert response.status_code in [400, 401, 422]
    assert "message" in data


#  FAILURE TEST

def test_intentional_failure_example():

    url = f"{BASE_URL}/auth/login"

    payload = {
        "email": os.getenv("EMAIL"),
        "password": os.getenv("PASSWORD")
    }

    response = requests.post(url, json=payload)

    # intentionally wrong to demonstrate failure
    assert response.status_code == 500