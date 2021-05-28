import requests

# response = requests.get('https:google.com')
# print(response.text)

response = requests.get('http://206.189.44.36:8900/students/')

result = response.json()
print(result)

