from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PackagesGulliver():
    def __init__(self, driver):
        self.driver = driver

    def click_on_first_package(self):
        # cuntinue_buttons = self.driver.find_elements(By.XPATH, "//a[text()='המשך']")
        # print(cuntinue_buttons)
        first_result_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//a[@class='order-btn' and @data-gamitee-link='https://www.gulliver.co.il/"
                           "packages/details?PackageKey=alp_100502266368_16625678721"
                           "_XDQAFY_2024-04-11_2024-04-14_HER_57120037_57119995_1_21640_2_0_0"
                           "_TLV&NumOfAdults=2&NumOfChilds=0&NumOfInfants=0&Affiliate=gamitee']"))
        )
        # cuntinue_buttons[1].click()
        first_result_link.click()

    def package_meaorgan_isDisplayed(self):
        package_meaorgan = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='interactiveMenu']/li[5]/a/span[2]"))
        )
        return package_meaorgan.is_displayed()

    def click_search_withoutdate(self):
        try:
            hotelWorld_button = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div[1]/search-box/div/div/div[6]/input"))
            )
            hotelWorld_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def package_withoyt_dates_isDisplayed(self):
        package_n_date = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div"))
        )
        return package_n_date.is_displayed()

    def click_hotel_sale(self):
        try:
            hotelWorld_button = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "/html/body/div[2]/div/div/div/div/div/sale-page-deals/div/div/div[2]/a[1]/div/div[3]"))
            )
            hotelWorld_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def check_sale_page_isdisplayed(self):
        package_n_sale = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'מחיר')]"))
        )
        return package_n_sale.is_displayed()

    def package_meaorgen_table_is_displayed(self):
        package_n_sale = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'חיפוש טיול מאורגן')]"))
        )
        return package_n_sale.is_displayed()