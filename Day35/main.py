import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")


OW_API_KEY = os.environ.get("OW_API_KEY")
LAT = 7.2438769
LON =37.9049922
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat":LAT,
    "lon":LON,
    "appid":OW_API_KEY,
    "cnt":4
}

response = requests.get(url=BASE_URL,params=parameters)
response.raise_for_status()
wether_data = response.json()["list"]



is_rain = False

for i in range(len(wether_data)):
    if wether_data[i]["weather"][0]["id"] < 700:
        is_rain =True
if is_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='It is going to rain today, Remember to bring an umbrella',
        from_="+1 507 431 1038",
    to='+251996940095'
    )
    print(message.sid)
    print(message.status)