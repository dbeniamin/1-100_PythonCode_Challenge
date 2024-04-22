import requests
import os
from pprint import pprint

sheety_url = "https://api.sheety.co/bb393f4c1ca3e623fd70881676addab6/flightDeals/prices"

SHEETY_FLIGHT_TOKEN = os.environ["SHEETY_FLIGHT_TOKEN"]

headers_auth = {
    "Authorization": f"Bearer {SHEETY_FLIGHT_TOKEN}"
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_data(self):
        response = requests.get(url=sheety_url, headers=headers_auth)
        response.raise_for_status()
        received_data = response.json()
        self.destination_data = received_data["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_url}/{city["id"]}",
                json=new_data,
                headers=headers_auth
            )
            print(response.text)
