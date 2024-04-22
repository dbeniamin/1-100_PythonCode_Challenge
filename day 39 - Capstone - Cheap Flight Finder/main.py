# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


""" use below reference for time date manipulation"""
""" https://stackoverflow.com/questions/4541629/how-to-create-a-datetime-equal-to-15-minutes-ago/4541668 """


data_manager = DataManager()
sheet_data = data_manager.get_data()
# print(sheet_data) # print statement to check the progress

notification_manager = NotificationManager
flight_search = FlightSearch()
ORIGIN_CITY_IATA = "BUH"


if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch

    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_city_code(row["city"])
    print(f"sheet_data\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_code()

tomorrow = datetime.now() + timedelta(days=1)
four_months_from_today = datetime.now() + timedelta(days=(4 * 30))

for destination in sheet_data:
    flight = flight_search.find_flight(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=four_months_from_today
    )

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low Price Flight for {flight.price} to fly from: {flight.origin_city} to {flight.dest_city},"
                    f"from {flight.out_date} to {flight.return_date}"
        )
