import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    """A class to handle interactions with the Google Sheet API via Sheety."""
    def __init__(self):
        """Initializes the DataManager with API endpoint and authorization header."""
        self.endpoint = "https://api.sheety.co/21bf6521e405f3a9823fecb48370630d/flightDeals/prices"
        self.session = requests.Session()
        secret_token = os.environ.get("SECRET")
        if not secret_token:
            raise ValueError("SECRET environment variable is not set.")
        self.session.headers.update({"Authorization": f"Bearer {secret_token}"})

    def fetch_data(self):
        try:
            response = self.session.get(url=self.endpoint)
            response.raise_for_status() 
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching data: {e}")
            raise