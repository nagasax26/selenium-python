# selenium-python

### usage demo

```python
from base_page import BasePage
from base_element import BaseElement
from base_input import BaseInput
from elements import Elements
from selenium.webdriver.common.by import By

class SomePage(BasePage):
    url = 'your_url_to_test'
    
    @property
    def my_input(self):
        locator = (By.XPATH, '//input')
        return BaseInput(driver=self.driver, locator=locator)
    
    @property
    def my_button(self):
        locator = (By.CSS_SELECTOR, 'button[type="submit"]')
        return BaseElement(driver=self.driver, locator=locator)
    
    def my_list_of_elements(self):
        locator = (By.CSS_SELECTOR, 'div.title')
        return Elements(driver=self.driver, locator=locator)

my_page = SomePage()
my_page.go()
my_page.my_input.input_text = 'my cool input'
my_page.my_button.click()
my_page.close()
```