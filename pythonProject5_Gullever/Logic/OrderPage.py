from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderGulliver():
    def __init__(self, driver):
        self.driver = driver

    def title_on_packages(self):
        package_title = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[text() = 'מחיר החופשה (טיסה + מלון)']"))
        )
        return package_title
