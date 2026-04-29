import requests
import os
from dotenv import load_dotenv
from utils.helpers import generate_unique_name

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


# CREATE ROLE TEST ORGANISATION

def create_org(auth_headers):

    payload = {
        "name": generate_unique_name(),
        "description": "roles test org",
        "country": "ng",
        "type": "user default org"
    }

    response = requests.post(
        f"{BASE_URL}/organisations",
        json=payload,
        headers=auth_headers
    )

    data = response.json()

    print("ORG:", response.status_code, data)

    assert response.status_code in [200, 201]

    return data["data"]["id"]



# GET ROLES

def test_get_organisation_roles(auth_headers):

    org_id = create_org(auth_headers)

    response = requests.get(
        f"{BASE_URL}/organisations/{org_id}/roles",
        headers=auth_headers
    )

    data = response.json()

    print(response.status_code)
    print(data)

    assert response.status_code in [200, 404]



# CREATE ROLE

def test_create_organisation_role(auth_headers):

    org_id = create_org(auth_headers)

    payload = {
        "name": "QA Tester"
    }

    response = requests.post(
        f"{BASE_URL}/organisations/{org_id}/roles",
        json=payload,
        headers=auth_headers
    )

    data = response.json()

    print(response.status_code)
    print(data)

    assert response.status_code in [200, 201]


# NEGATIVE TEST - INVALID ORG

def test_get_roles_with_invalid_org_id_fails(auth_headers):

    response = requests.get(
        f"{BASE_URL}/organisations/invalid-org-123/roles",
        headers=auth_headers
    )

    data = response.json()

    print(response.status_code)
    print(data)

    assert response.status_code in [400, 404]