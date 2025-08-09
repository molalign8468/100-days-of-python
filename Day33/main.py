import requests
import smtplib
from datetime import datetime
import time

MY_LAT = 51.507351 
MY_LONG = -0.127758 

MY_EMAIL = "hasetgetahun7@gmail.com" # Update with your Email
PASSWORD=""#update with your Gmail App Password
SMTP_HOST="smtp.gmail.com"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <=sunrise:
        return True



def main():
    if is_iss_overhead() and is_night():
        with smtplib.SMTP(SMTP_HOST) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs="molalign229@gmail.com",msg="Subject:Look up \n\n\ The ISS is above your sky")

while True:
    time.sleep(60)
    main()



