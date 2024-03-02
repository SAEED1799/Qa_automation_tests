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


class OrderCompleteTests(unittest.TestCase):

    def setUp(self):
        self.browser = None
        self.browser_in = BrowserWrapper()
        self.driver = self.browser_in.get_driver(
            self.browser)  # You can replace 'Chrome' with the browser of your choice  # Navigate to Gulliver website
        # self.driver.get("https://www.gulliver.co.il/")
        self.home_page = HOMEGulliver(self.driver)

    # negative test
    def test_orderPage_not_good_details(self):
        self.home_page.click_on_packages()
        self.order_page = OrderGulliver(self.driver)
        self.order_page.click_on_package()
        time.sleep(2)
        self.order_page.click_continue_order()
        time.sleep(3)
        self.order_page.insert_keys_name()
        time.sleep(3)
        self.order_page.click_last_conform_name()
        time.sleep(3)
        self.assertTrue(self.order_page.filed_input_name(),
                        "filed input name_name just of english")

    def tearDown(self):
        self.driver.quit()
