from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class OrderGulliver(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def title_on_packages_is_displayed(self):
        package_title = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[text() = 'מחיר החופשה (טיסה + מלון)']"))
        )
        return package_title.is_displayed()

    def click_on_package(self):
        try:
            hotelWorld_button = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/glv-hot-"
                                                            "deals/div/div/div[4]/a[5]/div/div[3]"))
            )
            hotelWorld_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def click_continue_order(self):
        try:
            hotelWorld_button = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[10]/div[2]"
                                                            "/div/div[3]/div[3]/a"))
            )
            hotelWorld_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def insert_keys_name(self):
        try:
            hotelWorld_button = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='firstName-input']"))
            )
            hotelWorld_button.send_keys("skdjflsd5645")
        except Exception as e:
            print(f"An error occurred: {e}")

    def click_last_conform_name(self):
        try:
            hotelWorld_button = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='payerForm']/div[3]/button"))
            )
            hotelWorld_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def filed_input_name(self):
        package_title = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='payerForm']/div[1]/glv-form-input[1]/div"))
        )
        return package_title.is_displayed()
