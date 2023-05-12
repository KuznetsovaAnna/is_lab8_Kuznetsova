import requests
from bs4 import BeautifulSoup


def find_authors(url, tags):
    global quotes

    r = requests.get(url)
    html_text = r.text

    soup = BeautifulSoup(html_text, "html.parser")
    page_content = soup.find_all('div', {'class': 'quote'})

    for line in page_content:
        quote = line.find('span', {'class': 'text'})
        quote_tags = line.find_all('a', {'class': 'tag'})

        if all(tag in [t.text for t in quote_tags] for tag in tags):
            quotes.append(quote.text.strip())


quotes = []
tags = input("Enter one or more tags separated by spaces: ").split()

i = 1
while True:
    url = f'http://quotes.toscrape.com/page/{i}/'
    r = requests.get(url)

    if "No quotes found!" in r.text:
        break

    find_authors(url, tags)
    i += 1

for quote in quotes:
    print(quote)
