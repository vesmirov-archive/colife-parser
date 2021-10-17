from bs4 import BeautifulSoup


def _get_urls(objects):
    urls = []

    for obj in objects:
        url = obj.find('a')['href']
        urls.append(url)
    
    return urls


def _find_by_unique_attribute(soup, unique):
    pattern = f"{unique['element']}[{unique['attribute']}=\"{unique['value']}\"]"
    objects = soup.select(pattern)

    if objects:
        return objects
    
    raise ValueError(f'No unique attribute: {pattern}')


def get_colife_objects(html, unique_attribute, parser='lxml'):
    warnings = []

    soup = BeautifulSoup(html, parser)

    try:
        objects = _find_by_unique_attribute(soup, unique_attribute)
        return _get_urls(objects)
    except ValueError:
        pass
        # TODO logging

    return
