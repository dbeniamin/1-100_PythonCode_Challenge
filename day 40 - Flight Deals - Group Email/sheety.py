import requests
import os

BEARER = os.getenv("Bearer token for sheety API")
USERNAME = os.getenv("API Username Sheety")

PROJECT = "flightDealUsers"
SHEET = "users"

sheety_url = "https://api.sheety.co"


def post_new_row(first_name, last_name, email):
    endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}"
    url = sheety_url + endpoint_url
    headers = {
        "Authorization": f"Bearer {BEARER}",
        "Content-Type": "application/json",
    }
    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,

        }
    }

    response = requests.post(url=url, headers=headers, json=body)
    response.raise_for_status()
    print(response.text)
