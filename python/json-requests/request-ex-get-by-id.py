import requests

print('Выполняется запрос...')
res = requests.get('http://206.189.44.36:8900/students/2/')
print('Запрос завершился')

data = res.json()
print(data)
