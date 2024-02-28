import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Logic.HomePage import HOMEGulliver
from Logic.OrderPage import OrderGulliver
from Logic.PackagesPage import PackagesGulliver
from Logic.CretePagePackeges import CreteGulliver
from Logic.PrivatAreaPage import areaGulliver
from Logic.rentcarPage import rentalCarGulliver
from infra.browser_wrapper import GulliverBrowserWrapper


class TestGulliver(unittest.TestCase):
    def setUp(self):
        self.browser = GulliverBrowserWrapper()
        self.driver = self.browser.get_driver()  # You can replace 'Chrome' with the browser of your choice  # Navigate to Gulliver website
        self.home_page = HOMEGulliver(self.driver)

    # test home title page
    def test_home_page_title(self):
        # this ok
        actual_title = self.home_page.get_title()
        expected_title = "טיסות, חבילות נופש ומלונות בארץ ובחו״ל – גוליבר"
        self.assertEqual(expected_title, actual_title, "Homepage title doesn't match expected")

    # test see if can go to package from the home page to package of crete
    def test_logic_pages_krete_package(self):
        # this ok
        self.home_page.click_on_packages()
        self.cretepackege_page = CreteGulliver(self.driver)
        self.cretepackege_page.click_on_kritim()
        self.package_page = PackagesGulliver(self.driver)
        self.package_page.click_on_first_package()
        self.order_page = OrderGulliver(self.driver)
        self.assertTrue(self.order_page.title_on_packages().is_displayed(), "Package tour title is not displayed")

        # test check if they okay without id to private area

    def test_check_idOk(self):
        # this ok
        # Navigate to the Gulliver website
        self.home_page.click_on_private_area()
        self.area_page = areaGulliver(self.driver)
        self.area_page.click_ok_button_id()
        time.sleep(3)
        self.assertTrue(self.area_page.title_on_area().is_displayed(),
                        "Package tour title is not displayed")

        # test check if they go to rent car page

    def test_check_rentCar(self):
        self.home_page.click_button_rentcar()

        self.rentCar_page = rentalCarGulliver(self.driver)

    # result = self.rentCar_page.age_driver_label_is_displayed()
    # self.assertTrue(self.rentCar_page.age_driver_label_is_displayed(), "Package tour title is not displayed")
    # self.assertTrue(self.rentCar_page.agebear(), "Package tour title is not displayed")

    # test check if i choose hotel in the world i go to this page
    def test_check_hotelWorld(self):
        # this ok
        self.home_page.click_hotel_world()
        self.package_hotel_world = PackagesGulliver(self.driver)
        self.package_hotel_world.package_meaorgan_isDisplayed()
        self.assertTrue(self.package_hotel_world.package_meaorgan_isDisplayed(), "hotel world is not displayed")

    # test check if can do searck without dates
    def test_check_no_date_eilat(self):
        # this ok just i want to button ok to the driver
        self.home_page.click_hotels_inEilat()
        self.package_page = PackagesGulliver(self.driver)
        self.package_page.click_search_withoutdate()
        time.sleep(5)
        self.assertTrue(self.package_page.package_withoyt_dates_isDisplayed(), "without dates its not displayed")

    # this test see if i flow from home page to sales page i well come
    def test_check_hotel_sale(self):
        self.home_page.click_sale_hotel()
        time.sleep(3)
        self.package_sale_page = PackagesGulliver(self.driver)
        self.package_sale_page.click_hotel_sale()
        time.sleep(3)
        # self.assertFalse(self.package_sale_page.check_sale_page_isdisplayed(), "sales its not displayed")

        # test for testing טיולים מאורגנים אם הוא כן מצליח ללחוץ ולעבור
#return to this test out at 18:00
    def test_organized_tours(self):
        # Open the Gulliver website
        #click on teolem maorganeem
        self.home_page.click_contact_us_link_organized()
        self.package_page = PackagesGulliver(self.driver)
        self.assertTrue(self.package_page.package_meaorgen_table_is_displayed(), "without dates its not displayed")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
