from selenium import webdriver


class Firefox(object):
    """
    Ready Chrome driver 
    """
    def __init__(self):
        self.options = webdriver.FirefoxOptions()
        self.driver = self._setup_driver()
    
    def _setup_driver(self):
        self.options.add_argument('--headless')
        return webdriver.Firefox(options=self.options)

    @property
    def page(self):
        return self.driver.page_source

    def get(self, url: str):
        self.driver.get(url)

    def close(self):
        self.driver.quit()
