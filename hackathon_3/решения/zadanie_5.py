import requests
from bs4 import BeautifulSoup

url = 'https://softech.kg/phones/apple-smartphone/'

# Отправка запроса и получения response(результат/ответ)
main_page = requests.get(url)

# Создание объекта BeautifulSoup
soup = BeautifulSoup(main_page.text, 'html.parser')

product_layouts = soup.find_all(
    'div', class_='product-layout')


iphones = []
for product_layout in product_layouts:
    product_url = product_layout.a.get('href')
    product_detail_page = requests.get(product_url)
    product_soup = BeautifulSoup(product_detail_page.text, 'html.parser')
    info = product_soup.find(class_='general_info')
    name = info.h1.text.strip()
    price = info.find_all(class_='price-new')[-1].text.strip()

    spisok = info.find(class_='list-unstyled')
    all_li = spisok.find_all('li')
    proizvoditel = all_li[0].a.text.strip()
    model = all_li[1].span.text.strip()
    artikul = all_li[2].span.text.strip()

    print(name, price, proizvoditel, model, artikul)
    iphones.append({
        'name': name,
        'price': price,
        'proizvoditel': proizvoditel,
        'model': model,
        'artikul': artikul
    })


