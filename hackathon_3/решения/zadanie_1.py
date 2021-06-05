import requests

response = requests.get('http://206.189.44.36:8900/students/')

students = response.json()

for student in students:
    status = 'Совершеннолетний'
    if student['age'] < 18:
        status = 'Несвершеннолетний'
    message = f"{student['name']}, {student['age']}, {student['phone']}, {status}"
    print(message)

