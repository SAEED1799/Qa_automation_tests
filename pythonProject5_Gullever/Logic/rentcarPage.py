from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class rentalCarGulliver:

    # AGE_DRIVER_LABEL = "//div[contains(text(),'גיל הנהג')]"

    def __init__(self, driver):
        self.driver = driver
        # self.age_driver_label = self.driver.find_element(By.XPATH, self.AGE_DRIVER_LABEL)

    def agebear(self):
        return True

    def age_driver_label_is_displayed(self):
            try:
                package_title = WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'גיל הנהג')]"))
                )
                return package_title.is_displayed()
            except TimeoutException:
                print("Timed out waiting for package title element to be visible")
                return False

        # package_title = WebDriverWait(self.driver, 20).until(
        #     EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'גיל הנהג')]"))
        # )
        # return package_title.is_displayed()
