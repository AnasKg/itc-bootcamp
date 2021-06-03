import requests
from bs4 import BeautifulSoup

page = requests.get('http://olympus.realpython.org/profiles')

soup = BeautifulSoup(page.text, 'html.parser')


spisok_a = soup.find_all('a')

site = 'http://olympus.realpython.org/'

for a in spisok_a:
    s = f"{site}{a['href']}"
    print(s)



