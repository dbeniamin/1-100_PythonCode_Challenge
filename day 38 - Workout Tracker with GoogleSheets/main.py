import requests
from datetime import datetime
import os


nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/bb393f4c1ca3e623fd70881676addab6/workoutTracker/workouts"

BEARER_TOKEN = os.environ["TEST_SHEETY_TOKEN"]
APP_ID = os.environ["APP_NUTRI_ID"]
API_KEY = os.environ["API_NUTRI_KEY"]

WEIGHT_KG = input("How much do you weight? in kg: ... ")
HEIGHT_CM = input("How tall are you? in cm : ... ")
AGE_YEARS = input("How old are you?: ... ")
NAME = input("What is your name?: ...")

header_bearer = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}


headers_settings = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
# ##  setup to get the  data from nutritionix  ###
personal_params = {
    "query": input("What training did you do today ?: ... \n"),
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE_YEARS
}

response = requests.post(url=nutritionix_endpoint, headers=headers_settings, json=personal_params)
response.raise_for_status()
workout_data = response.json()
# print(workout_data)  # print statement to check the values

# ## date and time setup  ###

today = datetime.now()
date_param = today.strftime("%d/%m/%Y")
time_param = today.strftime("%H:%M:%S")
# print(date_param, time_param)  # print statement to check the values

# ## Extracting values from nutritionix response ###

"""  ------------ IMPORTANT NOTICE ------------ """
""" this method works for the case where you have only one exercise loged """
# duration_value = workout_data["exercises"][0]["duration_min"]
# calories_value = workout_data["exercises"][0]["nf_calories"]
# activity_name_value = workout_data["exercises"][0]["name"]
# print(duration_value, calories_value, activity_name_value)


"""  ------------ IMPORTANT NOTICE - Read below commments ------------ """
# ## ----------------------- shetty params ----------------------- ###
# ## use a for loop so the data can be extracted if the user has more than one input ###
# ## i.e. in case the user input is 2 or more different activities ###


for exercise in workout_data["exercises"]:
    # loop in the json file passing the "exercises" param

    sheet_input = {
        "workout": {
            # pass date and time params in separate collumns in google worksheets based on the date and time formating.

            "date": date_param,
            "time": time_param,
            # extract and save the data based on the passed keys i.e. "name", "duration", "nf_calories"
            # key can be observerd in the first response json data type.

            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
            "name": NAME.title()
        }
    }
    response_sheety = requests.post(url=sheety_endpoint, json=sheet_input, headers=header_bearer)
    # print(response_sheety.text)  # print statement to check the values


