import requests
from bs4 import BeautifulSoup

from drivers import Firefox

COLIFE_ACTUAL_URL = 'https://colife.ru/catalog'
COLIFE_REMONT_URL = 'https://colife.ru/remont'


def main():
    browser = Firefox()
    # TODO
    browser.close()


if __name__ == '__main__':
    main()
    