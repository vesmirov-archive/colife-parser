import os

from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class Firefox(object):
    """
    Ready Chrome driver 
    """
    def __init__(self, timeout=10, options=None):
        self.timeout = timeout
        self.options = webdriver.FirefoxOptions()
        self.driver = self._setup_driver(options)
    
    def _setup_driver(self, options):
        binary = FirefoxBinary(os.getenv('FIREFOX_BINARY_PATH', '/usr/bin/firefox'))

        if options:
            map(self.options.add_argument, options)

        self.options.add_argument('--headless')

        driver = webdriver.Firefox(firefox_binary=binary, options=self.options)
        driver.set_page_load_timeout(self.timeout)

        return driver

    @property
    def page(self):
        return self.driver.page_source

    @property
    def url(self):
        return self.driver.current_url

    def get(self, url: str):
        try:
            self.driver.get(url)
        except (WebDriverException) as e:
            # TODO add logging
            print(e)

    def close(self):
        self.driver.quit()
