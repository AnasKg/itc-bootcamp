import requests
from requests.api import request

# response = requests.get('https:google.com')
# print(response.text)

response = requests.get('http://206.189.44.36:8900/students/')

result = response.json()

for el in result:
    for key, value in el.items():
        s = f'{key}:'
        print(key, value)
    print('-----------------------------')


