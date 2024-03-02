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


class AreaTests(unittest.TestCase):

    def setUp(self):
        self.browser = None
        self.browser_in = BrowserWrapper()
        self.driver = self.browser_in.get_driver(self.browser)# You can replace 'Chrome' with the browser of your choice  # Navigate to Gulliver website
        # self.driver.get("https://www.gulliver.co.il/")
        self.home_page = HOMEGulliver(self.driver)

    def test_check_idOk(self):
        # this ok
        # Navigate to the Gulliver website
        self.home_page.click_on_private_area()
        self.area_page = areaGulliver(self.driver)
        self.area_page.click_ok_button_id()
        self.assertTrue(self.area_page.title_on_area_is_displayed(),
                        "Package tour title is not displayed")

    # this is bug for insert mail amd the sighn up ok with not good mail
    def test_check_mail_firstPage(self):
        self.home_page.click_insert_mail_keys()
        time.sleep(1)
        self.home_page.insert_mail_keys()
        self.home_page.click_register_mail_keys()
        time.sleep(10)
        self.assertTrue(self.home_page.mail_is_ok_is_displayed(), "without mail its displayed")

    def tearDown(self):
        self.driver.quit()

