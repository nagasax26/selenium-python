import time
from selenium import webdriver
from decouple import config
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
executable_path = config('EXECUTABLE_PATH')


class BasePage:
    url = None

    def __init__(self, driver=None, no_gui=False):
        if driver:
            self.driver = driver
        else:
            if no_gui:
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--disable-gpu')
            self.driver = webdriver.Chrome(executable_path=executable_path, options=chrome_options)

    def go(self):
        self.driver.get(self.url)

    @property
    def base_url(self):
        url_list = self.url.split('/')
        protocol = url_list[0]
        host = url_list[2]
        base_url = protocol + '//' + host
        return base_url

    def go_to(self, link):
        if self.base_url in link:
            self.url = link
        else:
            self.url = self.base_url + link
        self.go()

    def scroll(self, *args, scroll_by=None, timeout=3, stop_time=None):
        page_load_time = timeout
        if args:
            args[0](self.driver)

        last_height = self.driver.execute_script("return document.body.scrollHeight;")
        if stop_time:
            stop_loop_time = time.time() + (60 * stop_time)
        while True:
            # Scroll down to bottom
            if scroll_by:
                self.driver.execute_script(f"window.scrollTo(0, {scroll_by});")
            else:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(page_load_time)
            if args:
                args[0](self.driver)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight;")
            if new_height == last_height:
                break
            if stop_time is not None and time.time() > stop_loop_time:
                break
            last_height = new_height

    def refresh(self):
        self.driver.refresh()

    @property
    def page_source(self):
        return self.driver.page_source

    def close(self):
        self.driver.close()


