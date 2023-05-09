import requests
from datetime import datetime

# -------------------creating an acc in pixela--------------------#
pixela_endpoint = "https://pixe.la/v1/users"
token = "32rfw4tgw43t63tergrtj75"
username = "wolfgang2419"
graph_id = "graph1"

user_param = {
    "token": token,
    "username": username,
    "notMinor" : "yes",
    "agreeTermsOfService": "yes",
}

#respond = requests.post(url=pixela_endpoint, json=user_param)
#print(respond.text)


# -------------- creating graph --------------------------#
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id": graph_id,
    "name": "Progamming Graph",
    "unit": "hours",
    "type": "int",
    "color": "momiji",
}

header = {
    "X-USER-TOKEN": token
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
#print(response.text)


# ----------------getting data recored in graph ---------------#
data_record_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"
today = datetime.now()
# print(today.strftime("%Y%m%d"))

record_details = {
    "date":today.strftime('%Y%m%d'),
    "quantity": input("How may hours did you progam? "),
}

response = requests.post(url=data_record_endpoint, json=record_details, headers=header)
print(response.text)


# --------------- Modifing a data that is already posted (in graph) -------------------
date_to_modify = datetime(year=2022, month=10, day=30)

date_modify_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{date_to_modify.strftime('%Y%m%d')}"
date_to_modify_details = {
    "quantity": "5"
}

#response = requests.put(url=date_modify_endpoint, json=date_to_modify_details, headers=header)
#print(response.text)


# ----------- deleting a data that is posted ------------------#
date_to_delete = datetime(year=2022, month=10, day=31)
date_to_delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{date_to_delete.strftime('%Y%m%d')}"

#response = requests.delete(url=date_to_delete_endpoint, headers=header)
#print(response.text)