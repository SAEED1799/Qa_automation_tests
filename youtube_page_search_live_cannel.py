from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from infra.base_page import BasePage


class Youtube_Page_Search_live_Channel(BasePage):
    SEARCH_INPUT_LIVE_CHANNEL = "//*[@id='chips']/yt-chip-cloud-chip-renderer[4]"

    def __int__(self, driver):
        super().__init__(driver)
        #self.search_input = self.driver.find_element(By.XPATH, self.SEARCH_INPUT_CHANNEL)  # logic

    def click_channel(self):
        try:
            self.search_input_live_channel = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.SEARCH_INPUT_LIVE_CHANNEL)))  # logic
            self.search_input_live_channel.click()
            WebDriverWait(self._driver, 5).until(EC.alert_is_present())

        except Exception as e:
            print("ok")
