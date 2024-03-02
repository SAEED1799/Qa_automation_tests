from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class CreteGulliver(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_kritim(self):
        kritim_package_link = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'כרתים')]"))
        )
        kritim_package_link.click()
