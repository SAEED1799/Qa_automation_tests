from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class areaGulliver(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def click_ok_button_id(self):
        order_ok_button = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "/html/body/div[2]/div/div/div/div/div[3]/div[1]/div[1]"
                                              "/div/div/form/div/div[3]/button/span"))
        )
        order_ok_button.click()

    def title_on_area_is_displayed(self):
        package_title = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/p"))
        )
        return package_title.is_displayed()
