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


class RentalCarTest(unittest.TestCase):

    def setUp(self):
        self.browser = None
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.get_driver(
            self.browser)  # You can replace 'Chrome' with the browser of your choice  # Navigate to Gulliver website
        # self.driver.get("https://www.gulliver.co.il/")
        self.home_page = HOMEGulliver(self.driver)
        self.list = ["chrome", "fireFox", "edge"]

    def test_check_rentCar(self):
        self.home_page.click_button_rentcar()

        self.rentCar_page = rentalCarGulliver(self.driver)

        # result = self.rentCar_page.age_driver_label_is_displayed()
        self.assertTrue(self.rentCar_page.age_driver_label_is_displayed(), "flow to rental car page is ok")

    def tearDown(self):
        self.driver.quit()
