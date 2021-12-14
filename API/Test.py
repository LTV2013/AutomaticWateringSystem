import requests

BASE = "http://192.168.178.23:5000/"

response = requests.get(BASE + "api/getPlantData")
print(response)
print(response.json())