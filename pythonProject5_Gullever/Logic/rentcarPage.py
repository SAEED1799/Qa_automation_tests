import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class rentalCarGulliver(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # AGE_DRIVER_LABEL = "//div[contains(text(),'גיל הנהג')]"
    def agebear(self):
        return True

    def age_driver_label_is_displayed(self):
        time.sleep(5)
        try:
            package_title = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='form1']/div[7]/div[3]/div/div/h2/img"))
            )
            return package_title.is_displayed()
        except TimeoutException:
            print("Timed out waiting for package title element to be visible")
            return False

    # package_title = WebDriverWait(self.driver, 20).until(
    #     EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'גיל הנהג')]"))
    # )
    # return package_title.is_displayed()
