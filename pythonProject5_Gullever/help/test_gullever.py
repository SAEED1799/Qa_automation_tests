import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from help.homepage_gulliver import HOMEPAGE_GULLIVER


class TestGulliver(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        # self.wait = None

    def setUp(self):
        self.gulliver_page = HOMEPAGE_GULLIVER()

    # test for title bage

    def test_home_page_title(self):
        self.gulliver_page.navigate_to_homepage()
        actual_title = self.gulliver_page.get_title()
        expected_title = "טיסות, חבילות נופש ומלונות בארץ ובחו״ל – גוליבר"
        self.assertEqual(expected_title, actual_title, "Homepage title doesn't match expected")

    # test for testing טיולים מאורגנים אם הוא כן מצליח ללחוץ ולעבור
    def test_organized_tours(self):
        # Open the Gulliver website
        self.gulliver_page.navigate_to_homepage()
        self.gulliver_page.click_contact_us_link_organized()
        # Retrieve the title from the WebDriver object
        organized_tours_page_title = self.gulliver_page.driver.title
        # Add assertions to ensure that the page for organized tours is loaded
        self.assertIn("טיולים מאורגנים", organized_tours_page_title,
                      "Organized tours page is not loaded successfully")

    # טסט עבור בחירה מקום טיולים וכניסה ובחירה חבילה ומתקדמים לתשלום
    def test_book_flight_to_package(self):
        # Open the Gulliver website
        self.gulliver_page.navigate_to_homepage()
        self.gulliver_page.click_and_complete_package_tour()
        expected_xpath = "/html/body/div[2]/div/div/div/div/div/div[10]/div[1]"
                        # "//div[text() = 'מחיר החופשה (טיסה + מלון)']"
        actual_xpath = "/html/body/div[2]/div/div/div/div/div/div[10]/div[1]"
        self.assertEqual(actual_xpath, expected_xpath)

    # test check if they okay without id
    def test_check_idOk(self):
        # Navigate to the Gulliver website
        self.gulliver_page.navigate_to_homepage()
        order_link = WebDriverWait(self.gulliver_page.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/glv-footer-v3/div/div[3]/div[1]/div/span[5]/a"))
        )
        order_link.click()
        time.sleep(3)
        order_ok_button = WebDriverWait(self.gulliver_page.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "/html/body/div[2]/div/div/div/div/div[3]/div[1]/div[1]/div/div/form/div/div[3]/button/span"))
        )
        order_ok_button.click()
        time.sleep(2)
        expected_xpath = "/html/body/div[1]/div/div/div/div[2]/p"
        actual_xpath = "/html/body/div[1]/div/div/div/div[2]/p"
        self.assertEqual(actual_xpath, expected_xpath)

    # this test check have abug on disapility button
    def test_check_disapility(self):
        self.gulliver_page.navigate_to_homepage()
        try:
            disapility_button = WebDriverWait(self.gulliver_page.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='INDmenu-btn']"))
            )
            disapility_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(3)

    # test check if can invalidate order with not good email or any thin else
    def test_check_invalidate(self):
        self.gulliver_page.navigate_to_homepage()
        try:
            invalidate_button = WebDriverWait(self.gulliver_page.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/glv-footer-v3/div/div[3]/div[7]/div/span"))
            )
            invalidate_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(3)

    # test check if they go to rent car page
    def test_check_rentCar(self):
        self.gulliver_page.navigate_to_homepage()
        try:
            rentCar_button = WebDriverWait(self.gulliver_page.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/glv-header-v3/div/div[3]/div[1]/a[5]"))
            )
            rentCar_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(3)
        expected_xpath = "/html/body/div/div/div/div/div/div[3]/div[2]/div/div/div/div/label/span[3]/div/div"
        actual_xpath = "/html/body/div/div/div/div/div/div[3]/div[2]/div/div/div/div/label/span[3]/div/div"
        self.assertEqual(actual_xpath, expected_xpath)

    # test check if i choose hotel in the world i go to this page
    def test_check_hotelWorld(self):
        self.gulliver_page.navigate_to_homepage()
        try:
            hotelWorld_button = WebDriverWait(self.gulliver_page.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/glv-header-v3/div/div[3]/div[1]/a[4]"))
            )
            hotelWorld_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(3)
        expected_xpath = "//*[@id='interactiveMenu']/li[5]/a/span[2]"
        actual_xpath = "//*[@id='interactiveMenu']/li[5]/a/span[2]"
        self.assertEqual(actual_xpath, expected_xpath)

    # check if i do not good mail its okay or tell me that syntax mail not good
    def test_check_mail_firstPage(self):
        self.gulliver_page.navigate_to_homepage()
        try:
            hotelWorld_button = WebDriverWait(self.gulliver_page.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "// *[ @ id = 'ZA_CAMP_IN_PAGE_INPUT_1_CID_76461']"))
            )
            hotelWorld_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

        # element = self.gulliver_page.driver.find_element_by_xpath(
        #     "//*[@id='ZA_CAMP_IN_PAGE_INPUT_1_CID_76461']")
        # element.send_keys("5gftger")
        # time.sleep(5)

        # time.sleep(10)  # we need to use Explicit Wait insted
        # expected_xpath = "//*[@id='ZA_CAMP_IN_PAGE_DIV_1_CID_76461']/div[2]/div[2]/img"
        # actual_xpath = "//*[@id='ZA_CAMP_IN_PAGE_DIV_1_CID_76461']/div[2]/div[2]/img"
        # self.assertEqual(actual_xpath, expected_xpath)

    def test_check_modate_eilat(self):
        self.gulliver_page.navigate_to_homepage()
        try:
            hotelWorld_button = WebDriverWait(self.gulliver_page.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/glv-header-v3/div/div[3]/div[2]/a[2]"))
            )
            hotelWorld_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(3)
        try:
            hotelWorld_button = WebDriverWait(self.gulliver_page.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div[1]/search-box/div/div/div[6]/input"))
            )
            hotelWorld_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(3)

        expected_xpath = "/html/body/div[2]/div/div/div/div/div[2]/div[1]/search-box/div/div/div[6]/input"
        actual_xpath = "/html/body/div[2]/div/div/div/div/div[2]/div[1]/search-box/div/div/div[6]/input"
        self.assertEqual(actual_xpath, expected_xpath)

    # check if the hotel in jerusalem and have about the deal of the sale
    def test_check_hotel_sale(self):
        self.gulliver_page.navigate_to_homepage()
        try:
            hotelWorld_button = WebDriverWait(self.gulliver_page.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  "/html/body/div[2]/div/div/div/div/div/div[1]/main-carousel-directive/div/div/div[1]/div[1]/a/div"))
            )
            hotelWorld_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(3)
        try:
            hotelWorld_button = WebDriverWait(self.gulliver_page.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "/html/body/div[2]/div/div/div/div/div/sale-page-deals/div/div/div[2]/a[1]/div/div[3]"))
            )
            hotelWorld_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(3)

        expected_xpath = "/html/body/div[2]/div/div/div/div/div[2]/div[2]/div/span[2]"
        actual_xpath = "/html/body/div[2]/div/div/div/div/div[2]/div[2]/div/span[2]"
        self.assertEqual(actual_xpath, expected_xpath)

    def tearDown(self):
        self.gulliver_page.close()


if __name__ == "__main__":
    unittest.main()
