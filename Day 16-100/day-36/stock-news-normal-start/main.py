import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

WHATSAPP_FROM = os.getenv("WHATSAPP_FROM")
WHATSAPP_TO = os.getenv("WHATSAPP_TO")

CONTENT_SID = os.getenv("CONTENT_SID")
CONTENT_VARIABLES = os.getenv("CONTENT_VARIABLES")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# --- checks ---
required = {
    "STOCK_API_KEY": STOCK_API_KEY,
    "NEWS_API_KEY": NEWS_API_KEY,
    "TWILIO_ACCOUNT_SID": TWILIO_ACCOUNT_SID,
    "TWILIO_AUTH_TOKEN": TWILIO_AUTH_TOKEN,
    "WHATSAPP_FROM": WHATSAPP_FROM,
    "WHATSAPP_TO": WHATSAPP_TO,
    "CONTENT_SID": CONTENT_SID,
    "CONTENT_VARIABLES": CONTENT_VARIABLES,
}
missing = [k for k, v in required.items() if not v]
if missing:
    raise RuntimeError(f"Missing in .env: {', '.join(missing)}")

# --- STEP 1: Stock prices ---
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
payload = response.json()

time_series = payload.get("Time Series (Daily)")
if not time_series:
    raise RuntimeError(f"AlphaVantage error: {payload}")

data_list = list(time_series.values())
yesterday_close = float(data_list[0]["4. close"])
day_before_close = float(data_list[1]["4. close"])

difference = yesterday_close - day_before_close
up_down = "🔺" if difference > 0 else "🔻"

# по-логично % спрямо предишния ден
diff_percent = round((difference / day_before_close) * 100)

print("Yesterday close:", yesterday_close)
print("Day before close:", day_before_close)
print("Diff %:", diff_percent)

# --- STEP 2: News (ако искаш) ---
# Оставяме го, но WhatsApp ще прати независимо, за да тестваш.
if abs(diff_percent) > 1:
    news_params = {"apiKey": NEWS_API_KEY, "qInTitle": COMPANY_NAME, "pageSize": 3, "language": "en"}
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json().get("articles", [])[:3]

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {a.get('title','')}\nBrief: {a.get('description','')}"
        for a in articles
    ]
    print(formatted_articles)

# --- WhatsApp send (template message) ---
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

body = "\n\n".join(formatted_articles)

msg = client.messages.create(
    from_="whatsapp:+14155238886",
    to="whatsapp:+359877771139",
    body=body
)
print("SID:", msg.sid, "Status:", msg.status)

