import requests

print('Выполняется запрос')
response = requests.delete(
    'http://206.189.44.36:8900/students/3/')

print('Запрос завершился')
print(response.text)
