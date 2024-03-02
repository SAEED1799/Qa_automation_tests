
import time
import unittest
from Logic.HomePage import HOMEGulliver
from Logic.OrderPage import OrderGulliver
from Logic.PackagesPage import PackagesGulliver
from Logic.CretePagePackeges import CreteGulliver
from infra.browser_wrapper import BrowserWrapper


class packageTests(unittest.TestCase):

    def setUp(self):
        self.browser = None
        self.browser_in = BrowserWrapper()
        self.driver = self.browser_in.get_driver(self.browser)  # You can replace 'Chrome' with the browser of your choice  # Navigate to Gulliver website
        self.home_page = HOMEGulliver(self.driver)

    # test see if can go to package from the home page to package of crete
    def test_show_packages_chose_trip(self):
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

   # test check if can do search without dates
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

    def tearDown(self):
        self.driver.quit()
