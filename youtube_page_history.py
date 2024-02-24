import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from infra.base_page import BasePage


class Youtube_Page_History(BasePage):
    SEARCH_INPUT = "//*[@title='היסטוריה']"

    def __int__(self, driver):
        super().__init__(driver)
        # self.search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)  # logic

    def click_btn(self):
        try:
            self.search_input = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.SEARCH_INPUT)))  # logic
            self.search_input.click()
            WebDriverWait(self._driver, 5).until(EC.alert_is_present())

        except Exception as e:
            print("ok")
