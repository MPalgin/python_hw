import os
from functools import wraps
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def logger(path):
    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            log_output = [f'Log time: {datetime.now()}\n', f'Function name: {old_function.__name__}\n',
                          f'Function args: {args}, {kwargs}\n', f'Return: {old_function(*args, **kwargs)}']

            with open(path, 'a+', encoding='utf8') as log:
                for elem in log_output:
                    log.write(elem)
            return old_function(*args, **kwargs)

        return new_function

    return __logger


# Функция для проверки задания 3
@logger('log_3.log')
def get_data_from_habr(posts, keywords, main_link):
    res = []
    for data in posts:
        hubs = data.findAll("a", class_="tm-title__link")
        hubs = [hub.span.text.lower() for hub in hubs]
        matched_data = [hub for hub in hubs for key_word in keywords if key_word in hub]
        if len(matched_data):
            title_data = data.find('a', class_='tm-title__link')
            title = title_data.text.strip()
            link = title_data['href']
            date = data.find('a', class_='tm-article-datetime-published tm-article-datetime-published_link')
            date = date.time['datetime']
            date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
            date = date.strftime("%Y-%m-%d, %H:%M:%S")

            print(f'{date} - {title} - {main_link[:-7] + link}')
            res.append(f'{date} - {title} - {main_link[:-7] + link}')
        return res


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'



if __name__ == '__main__':
    test_2()
    KEYWORDS = ['сети', 'raspberry pi', 'web', 'python', 'LTE']
    MAIN_LINK = 'https://habr.com/ru/all'

    ret = requests.get(url=MAIN_LINK)
    soup = BeautifulSoup(ret.text, 'html.parser')

    posts = soup.findAll('article', class_='tm-articles-list__item')
    print(get_data_from_habr(posts, KEYWORDS, MAIN_LINK))
