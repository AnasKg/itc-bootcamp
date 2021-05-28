import requests

new_student = {
	"name": "Alex",
	"age": 18,
	"group": "Python-3",
	"phone": "+996777799993",
	"email": "tetstts@gmail.com",
	"created_by": "Anas"
}

response = requests.post(
    'http://206.189.44.36:8900/students/', data=new_student)

result = response.json()
print(result)
