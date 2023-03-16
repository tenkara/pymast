import requests
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
}

response = requests.get(url="http://api.sunrise-sunset.org/json")
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(sunrise)
print(sunset)
