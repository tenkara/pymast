import requests
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": os.getenv("PIXELA_TOKEN"),
    "username": os.getenv("PIXELA_USERNAME"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": os.getenv("PIXELA_TOKEN")
}

# requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs/{graph_config['id']}"

# today = "20230402"
today = datetime.datetime.now()
today = today.strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": input("How many kilometers did you cycle today? "),
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs/{graph_config['id']}/{today}"

# new_pixel_data = {
#     "quantity": "4.56",
# }

response = requests.put(url=update_pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)

# delete_pixel_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs/{graph_config['id']}/{today}"

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
