import os
import requests
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager

def main():
    try:
        flight_search = FlightSearch()
        flight_data_processor = FlightData(flight_search)
        data_manager = DataManager()
        notification_manager = NotificationManager()
    except ValueError as e:
        print(f"Initialization error: {e}. Please check your environment variables.")
        return
    try:
        flight_data = flight_data_processor.get_formatted_data()
        
        doc_data = data_manager.fetch_data()
    except (requests.exceptions.RequestException, KeyError) as e:
        print(f"Error fetching data: {e}")
        return
    price_sheet = {
        item.get("iataCode"): item.get("lowestPrice") 
        for item in doc_data.get("prices", [])
    }
    
    for flight in flight_data:
        destination_iata = flight.get("destination")
        
        if destination_iata in price_sheet:
            lowest_price = price_sheet[destination_iata]
            flight_price = float(flight.get("price", 0))

            if flight_price <= float(lowest_price):
                notification_manager.send_sms(
                    price=flight_price,
                    origin=flight.get("origin"),
                    destination=destination_iata,
                    departureDate=flight.get("departureDate"),
                    returnDate=flight.get("returnDate")
                )
                print(f"Found a deal to {destination_iata} for ${flight_price}!")

if __name__ == "__main__":
    main()