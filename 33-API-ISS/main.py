import requests
response =requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

longitude = response.json()['iss_position']['longitude']
latitude = response.json()['iss_position']['latitude']
iss_position = (latitude, longitude)
print(iss_position)
