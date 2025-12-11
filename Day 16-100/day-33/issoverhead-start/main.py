import time

import requests
from datetime import datetime
import smtplib
from pandas.io.formats.format import return_docstring
my_email = "borislav.2404g@gmail.com"
password = "cwybbmewaslpmxhx"
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check ISS proximity
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and
            MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True
    return False


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

    # Use UTC because API is UTC
    time_now = datetime.utcnow().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    return False


while True:
    time.sleep(60)  # Run every 60 seconds

    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg="Subject: Look Up!\n\nThe ISS is above you in the sky!"
            )
        print("Email sent!")
    else:
        print("Not time yet...")