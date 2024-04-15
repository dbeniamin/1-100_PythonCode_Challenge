import requests
from datetime import datetime

""" https://pixe.la/ and https://docs.pixe.la/ are used during this project """

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "benjamin-test1ng"
TOKEN = "randomgenerated123!@#$55token"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
""" use the below statement to create the user and the token """
""" at fist use you have to select a user name and whatever token you want """
# statements used to create the user and token

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# statement to create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# print(graph_endpoint)  # check value print statement
graph_params = {
    "id": "graph1",
    "name": "testgraph",
    "unit": "Kg",
    "type": "float",
    "color": "sora",
    "json": "testing"
}

headers_param = {
    "X-USER-TOKEN": TOKEN
}

""" make the request to print the graph you need """
# ## -------------- IMPORTANT NOTE - READ BELOW -------------- ###
# json= graph_params is taken in consideration as the body of the request
# use the params= arugment and not the json the request will return an error message
# {"message":"Request body is empty.","isSuccess":false}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers_param)
# print(response.text)

# https://pixe.la/v1/users/a-know/graphs/test-graph.html - acces the graph
# replace a-know with your username and test-graph with graph id

""" https://www.w3schools.com/python/python_datetime.asp - how to format date and time based on what format you need """

# today = datetime.now()  # in case you need another day pass the values in the date time request
# i.e. today = datetime(year=2024, month=2, day= 10) and will get transformed based on the formating used
today = datetime(year=2024, month=2, day=10)

add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
add_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "11.1",
}

""" use the below format to create a pixel for a specific activity """
# response = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=headers_param)
# print(response.text)

""" use the below format to edit an already creeated pixel """
edit_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
edit_pixel_params = {
    "quantity": "7"
}
# response = requests.put(url=edit_pixel_endpoint, json=edit_pixel_params, headers=headers_param)
# print(response.text)


""" use the below format to delete an already creeated pixel """
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers_param)
print(response.text)
