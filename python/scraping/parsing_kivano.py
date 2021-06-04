import requests
from bs4 import BeautifulSoup

url = 'https://www.kivano.kg'

# Отправка запроса и получения response(результат/ответ)
main_page = requests.get(url)

# Создание объекта BeautifulSoup
soup = BeautifulSoup(main_page.text, 'html.parser')

# Нахождение тегов div с классом 'product_box'
product_box = soup.find_all('div', class_='product_box')
print('Количество: ', len(product_box))

for product in product_box:
    # достаем 
    product_title = product.find(class_='product_title').text
    product_price_span = product.find(class_='product_price').find_all('span')
    product_price = product_price_span[-1].text
    message = f'{product_title}-{product_price}'
    print(message)
    print('---------------------------------------')



