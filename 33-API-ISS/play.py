import requests
from datetime import datetime
# response =requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# longitude = response.json()['iss_position']['longitude']
# latitude = response.json()['iss_position']['latitude']
# iss_position = (latitude, longitude)
# print(iss_position)
MY_LAT = 39.550053
MY_LONG = -105.782066

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
print(time_now)
print(sunrise.split("T")[1].split(":")[0]
print(sunset)
