import requests
from datetime import datetime
import smtplib
import time
from dotenv import load_dotenv
import os

load_dotenv()

MY_LAT = 39.550053
MY_LONG = -105.782066

my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    longitude = float(response.json()['iss_position']['longitude'])
    latitude = float(response.json()['iss_position']['latitude'])

# Is my position within +5 or -5 degrees of the ISS position?

    if (MY_LAT - 5) <= latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= longitude <= (MY_LONG + 5):
        return True
    
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']
    time_now = datetime.now()
    if time_now.hour >= sunset.split("T")[1].split(":")[0] or time_now.hour <= sunrise.split("T")[1].split(":")[0]:
        return True
    time_now = datetime.now()
    if time_now >= sunset.split("T")[1].split(":")[0] or time_now <= sunrise.split("T")[1].split(":")[0]:
        print("It's dark")
    
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com") # Connect to the SMTP server
        connection.starttls() # Encrypt the connection
        connection.login(user=my_email, password=password) # Log in to the email server
        connection.sendmail(
            from_addr=my_email,
            to_addrs="my_email",
            msg="Subject:Look Up\n\nThe ISS is above you in the sky."
        )
        connection.close()




