import requests
import os
import dotenv
from twilio.rest import Client

dotenv.load_dotenv()

VIRTUAL_TWILIO_NUMBER = os.getenv("MY_TWILIO_NUMBER")
VERIFIED_NUMBER = os.getenv("RECIPIENT_NUMBER")

TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_NAME = "TSLA"     # See how this is selected: https://www.alphavantage.co/documentation/
NEWS_QUERY = "Tesla"
PRICE_CHANGE_PERCENTAGE = 5

news_parameters = {
    "q": NEWS_QUERY,
    "apiKey": NEWS_API_KEY,
}

stocks_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stocks_parameters)
stock_response.raise_for_status()
data = stock_response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
yesterday_closing_price = data_list[0]["4. close"]

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(f"Diff = {diff_percent}%")

# Fetch the first 3 articles for the NEWS_QUERY.
if abs(diff_percent) > PRICE_CHANGE_PERCENTAGE:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for
        article in three_articles]

    # Send a separate message with each article's title and description to your phone number.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
