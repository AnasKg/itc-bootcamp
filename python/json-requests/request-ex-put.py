import requests

updated_student = {
	"name": "Aibek",
	"age": 23,
	"group": "Python-3",
	"phone": "+99655553333",
	"email": "aibek@gmail.com",
	"created_by": "Sezim"
}

print('Выполняется запрос')
response = requests.put(
    'http://206.189.44.36:8900/students/3/', data=updated_student)

print('Запрос завершился')

result = response.json()
print(result)
