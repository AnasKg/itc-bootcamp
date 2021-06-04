import requests
from bs4 import BeautifulSoup
import urllib

url = 'https://www.kivano.kg'

# url_2 = 'https://www.kivano.kg/product/view/sotovyy-telefon-samsung-galaxy-a52-2021-8-128gb-sm-a525f-ds-chernyy'

# print(urllib.parse.urljoin(url_2, '/itc'))

# Отправка запроса и получения response(результат/ответ)
main_page = requests.get(url)

# Создание объекта BeautifulSoup
soup = BeautifulSoup(main_page.text, 'html.parser')

category_html = soup.find_all('div', class_='leftmenu-title')

for category in category_html:
    category_name = category.text
    category_url_href = category.a.get('href')
    category_url = url + category_url_href
    print('#####################################################')
    print('Процес парсинга категория: ', category_name)
    category_page = requests.get(category_url)
    category_soup = BeautifulSoup(category_page.text, 'html.parser')
    products = category_soup.find_all('div', class_='item product_listbox oh')

    for product in products:
        product_title = product.find(class_='listbox_title').find('a').text
        product_short_description = product.find(
            class_='listbox_title').next_sibling
        product_price = product.find(class_='listbox_price').strong.text
        print('Название: ', product_title)
        print('Описание: ', product_short_description)
        print('Стоимость: ', product_price)
        print('------------------------------------------------\n')

        





