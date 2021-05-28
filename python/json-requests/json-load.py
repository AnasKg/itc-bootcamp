import json  # Модуль для работы с json

# Открываю json файл для получения данных
with open('load-example.json', 'r') as f:
    # json.load для загрузки json данных в dictionary
    res = json.load(f)
    print(res)
 
