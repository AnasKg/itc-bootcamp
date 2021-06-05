import requests

print('Выполняется запрос')
response = requests.delete(
    'http://206.189.44.36:8900/students/8/')

print('Запрос завершился')

if response.status_code == 204:
    print('Успешно удалено')
else:
    print(response.text)