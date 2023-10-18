import requests
import json

url = "https://wsu.instructure.com/api/v1/users/self/enrollments"
f = open('config.json')
data = json.load(f)
token = data["token"]

header = {"Authorization": "Bearer "+token }

r = requests.get(url, headers=header)

r = r.json()   
# rdump = json.dumps(r, indent=4, separators=("\n ", " = "))

# print(rdump)
for item in r:
    course = item.get("course_id")
    url = "https://wsu.instructure.com/api/v1/courses/"+str(course)+"/assignments"
    r2 = requests.get(url, headers=header)
    r2 = r2.json()
    
    print()
    print(r2[0].get("course_id"))
    for x in r2:
        print(f'{x.get("name"):60} - {x.get("due_at")}')