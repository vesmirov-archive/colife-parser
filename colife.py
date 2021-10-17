import requests
from bs4 import BeautifulSoup

from drivers import Firefox

OBJECTS_READY_URL = 'https://colife.ru/catalog'
OBJECTS_IN_RENOVATION_URL = 'https://colife.ru/remont'

READY_HTML_PATH = {
    'div': {'id': 'rec118977214', 'order': None},
    'div': {'class': 't776', 'order': 0},
    'div': {'class': 't-store js-store', 'order': 0},
    'div': {'class': 'js-store-grid-cont t-store__grid-cont t-container t-store__grid-cont_mobile-grid t-store__valign-buttons', 'order': 2},
}

RENOVATION_HTML_PATH = {}


def get_colife_objects(html, path, parser='lxml'):
    warnings = []
    soup = BeautifulSoup(html, parser)

    # TODO add scrapping options    


def main():
    browser = Firefox()
    
    page_html = browser.get(OBJECTS_READY_URL)
    objets = get_colife_objects(page_html, READY_HTML_PATH)

    browser.close()


if __name__ == '__main__':
    main()
    