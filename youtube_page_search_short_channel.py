from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from infra.base_page import BasePage


class Youtube_Page_Search_short_Channel(BasePage):
    SEARCH_INPUT_SHORT_CHANNEL = "//div[./ytd-mini-guide-entry-renderer[./*[@id='endpoint']]]"

    def __int__(self, driver):
        super().__init__(driver)
        #self.search_input = self.driver.find_element(By.XPATH, self.SEARCH_INPUT_CHANNEL)  # logic

    def click_short_channel(self):
        try:
            self.search_input_short_channel = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.SEARCH_INPUT_SHORT_CHANNEL)))  # logic
            self.search_input_short_channel.click()
            WebDriverWait(self._driver, 5).until(EC.alert_is_present())

        except Exception as e:
            print("ok")
