from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from infra.base_page import BasePage


class YouTubePage(BasePage):

    SEARCH_INPUT = "//input[@id='search']"

    def __init__(self,driver):
        super().__init__(driver)
        self.search_input = self._driver.find_element(By.XPATH,self.SEARCH_INPUT)

    def fill_search_input(self,text):
        self.search_input.send_keys(text)#logic

    def press_enter_on_search_input(self):
        self.search_input.send_keys(Keys.RETURN)

    def search_flow(self,text):
        self.fill_search_input(text)
        self.press_enter_on_search_input()