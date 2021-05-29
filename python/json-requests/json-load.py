import json

from requests.api import request  # Модуль для работы с json

res = {}
# Открываю json файл для получения данных
with open('load-example.json', 'r') as f:
    # json.load для загрузки json данных в dictionary
    res = json.load(f)
    res['language'] = 'Python'
    print(res)

with open('load-example.json', 'w') as f:
    json.dump(res, f)


 
