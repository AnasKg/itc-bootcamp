import json


with open('user_data.json', 'r') as file:
    data = json.load(file)
    for user in data:
        print(user['id'], user['first_name'], user['last_name'])
    
