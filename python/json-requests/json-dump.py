import json # Модуль для работы с json

student = {
    'name': 'Alex',
    'age': 18,
    'phone': '+996777444333'
}

# Открываю файл для записи
with open('dump-ex-2.json', 'w') as file:
    # json.dump для записи в json формат
    json.dump(student, file)

