from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.TWILIO_ACCOUNT_SID = os.environ.get("account_sid")
        self.TWILIO_AUTH_TOKEN = os.environ.get("auth_token")
        pass
    def send_sms(self,price,origin,destination,departureDate,returnDate):
        """Sends a text message using Twilio."""
        template = f"Low Price alert! Only ${price} to fly from {origin} o {destination},on {departureDate} until {returnDate}"
        try:
            client = Client(self.TWILIO_ACCOUNT_SID, self.TWILIO_AUTH_TOKEN)
            message = client.messages.create(
                body=template,
                from_="+15074311038", 
                to='+251996940095'    
            )
            print(f"Message sent successfully with SID: {message.sid}")
        except Exception as err:
            print(f"Twilio error occurred: {err}")