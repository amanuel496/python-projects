import smtplib
import time
import requests
from datetime import datetime, timezone

MY_EMAIL = "email"  # Your email
PASSWORD = "password"  # Your password

MY_LAT = 39.690452  # Your latitude
MY_LONG = -104.902140  # Your longitude


# Your position is within +5 or -5 degrees of the ISS position.
def check_iss_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    higher_lat_bound = MY_LAT + 5
    lower_lat_bound = MY_LAT - 5
    higher_long_bound = MY_LONG + 5
    lower_long_bound = MY_LONG - 5
    if (lower_lat_bound <= iss_latitude <= higher_lat_bound) and (
            lower_long_bound <= iss_longitude <= higher_long_bound):
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now(timezone.utc).hour

    if time_now >= sunset or time_now <= sunrise:
        return True

    return False


counter = 0

while True:
    if counter % 3600 == 0:
        print(counter / 3600)
    if check_iss_location():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject: ISS Satellite\n\n"
                                                                           "Look up, ISS satellite is above your head.")

    if check_iss_location() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject: ISS Satellite Night\n\n"
                                                                           "Look up, ISS satellite is above your head.")
    counter += 1
    time.sleep(60)
