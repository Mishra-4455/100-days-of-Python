import requests
from datetime import datetime

USERNAME = "abhinav5"
TOKEN = "sjdioajdskljawodno"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# pixela = requests.post(url=pixela_endpoint, json=user_params)
# print(pixela.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime(year=2026, month=9, day=29)
formated_date = today.strftime("%Y%m%d")

input_endpoint = f"{graph_endpoint}/{graph_config["id"]}"
input_config = {
    "date": formated_date,
    "quantity": "10"
}

delete_endpoint = f"{input_endpoint}/{formated_date}"

update_endpoint = f"{input_endpoint}/{formated_date}"
update_config = {
    "quantity": "2.2"
}

# creating a graph
# graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# crating a pixel
# graph = requests.post(url=input_endpoint, json=input_config, headers=headers)

# deleting a pixel
# graph = requests.delete(url=delete_endpoint, headers=headers)

# updating a pixel
graph = requests.put(url=update_endpoint, json=update_config, headers=headers)
print(graph.text)