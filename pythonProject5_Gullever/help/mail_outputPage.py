from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from help.homepage_gulliver import HOMEPAGE_GULLIVER


class Page_mail:
    SEARCH_INPUT = "//*[@id='ZA_CAMP_IN_PAGE_INPUT_1_CID_76461']"

    def __init__(self, driver):
        self.gulliver_page = HOMEPAGE_GULLIVER().navigate_to_homepage()

        self.search_input = self.gulliver_page.driver.find_element(By.XPATH, self.SEARCH_INPUT)

    def fill_search_input(self, text):
        self.search_input.send_keys(text)  # logic

    def press_enter_on_search_input(self):
        self.search_input.send_keys(Keys.RETURN)

    def search_flow(self, text):
        self.fill_search_input(text)
        self.press_enter_on_search_input()
