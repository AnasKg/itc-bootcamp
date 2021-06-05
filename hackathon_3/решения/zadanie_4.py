import requests
from bs4 import BeautifulSoup

url = 'https://softech.kg'

# Отправка запроса и получения response(результат/ответ)
main_page = requests.get(url)

# Создание объекта BeautifulSoup
soup = BeautifulSoup(main_page.text, 'html.parser')

product_layouts = soup.find_all(
    'div', class_='product-layout col-lg-3 col-md-3 col-sm-3 col-xs-12')

products = []
for product_layout in product_layouts:
    product_price = product_layout.find(class_='price').text.strip()
    product_name = product_layout.find(class_='name').a.text.strip()
    product_short_description = product_layout.find(class_='description-small').text.strip()
    print(product_name, product_price)
    products.append({
        'name': product_name,
        'description': product_short_description,
        'price': product_price
    })

print(products)

