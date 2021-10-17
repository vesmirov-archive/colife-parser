import os
import time

from dotenv import load_dotenv
from drivers import Firefox
import telebot
from parser.objects import get_colife_objects

# Colife
OBJECTS_READY_URL = 'https://colife.ru/catalog'
OBJECTS_IN_RENOVATION_URL = 'https://colife.ru/remont'
UNIQUE_HTML_ELEMENT = {'element': 'div', 'attribute': 'data-product-pack-label', 'value': 'lwh'}

# Telegram
load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


def main():
    bot = telebot.TeleBot(TOKEN)
    browser = Firefox()
    cache = []

    while True:
        try:
            browser.get(OBJECTS_READY_URL)
            objects = get_colife_objects(browser.page, UNIQUE_HTML_ELEMENT)

            cache = list(filter(lambda el: el in objects, cache))
            filtered_objects = list(filter(lambda obj: obj not in cache, objects))
            cache.extend(filtered_objects)

            if filtered_objects:
                message = '\n'.join(filtered_objects)
                bot.send_message(CHAT_ID, f'Новые поступления:\n{message}')
        except Exception as e:
            bot.send_message(CHAT_ID, str(e))
            break

    browser.close()


if __name__ == '__main__':
    main()
