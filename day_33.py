### API - ISS - Tracker ###
import requests
from datetime import datetime

MY_LAT = 44.426765
MY_LONG = 26.102537

""" https://www.webfx.com/web-development/glossary/http-status-codes/ """
""" https://www.latlong.net/ -> use to convert/find locations """
""" https://api.sunrise-sunset.org/json   -> sunrise / sunset API """
""" https://sunrise-sunset.org/api -> documentation for the used API"""

# use the .get() to acces the api
response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response.status_code)
# .raise_for_status() -  will raise a HTTTP error if the returned code is unsuccesful

response.raise_for_status()
# can have passed arguments to extract various details and arguments like iss_position, latitude, etc
data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)

# api call example
# endpoint ? param name = value & etc

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters,)
response.raise_for_status()
data = response.json()
# use split method to get the hours
# split by "T", index the result to further split , then by ":" and in the end select the index to get i.e. [0]
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

# use the below line to get date and time
time_now = datetime.now()
print(time_now.hour)












