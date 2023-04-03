import requests
from dotenv import load_dotenv
import os
import streamlit as st
import datetime

load_dotenv()

st.title("Workout Tracker")
st.write("This app tracks your workouts and calories burned")
query = st.text_input("What exercise did you do?")

headers = {
    "x-app-id": os.getenv("NUTRIONIX_APP_ID"),
    "x-app-key": os.getenv("NUTRIONIX_API_KEY"),
    "x-remote-user-id": "0",
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# query = input("Tell me which exercises you did: ")

if query:
    exercise_params = {
        "query": query,
    }

    response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
    result = response.json()
    print(result)

    st.write(result)


# get_workouts = requests.get(os.getenv("SHEETY_ENDPOINT"))
# result = get_workouts.json()
# print(result)

    today = datetime.datetime.now()
    today_date = today.strftime("%Y%m%d")
    today_time = today.strftime("%H:%M:%S")

    workout_data = result["exercises"]


    for workout in workout_data:
    # print(workout["name"].title())
    # print(workout["duration_min"])
    # print(workout["nf_calories"])
    # print(workout["user_input"])
    # print(workout["workout"]["date"])
    # print(workout["workout"]["time"])
    # print(workout["workout"]["exercise"])
    # print(workout["workout"]["duration"])
    # print(workout["workout"]["calories"])

        add_workout = {
            "date": today_date,
            "time": today_time,
            "exercise": workout["name"].title(),
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"],
        }

        print(add_workout)
        st.write(add_workout)
        
        add_workout = requests.post(os.getenv("SHEETY_ENDPOINT"), json={
            "workout": {
                "date": today_date,
                "time": today_time,
                "exercise": workout["name"].title(),
                "duration": workout["duration_min"],
                "calories": workout["nf_calories"],
            }
        })

# add_workout = requests.post(os.getenv("SHEETY_ENDPOINT"), json={
#     "workout": {
#         "date": "02/05/2021",
#         "time": "12:00",
#         "exercise": "Cycling",
#         "duration": "45",
#         "calories": "500",
#     }
# })

# print(add_workout.text)
