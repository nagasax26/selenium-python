from lxml import etree

from base_page import BasePage


class Listing(object):
    def __init__(self, listing_div):
        self.name = listing_div.find('./span/b').text
        self.wealth = int(listing_div.find('./p').text)


class PageWithListings:
    def __init__(self, source_page):
        self.tree = etree.HTML(source_page)

    def get_listings(self):
        locator = './/div/span/..'
        divs = self.tree.findall(locator)
        return [Listing(div) for div in divs]

    def get_listings_high_to_low(self):
        return sorted(self.get_listings(), key=lambda x: x.wealth, reverse=True)

    @property
    def highest_price(self):
        return self.get_listings_high_to_low()[0]


class TechStepAcademy(BasePage):
    url = 'https://techstepacademy.com/trial-of-the-stones/'


def run_page():
    browser = TechStepAcademy()
    browser.go()

    merchants = PageWithListings(browser.page_source)

    wealth = merchants.highest_price.wealth
    name = merchants.highest_price.name
    assert wealth == 3000, print(f"Assert Failed: wealth={wealth}")
    assert name == 'Jessica', print(f"Assert Failed: name={name}")
    print('Test Passed')
    browser.close()