import requests
from bs4 import BeautifulSoup


def find_authors(url):
    global authors

    r = requests.get(url)
    html_text = r.text

    soup = BeautifulSoup(html_text, "html.parser")
    page_content = soup.find_all('div', {'class': 'quote'})

    for line in page_content:
        author = line.find('small', {'class': 'author'}).text
        quote = line.find('span', {'class': 'text'}).text

        if author not in authors:
            authors.update({author: [quote]})
        else:
            authors[author].append(quote)


authors = {}

i = 1
while True:
    url = f'http://quotes.toscrape.com/page/{i}/'
    r = requests.get(url)

    if "No quotes found!" in r.text:
        break

    find_authors(url)
    i += 1

result = sorted(authors, key=lambda x: len(authors[x]), reverse=True)
print(result)

for i in range(len(result)):
    print(f'{result[i]}: {len(authors[result[i]])}')
