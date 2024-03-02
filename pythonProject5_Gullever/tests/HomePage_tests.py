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


class HomePageTests(unittest.TestCase):

    def setUp(self):
        self.browser = None
        self.browser_in = BrowserWrapper()
        self.driver = self.browser_in.get_driver(self.browser)  # You can replace 'Chrome' with the browser of your choice  # Navigate to Gulliver website
        # self.driver.get("https://www.gulliver.co.il/")
        self.home_page = HOMEGulliver(self.driver)
        self.list = ["chrome", "fireFox", "edge"]

    # test home title page

    def test_home_page_title(self):
        # this ok
        actual_title = self.home_page.get_title()
        expected_title = "טיסות, חבילות נופש ומלונות בארץ ובחו״ל – גוליבר"
        self.assertEqual(expected_title, actual_title, "Homepage title doesn't match expected")

    # test check if i choose hotel in the world i go to this page
    def test_check_hotelWorld(self):
        # this ok
        self.home_page.click_hotel_world()
        self.package_hotel_world = PackagesGulliver(self.driver)
        self.package_hotel_world.package_meaorgan_isDisplayed()
        self.assertTrue(self.package_hotel_world.package_meaorgan_isDisplayed(), "hotel world is not displayed")

        # test for testing טיולים מאורגנים אם הוא כן מצליח ללחוץ ולעבור

    def test_organized_tours(self):
        # Open the Gulliver website
        # click on teolem maorganeem
        self.home_page.click_contact_us_link_organized()
        self.package_page = PackagesGulliver(self.driver)
        self.assertTrue(self.package_page.package_meaorgen_table_is_displayed(), "without dates its not displayed")

    def tearDown(self):
        self.driver.quit()

