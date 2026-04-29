import requests
import os
from dotenv import load_dotenv
from utils.helpers import generate_unique_name

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


# CHANNEL TEST HELPERS

def build_channel_payload(org_id):
    return {
        "username": "automation-user",
        "name": generate_unique_name(),
        "description": "automation channel test",
        "organisation_id": org_id
    }


# CREATE CHANNEL

def test_create_channel_successfully(auth_headers, organisation):

    payload = build_channel_payload(organisation)

    response = requests.post(
        f"{BASE_URL}/channels",
        json=payload,
        headers=auth_headers
    )

    data = response.json()

    print(response.status_code)
    print(data)

    assert response.status_code in [200, 201]
    assert "data" in data


# JOIN CHANNEL

def test_join_channel_successfully(auth_headers, organisation):

    create_payload = build_channel_payload(organisation)

    create_response = requests.post(
        f"{BASE_URL}/channels",
        json=create_payload,
        headers=auth_headers
    )

    assert create_response.status_code in [200, 201]

    channel_id = create_response.json()["data"]["id"]

    join_response = requests.post(
        f"{BASE_URL}/channels/{channel_id}/join",
        headers=auth_headers
    )

    print(join_response.status_code)
    print(join_response.json())

    assert join_response.status_code in [200, 201]


# LEAVE CHANNEL

def test_leave_channel_successfully(auth_headers, organisation):

    create_payload = build_channel_payload(organisation)

    create_response = requests.post(
        f"{BASE_URL}/channels",
        json=create_payload,
        headers=auth_headers
    )

    assert create_response.status_code in [200, 201]

    channel_id = create_response.json()["data"]["id"]

    leave_response = requests.post(
        f"{BASE_URL}/channels/{channel_id}/leave",
        headers=auth_headers
    )

    print(leave_response.status_code)
    print(leave_response.json())

    assert leave_response.status_code in [200, 201]


# NEGATIVE TEST (NO TOKEN)

def test_create_channel_without_token_fails(organisation):

    payload = build_channel_payload(organisation)

    response = requests.post(
        f"{BASE_URL}/channels",
        json=payload
    )

    print(response.status_code)
    print(response.json())

    assert response.status_code in [401, 403]