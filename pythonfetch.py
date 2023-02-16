import requests

response = requests.get('https://randomuser.me/api/?results=100&gender=male')

data = response.json()

male_users = data['results']


for i, user in enumerate(male_users):

  name = f"{user['name']['title']} {user['name']['first']} {user['name']['last']}"
  email = user['email']
  phone = user['phone']

  print(f"{i+1}. {name}\n phone: {phone}\n email: {email}")


