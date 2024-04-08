# ## Rain check Alert ###
# ## Send SMS / email with an API ###
# ## API keys and authentications ###
import requests
from twilio.rest import Client
import os

""" https://www.twilio.com/en-us - can be set up and used to send regular sms """
""" you need to set up your free twilio account """
""" you need to set up your https://api.openweathermap.org and get your own api key """
""" https://www.pythonanywhere.com/ can be used to run the code as a dayli script """

""" to get a virtual env on your machine with windows and pycharm use the following commands : """
# Run the following command to create a virtual environment named venv: python -m venv venv
# Activate the virtual environment: venv\Scripts\activate
# ********* export command will not work !!!! *********
# use the set command to set environment variables
# set KEY_NAME=the_actual_key_you_want_to_hide

""" https://stackoverflow.com/questions/42708389/how-to-set-environment-variables-in-pycharm """

MY_LAT = 44.426765
MY_LONG = 26.102537
API_KEY = os.environ["TEST_ENV_KEY"]
API_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "enter your own personal sid"
auth_token = "enter your own personal auth token"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "units": "metric",
    "cnt": 4,
    "appid": API_KEY,
}

response = requests.get(API_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

# tap in the weather id
# complete json is a dict {} -> provide values to get i.e ["list"] -> provide the index you want from the list
# repeat until you reach the value you want.

""" print(weather_data) -> print(weather_data["list"]) -> """
""" ->  print(weather_data["list"][0]) -> print(weather_data["list"][0]["weather"]) -> """
""" -> print(weather_data["list"][0]["weather"][0]) -> print(weather_data["list"][0]["weather"][0]["id"])"""

print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella !")  # print statement with a debug / testing purpose

    """ twilio template code to to call the client and send sms """
    # client = Client(account_sid, auth_token)
    # # message template available on twilio
    # message = client.messages \
    #     .create(
    #     body = "Enter the text of your message",
    #     from = "+1234567890"),
    #     to = "number that receives the message, can add multiple numbers to get verified on twilio"
    # )
    # # print the status to see if the sms was sent succesfully
    # print(message.status)
