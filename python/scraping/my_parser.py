import requests
from bs4 import BeautifulSoup

# Выполнение GET запроса на сайт
resp = requests.get('http://olympus.realpython.org/profiles/dionysus')

# Получение результата(response) в виде string 
html = resp.text
print(html)
# Создание объекта класса BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# метод get_text которые возвращает только тексты без html
print(soup.get_text())

# метод find_all, который принимает название тега и возвращает список этих тегов
imgs = soup.find_all('img')
print(imgs)

for el in imgs:
    # Получение значения атрибута src тега img
    print(el['src'])

# Получить заглавие сайта
title_name = soup.title.string
print(title_name)


