from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CreteGulliver():
    def __init__(self, driver):
        self.driver = driver

    def click_on_kritim(self):
        kritim_package_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'כרתים')]"))
        )
        kritim_package_link.click()
