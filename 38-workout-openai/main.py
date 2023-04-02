import requests
from dotenv import load_dotenv
import os

load_dotenv()

headers = {
    "x-app-id": os.getenv("NUTRIONIX_APP_ID"),
    "x-app-key": os.getenv("NUTRIONIX_API_KEY"),
    "x-remote-user-id": "0",
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# query = input("Tell me which exercises you did: ")

# exercise_params = {
#     "query": query,
    
# }

# response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
# result = response.json()
# print(result)

get_workouts = requests.get(os.getenv("SHEETY_ENDPOINT"))
result = get_workouts.json()
print(result)


add_workout = requests.post(os.getenv("SHEETY_ENDPOINT"), json={
    "workout": {
        "date": "02/05/2021",
        "time": "12:00",
        "exercise": "Cycling",
        "duration": "45",
        "calories": "500",
    }
})

print(add_workout.text)
