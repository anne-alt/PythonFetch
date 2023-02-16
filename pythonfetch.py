import requests

# for item in range(10):
response = requests.get('https://randomuser.me/api/?results=100&gender=male')

data = response.json()

male_users = data['results']

# print(male_users)

for i, user in enumerate(male_users):
  print(f"{i+1}. {user['name']['title']} {user['name']['first']} {user['name']['last']} {user['email']}")


