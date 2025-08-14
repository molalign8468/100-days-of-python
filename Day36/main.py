import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
PERCENTAGE_THRESHOLD = 5.0
NUMBER_OF_NEWS_ARTICLES = 3

ALPHA_VANTAGE_URL = "https://www.alphavantage.co/query"
NEWS_API_URL = "https://newsapi.org/v2/everything"
ALPHA_VANTAGE_API_KEY = os.environ.get("ALPHA_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.environ.get("account_sid")
TWILIO_AUTH_TOKEN = os.environ.get("auth_token")


def get_stock_data():
    """Fetches daily stock data for the specified stock."""
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    try:
        response = requests.get(url=ALPHA_VANTAGE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

def get_news_data():
    """Fetches top news articles for the specified company."""
    params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    try:
        response = requests.get(url=NEWS_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

def send_sms(body_text):
    """Sends a text message using Twilio."""
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=body_text,
            from_="+15074311038", 
            to='+251996940095'    
        )
        print(f"Message sent successfully with SID: {message.sid}")
    except Exception as err:
        print(f"Twilio error occurred: {err}")


def run_stock_checker():
    """Main function to check stock price and send news alerts."""
    stock_data = get_stock_data()
    if not stock_data or "Time Series (Daily)" not in stock_data:
        print("Failed to get stock data or data is malformed.")
        return

    daily_data = stock_data["Time Series (Daily)"]
    data_keys = list(daily_data.keys())
    
    if len(data_keys) < 2:
        print("Not enough daily data to perform a comparison.")
        return
        
    yesterday_data = daily_data[data_keys[0]]
    day_before_yesterday_data = daily_data[data_keys[1]]
    
    yesterday_close = float(yesterday_data["4. close"])
    day_before_close = float(day_before_yesterday_data["4. close"])
    
    price_difference = yesterday_close - day_before_close
    percentage_change = (price_difference / day_before_close) * 100
    
    print(f"TSLA percentage change: {percentage_change:.2f}%")
    
    if abs(percentage_change) >= PERCENTAGE_THRESHOLD:
        print("Significant price change detected. Fetching news...")
        news_data = get_news_data()
        if not news_data or "articles" not in news_data:
            print("Failed to get news data or data is malformed.")
            return

        # Prepare and send SMS messages
        articles = news_data["articles"][:NUMBER_OF_NEWS_ARTICLES]
        status_symbol = "🔺" if percentage_change > 0 else "🔻"
        
        for article in articles:
            headline = article.get("title", "No Title")
            brief = article.get("description", "No Brief")
            
            message_body = (
                f"{STOCK}: {status_symbol}{abs(percentage_change):.2f}%\n"
                f"Headline: {headline}\n"
                f"Brief: {brief}"
            )
            send_sms(message_body)

run_stock_checker()