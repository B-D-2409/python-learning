import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Зарежда променливите от .env файла в средата на изпълнение
load_dotenv()

# --- Ключове и номера се зареждат от средата (тези имена трябва да са във вашия .env файл!) ---
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.environ.get("TWILIO_FROM_NUMBER")
MY_PHONE_NUMBER = os.environ.get("MY_PHONE_NUMBER")

# OpenWeatherMap ключ
API_KEY_FORECAST = os.environ.get("OWM_API_KEY_FORECAST")

# --- OpenWeatherMap API част ---
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat": 48.135124,
    "lon": 11.581981,
    "appid": API_KEY_FORECAST, # Използваме променливата от .env
    "cnt": 4,
}

# Изпълнение на заявката с обработка на грешки
try:
    response = requests.get(OWN_Endpoint, params=weather_params)
    response.raise_for_status()
    weather_data = response.json()
except requests.exceptions.RequestException as e:
    # При грешка 401 (Unauthorized) това ще бъде отпечатано
    print(f"Грешка при заявката към OpenWeatherMap: {e}")
    exit() # Спираме скрипта при неуспешна заявка

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    # Кодове под 700 означават лошо време (дъжд, сняг, гръмотевици и т.н.)
    if int(condition_code) < 700:
       will_rain = True

# --- Twilio SMS част ---
if will_rain:
    # Започваме Twilio комуникация
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_=TWILIO_FROM_NUMBER,
        to=MY_PHONE_NUMBER,
    )

    print(f"Twilio Status: {message.status}")
else:
    print("Не се очаква лошо време в следващите 6 часа. SMS не е изпратен.")