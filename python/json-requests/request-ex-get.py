import requests

# response = requests.get('https:google.com')
# print(response.text)

response = requests.get('<IP-server>/students/')

result = response.json()
print(result)

