import requests
import os
from flight_data import FlightData

TEQUILA_URL = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]
headers_tequila = {
    "apikey": TEQUILA_API_KEY
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_city_code(self, city_name):
        # define headers to authenticate using the token
        headers_tequila = {
            "apikey": TEQUILA_API_KEY
        }
        get_city_code_url = f"{TEQUILA_URL}/locations/query"
        # define the query with the details to be extracted
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=get_city_code_url, headers=headers_tequila, params=query)
        response.raise_for_status()
        # use comprehension to extract details from the json format
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def find_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        headers_search = {
            "apikey": TEQUILA_API_KEY
        }
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 10,
            "one_for_city": 1,
            "adults": 2,
            "curr": "EUR",
            "max_sector_stopovers": 0
        }
        response = requests.get(url=f"{TEQUILA_URL}/v2/search", headers=headers_tequila, params=query)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        fligh_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            dest_city=data["route"][0]["cityTo"],
            dest_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
        )
        print(f"{fligh_data.dest_city}: EUR{fligh_data.price}")
        return fligh_data
