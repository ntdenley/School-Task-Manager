import requests
import json

url = "https://wsu.instructure.com/api/v1/courses"
f = open('config.json')
data = json.load(f)
token = data["token"]

header = {"Authorization": "Bearer "+token }

r = requests.get(url, headers=header)

r.json()

print(r)