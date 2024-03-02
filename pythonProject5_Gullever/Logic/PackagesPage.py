from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class PackagesGulliver(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def click_on_first_package(self):
        # cuntinue_buttons = self.driver.find_elements(By.XPATH, "//a[text()='המשך']")
        # print(cuntinue_buttons)
        first_result_link = WebDriverWait(self. _driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[@id='packages-results']/div[2]/div[2]/div[2]/div/generic-deals-group[1]"
                           "/div[2]/generic-deal[1]/div/div[1]/div[2]/div[3]/div[6]/a"))
        )
        # cuntinue_buttons[1].click()
        first_result_link.click()

    def package_meaorgan_isDisplayed(self):
        package_meaorgan = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='interactiveMenu']/li[5]/a/span[2]"))
        )
        return package_meaorgan.is_displayed()

    def click_search_withoutdate(self):
        try:
            hotelWorld_button = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div[1]/search-box/div/div/div[6]/input"))
            )
            hotelWorld_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def package_withoyt_dates_isDisplayed(self):
        package_n_date = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div"))
        )
        return package_n_date.is_displayed()

    def click_hotel_sale(self):
        try:
            hotelWorld_button = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "/html/body/div[2]/div/div/div/div/div/sale-page-deals/div/div/div[2]/a[1]/div/div[3]"))
            )
            hotelWorld_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def check_sale_page_isdisplayed(self):
        package_n_sale = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'מחיר')]"))
        )
        return package_n_sale.is_displayed()

    def package_meaorgen_table_is_displayed(self):
        package_n_sale = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'חיפוש טיול מאורגן')]"))
        )
        return package_n_sale.is_displayed()
