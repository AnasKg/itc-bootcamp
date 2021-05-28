import requests

new_student = {
	"name": "Aibek",
	"age": 23,
	"group": "Python-2",
	"phone": "+996777744444",
	"email": "aibek@gmail.com",
	"created_by": "Sezim"
}

response = requests.post(
    'http://206.189.44.36:8900/students/', data=new_student)

result = response.json()
print(result)
