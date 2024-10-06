import requests
from bs4 import BeautifulSoup
from datetime import datetime


KEYWORDS = ['сети', 'raspberry pi', 'web', 'python', 'LTE']
MAIN_LINK = 'https://habr.com/ru/all'

ret = requests.get(url=MAIN_LINK)
soup = BeautifulSoup(ret.text, 'html.parser')

posts = soup.findAll('article', class_='tm-articles-list__item')

for data in posts:
    hubs = data.findAll("a", class_="tm-title__link")
    hubs = [hub.span.text.lower() for hub in hubs]
    matched_data = [hub for hub in hubs for key_word in KEYWORDS if key_word in hub]
    if len(matched_data):
        title_data = data.find('a', class_='tm-title__link')
        title = title_data.text.strip()
        link = title_data['href']
        date = data.find('a', class_='tm-article-datetime-published tm-article-datetime-published_link')
        date = date.time['datetime']
        date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
        date = date.strftime("%Y-%m-%d, %H:%M:%S")

        print(f'{date} - {title} - {MAIN_LINK[:-7] + link}')
