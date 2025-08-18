from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD=os.environ.get("EMAIL_PASSWORD")
SMTP_HOST="smtp.gmail.com"

clone = requests.get("https://appbrewery.github.io/instant_pot/")
clone.raise_for_status()

soup = BeautifulSoup(clone.text,"html.parser")
price = soup.find(name="span",class_="a-price-whole").get_text()

if float(price) <= 100:
    with smtplib.SMTP(host=SMTP_HOST) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                                        to_addrs=os.environ.get("MY_SEND_TO_SEND"),
                                        msg=f"Subject:The Product Price is now ${price} below your target price, Buy now!")