import requests
import json

url = "https://wsu.instructure.com/api/v1/courses"
f = open('config.json')
data = json.load(f)
token = data["token"]

header = {"Authorization": "Bearer "+token, "enrollment_state": "active" }

r = requests.get(url, headers=header)

r = r.json()   
#r = json.dumps(r, indent=4)

for item in r:
    print(item.get("name"))