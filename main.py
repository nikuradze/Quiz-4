import requests
from bs4 import BeautifulSoup
import csv
import time

base_url = 'http://quotes.toscrape.com'
num_pages = 5
request_interval = 15

csv_file = open('quotes.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Quote', 'Author'])

for page in range(1, num_pages + 1):
    url = f'{base_url}/page/{page}'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        csv_writer.writerow([text, author])

    time.sleep(request_interval)

csv_file.close()
