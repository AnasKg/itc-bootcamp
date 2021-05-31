import requests

new_student = {
	"name": "Bermet",
	"age": 10,
	"group": "Python-3",
	"phone": "+996777444333",
	"email": "bermet@gmail.com",
	"created_by": "Anas"
}

response = requests.post(
    'http://206.189.44.36:8900/students/', data=new_student)

result = response.json()
print(result)
