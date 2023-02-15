import requests
import json
response_API = requests.get('https://randomuser.me/api/')
#print(response_API.status_code)
data = response_API.text

#json.loads(data)

print(data)