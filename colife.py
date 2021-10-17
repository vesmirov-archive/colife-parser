from drivers import Firefox
from parser.objects import get_colife_objects

OBJECTS_READY_URL = 'https://colife.ru/catalog'
OBJECTS_IN_RENOVATION_URL = 'https://colife.ru/remont'

UNIQUE_HTML_ELEMENT = {'element': 'div', 'attribute': 'data-product-pack-label', 'value': 'lwh'}


def main():
    browser = Firefox()    
    browser.get(OBJECTS_READY_URL)
    page_html = browser.page
    browser.close()

    objects = get_colife_objects(page_html, UNIQUE_HTML_ELEMENT)

    for obj in objects:
        print(obj)


if __name__ == '__main__':
    main()
    