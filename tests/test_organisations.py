import requests
import os
from dotenv import load_dotenv
from utils.helpers import generate_unique_name

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


# CREATE ORGANISATION (POSITIVE)

def test_create_organisation_successfully(auth_headers):

    payload = {
        "name": generate_unique_name(),
        "description": "Automation test organisation",
        "country": "ng",
        "type": "user default org"
    }

    response = requests.post(
        f"{BASE_URL}/organisations",
        json=payload,
        headers=auth_headers
    )

    data = response.json()

    assert response.status_code in [200, 201]
    assert data.get("status") in ["success", "ok"]
    assert "data" in data


# GET ORGANISATION BY ID

def test_retrieve_organisation_by_id(auth_headers):

    create_payload = {
        "name": generate_unique_name(),
        "description": "Retrieve test",
        "country": "ng",
        "type": "user default org"
    }

    create_response = requests.post(
        f"{BASE_URL}/organisations",
        json=create_payload,
        headers=auth_headers
    )

    assert create_response.status_code in [200, 201]

    org_id = create_response.json()["data"]["id"]

    response = requests.get(
        f"{BASE_URL}/organisations/{org_id}",
        headers=auth_headers
    )

    assert response.status_code == 200


# NEGATIVE: INVALID ORG ID

def test_invalid_organisation_id_fails(auth_headers):

    response = requests.get(
        f"{BASE_URL}/organisations/invalid-id",
        headers=auth_headers
    )

    assert response.status_code in [400, 404]


# NEGATIVE: MISSING FIELDS

def test_create_organisation_missing_fields_fails(auth_headers):

    payload = {
        "description": "Invalid org"
    }

    response = requests.post(
        f"{BASE_URL}/organisations",
        json=payload,
        headers=auth_headers
    )

    assert response.status_code in [400, 422]


# NEGATIVE: INVALID TYPE

def test_create_organisation_invalid_type_fails(auth_headers):

    payload = {
        "name": generate_unique_name(),
        "description": "Invalid type",
        "country": "ng",
        "type": "invalid_type_xyz"
    }

    response = requests.post(
        f"{BASE_URL}/organisations",
        json=payload,
        headers=auth_headers
    )

    assert response.status_code in [400, 422]


# NEGATIVE: NO AUTH

def test_create_organisation_without_token_fails():

    payload = {
        "name": generate_unique_name(),
        "description": "No auth test",
        "country": "ng",
        "type": "user default org"
    }

    response = requests.post(
        f"{BASE_URL}/organisations",
        json=payload
    )

    assert response.status_code in [401, 403]