from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Elements(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_elements = None
        self.find()

    def find(self):
        web_elements = WebDriverWait(self.driver, 10)\
            .until(EC.presence_of_all_elements_located(locator=self.locator))
        self.web_elements = web_elements

    def attribute(self, attribute):
        elements = [tag.get_attribute(attribute) for tag in self.web_elements]
        return elements
