from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class Youtube_Page_Search_Subscription(BasePage):
    SEARCH_INPUT_SUBSCRIPTION = "//tp-yt-paper-item//yt-formatted-string[text()='מינויים']"

    def __int__(self, driver):
        super().__init__(driver)
        # self.search_input_subscription = self.driver.find_element(By.XPATH, self.SEARCH_INPUT_SUBSCRIPTION)  # logic

    def click_subscription(self):
        try:
            self.search_input_subscription = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.SEARCH_INPUT_SUBSCRIPTION)))  # logic
            self.search_input_subscription.click()
            WebDriverWait(self._driver, 5).until(EC.alert_is_present())

        except Exception as e:
            print("ok")
