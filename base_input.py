from selenium.webdriver import ActionChains

from base_element import BaseElement


class BaseInput(BaseElement):
    def __init__(self, driver, locator):
        super().__init__(driver, locator)

    def set_input_text(self, value):
        action = ActionChains(self.driver)
        action.move_to_element(self.web_element)
        action.click()
        action.send_keys(value)
        action.perform()

    def get_input_text(self):
        return self.attribute('value')

    def clear(self):
        return self.web_element.clear()

    input_text = property(get_input_text, set_input_text)