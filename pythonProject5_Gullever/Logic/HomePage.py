from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class HOMEGulliver(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_packages(self):
        tour_package_link = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'חבילות נופש')]"))
        )
        tour_package_link.click()

    def get_title(self):
        return self._driver.title

    def click_on_private_area(self):
        order_link = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/glv-footer-v3/div/div[3]/div[1]/div/span[5]/a"))
        )
        order_link.click()

    def click_button_rentcar(self):
        try:
            rentCar_button = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/glv-header-v3/div/div[3]/div[1]/a[5]"))
            )
            rentCar_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def click_hotel_world(self):
        try:
            hotelWorld_button = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/glv-header-v3/div/div[3]/div[1]/a[4]"))
            )
            hotelWorld_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def click_hotels_inEilat(self):
        try:
            hotelWorld_button = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/glv-header-v3/div/div[3]/div[2]/a[2]"))
            )
            hotelWorld_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def click_sale_hotel(self):
        try:
            hotelWorld_button = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  "/html/body/div[2]/div/div/div/div/div/div[1]/main-carousel-directive/div/div/div[1]/div[1]/a/div"))
            )
            hotelWorld_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")


    def click_contact_us_link_organized(self):
        # Wait for an element that indicates the page is fully loaded
        try:
            hotelWorld_button = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH,
                                                "/html/body/glv-header-v3/div/div[3]/div[1]/a[3]"))
            )
            hotelWorld_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def click_insert_mail_keys(self):
        try:
            hotelWorld_button = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "// *[ @ id = 'ZA_CAMP_IN_PAGE_INPUT_1_CID_76461']"))
            )
            hotelWorld_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def insert_mail_keys(self):
        try:
            hotelWorld_button = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "// *[ @ id = 'ZA_CAMP_IN_PAGE_INPUT_1_CID_76461']"))
            )
            hotelWorld_button.send_keys("skdjflsd")
        except Exception as e:
            print(f"An error occurred: {e}")

    def click_register_mail_keys(self):
        try:
            hotelWorld_button = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='ZA_CAMP_IN_PAGE_SUBMIT_CID_76461']"))
            )
            hotelWorld_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def mail_is_ok_is_displayed(self):
        package_title = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='ZA_CAMP_IN_PAGE_DIV_1_CID_76461']/div[2]/div[2]/img"))
        )
        return package_title.is_displayed()

