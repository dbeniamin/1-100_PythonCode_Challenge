class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, dest_city, dest_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.dest_city = dest_city
        self.dest_airport = dest_airport
        self.out_date = out_date
        self.return_date = return_date
