import concurrent.futures
import time
import unittest
from Logic.HomePage import HOMEGulliver
from Logic.OrderPage import OrderGulliver
from Logic.PackagesPage import PackagesGulliver
from Logic.CretePagePackeges import CreteGulliver
from Logic.PrivatAreaPage import areaGulliver
from Logic.rentcarPage import rentalCarGulliver
from infra.browser_wrapper import BrowserWrapper


class TestGulliver(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()  # You can replace 'Chrome' with the browser of your choice  # Navigate to Gulliver website
        # self.driver.get("https://www.gulliver.co.il/")
        self.home_page = HOMEGulliver(self.driver)
        self.list = ["chrome", "fireFox", "edge"]

    ##this test ok well go
    # test home title page
    def test_home_page_title(self):
        # this ok
        actual_title = self.home_page.get_title()
        expected_title = "טיסות, חבילות נופש ומלונות בארץ ובחו״ל – גוליבר"
        self.assertEqual(expected_title, actual_title, "Homepage title doesn't match expected")
##this test ok well go
    # test see if can go to package from the home page to package of crete
    def test_logic_pages_crete_package(self):
        # this ok
        # this method is to click on package
        self.home_page.click_on_packages()
        # this is constructor og logic crete page
        self.crete_package_page = CreteGulliver(self.driver)
        # this is click of the packages just for crete
        self.crete_package_page.click_on_kritim()
        # this is constructor og logic packages page
        self.package_page = PackagesGulliver(self.driver)
        # this method is to click in the first package in the page
        self.package_page.click_on_first_package()
        # her is constructor of logic order page
        self.order_page = OrderGulliver(self.driver)
        # this asserts do direct from home page to page of order
        self.assertTrue(self.order_page.title_on_packages_is_displayed(),
                        "Package tour is not displayed")

        ##this test ok well go
        # test check if they okay without id to private area
    def test_check_idOk(self):
        # this ok
        # Navigate to the Gulliver website
        self.home_page.click_on_private_area()
        self.area_page = areaGulliver(self.driver)
        self.area_page.click_ok_button_id()
        self.assertTrue(self.area_page.title_on_area_is_displayed(),
                        "Package tour title is not displayed")

        # test check if they go to rent car page

    ##this test ok well go
    def test_check_rentCar(self):
        self.home_page.click_button_rentcar()

        self.rentCar_page = rentalCarGulliver(self.driver)

    # result = self.rentCar_page.age_driver_label_is_displayed()
    # self.assertTrue(self.rentCar_page.age_driver_label_is_displayed(), "Package tour title is not displayed")
    # self.assertTrue(self.rentCar_page.agebear(), "Package tour title is not displayed")

    ##this test ok well go
    # test check if i choose hotel in the world i go to this page
    def test_check_hotelWorld(self):
        # this ok
        self.home_page.click_hotel_world()
        self.package_hotel_world = PackagesGulliver(self.driver)
        self.package_hotel_world.package_meaorgan_isDisplayed()
        self.assertTrue(self.package_hotel_world.package_meaorgan_isDisplayed(), "hotel world is not displayed")

    ##this test ok well go
    # test check if can do search without dates
    def test_check_no_date_eilat(self):
        # this ok just i want to button ok to the driver
        self.home_page.click_hotels_inEilat()
        self.package_page = PackagesGulliver(self.driver)
        self.package_page.click_search_withoutdate()
        time.sleep(5)
        self.assertTrue(self.package_page.package_withoyt_dates_isDisplayed(), "without dates its not displayed")

    ##this test ok well go
    # this test see if i flow from home page to sales page i well come
    def test_check_hotel_sale(self):
        self.home_page.click_sale_hotel()
        time.sleep(3)
        self.package_sale_page = PackagesGulliver(self.driver)
        self.package_sale_page.click_hotel_sale()
        time.sleep(3)
        # self.assertFalse(self.package_sale_page.check_sale_page_isdisplayed(), "sales its not displayed")

    ##this test ok well go
    # test for testing טיולים מאורגנים אם הוא כן מצליח ללחוץ ולעבור

    def test_organized_tours(self):
        # Open the Gulliver website
        # click on teolem maorganeem
        self.home_page.click_contact_us_link_organized()
        self.package_page = PackagesGulliver(self.driver)
        self.assertTrue(self.package_page.package_meaorgen_table_is_displayed(), "without dates its not displayed")

    ##this test ok well go
    # this is bug for insert mail amd the sighn up ok with not good mail
    def test_check_mail_firstPage(self):
        self.home_page.click_insert_mail_keys()
        time.sleep(1)
        self.home_page.insert_mail_keys()
        self.home_page.click_register_mail_keys()
        time.sleep(10)
        self.assertTrue(self.home_page.mail_is_ok_is_displayed(), "without mail its displayed")

    def get_all_tests(self):
        self.all_tests = [self.test_check_hotel_sale(),self.test_check_hotelWorld(),self.test_check_idOk(),
                          self.test_check_mail_firstPage(),self.test_check_no_date_eilat(),self.test_check_rentCar()
                          ,self.test_home_page_title(),self.test_logic_pages_crete_package(),self.test_organized_tours() ]

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
