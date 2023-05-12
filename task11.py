import requests
from bs4 import BeautifulSoup


r = requests.get('http://olympus.realpython.org/profiles')
html_text = r.text

soup = BeautifulSoup(html_text, "html.parser")
result = soup.find_all('a', href=True)

for link in result:
    print(link['href'])
