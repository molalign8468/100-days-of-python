import requests
from flight_search import FlightSearch

class FlightData:
    """A class responsible for structuring and formatting flight data."""

    def __init__(self, flight_search: FlightSearch):
        try:
            self.raw_data = flight_search.fetch_data().get("data", [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching flight data: {e}")
            self.raw_data = []

    def get_formatted_data(self):
        if not self.raw_data:
            return []
        formatted_list = [
            {
                "origin": destination.get("origin", "N/A"),
                "destination": destination.get("destination", "N/A"),
                "departureDate": destination.get("departureDate", "N/A"),
                "returnDate": destination.get("returnDate", "N/A"),
                "price": destination.get("price", {}).get("total", "N/A")
            }
            for destination in self.raw_data
        ]
        return formatted_list