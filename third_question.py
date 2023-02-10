'''Сколько HTML-тегов в коде главной страницы сайта greenatom.ru? 
Сколько из них содержит атрибуты? 
Напиши скрипт на Python, который выводит ответы на вопросы выше '''

from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


def create_session_header() -> requests.Session():
    with requests.Session() as session:
        session.headers = {"User-Agent": UserAgent().firefox}
    return session


def parse_page(session: requests.Session, link: str) -> BeautifulSoup:
    return BeautifulSoup(session.get(link).text, 'html.parser')


def count_all_tags_on_page(soup: BeautifulSoup) -> int:
    return len(soup.findAll())


def count_tags_with_attributes(soup: BeautifulSoup) -> int:
    return len([tag for tag in soup.findAll() if len(tag.attrs) != 0])


if __name__ == '__main__':
    link = 'https://greenatom.ru/'
    session = create_session_header()
    soup = parse_page(session, link)
    print(f'Всего тегов на странице {link}: {count_all_tags_on_page(soup)}')
    print(
        f'Тегов с атрибутами на странице {link}: {count_tags_with_attributes(soup)}')