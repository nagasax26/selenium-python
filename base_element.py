from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        web_element = WebDriverWait(self.driver, 10)\
            .until(EC.presence_of_element_located(locator=self.locator))
        self.web_element = web_element

    def click(self):
        web_element = WebDriverWait(self.driver, 10) \
            .until(EC.element_to_be_clickable(locator=self.locator))
        action = ActionChains(self.driver)
        action.move_to_element(web_element)
        action.click()
        action.perform()

    def attribute(self, attribute):
        attribute = self.web_element.get_attribute(attribute)
        return attribute

    @property
    def text(self):
        inner_html = self.web_element.get_attribute('innerHTML')
        inner_text = self.web_element.get_attribute('innerText')
        text = self.web_element.text or inner_html or inner_text
        return text
