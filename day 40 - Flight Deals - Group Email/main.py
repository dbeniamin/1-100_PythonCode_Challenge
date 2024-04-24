from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "BUH"

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_code(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    print(flight.price)
    if flight is None:
        continue

    if flight.price < destinations[destination_code]["price"]:
        ### set up to send email to the created list on the Google sheet

        users = data_manager.get_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]
        message = (f"Low price alert ! Only E {flight.price} to fly from {flight.origin_city} to"
                   f" {flight.destination_city} from {flight.out_date} to {flight.return_date}")
        if flight.stop_overs > 0:
            message += f"\n Flight has {flight.stop_overs} stop over, via {flight.via_city}"

        notification_manager.send_emails(emails, message)

        ### twilio setup to send sms to yourself
        # notification_manager.send_sms(
        #     message=f"Low price alert! Only £{flight.price} "
        #             f"to fly from {flight.origin_city}-{flight.origin_airport} to "
        #             f"{flight.destination_city}-{flight.destination_airport}, "
        #             f"from {flight.out_date} to {flight.return_date}."
        # )
