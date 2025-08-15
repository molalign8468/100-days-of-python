import os
import requests
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    """A class to handle interactions with the Amadeus Flight Search API."""

    def __init__(self, origin: str = "PAR", max_price: int = 200):
        self.flight_endpoint = "https://test.api.amadeus.com/v1/shopping/flight-destinations"
        self.auth_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"

        self.client_id = os.environ.get("AMADEUS_API")
        self.client_secret = os.environ.get("AMADEUS_SECRET")
        self.origin = origin
        self.max_price = max_price
        
        self.session = requests.Session()
        self.access_token = self._get_access_token()
        self.session.headers.update({"Authorization": f"Bearer {self.access_token}"})

    def _get_access_token(self):
        if not self.client_id or not self.client_secret:
            raise ValueError("AMADEUS_API or AMADEUS_SECRET environment variables are not set.")

        auth_data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }

        try:
            response = requests.post(
                url=self.auth_endpoint,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                data=auth_data
            )
            response.raise_for_status()
            token_data = response.json()
            return token_data.get("access_token")
        except requests.exceptions.RequestException as e:
            print(f"Error getting access token: {e}")
            raise

    def fetch_data(self):
        params = {
            "origin": self.origin,
            "maxPrice": self.max_price
        }

        try:
            response = self.session.get(url=self.flight_endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching flight data: {e}")
            raise