import requests
from datetime import datetime

USERNAME = "boby777"
TOKEN = "hjkjksdjkkjdakj"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# =========================
# POST (Create user) - run once
# =========================
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# =========================
# POST (Create graph) - run once
# =========================
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Bicycle Graph",
    "unit": "Minutes",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# =========================
# POST (Create pixel)
# =========================
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("Колко минути кара колело днес? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print("Create pixel:", response.text)


# =========================
# PUT (Update pixel) - uncomment to use
# =========================
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print("Update pixel:", response.text)


# =========================
# DELETE (Delete pixel) - uncomment to use
# =========================
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print("Delete pixel:", response.text)
