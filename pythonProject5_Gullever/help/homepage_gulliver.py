import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser_wrapper import GulliverBrowserWrapper


class HOMEPAGE_GULLIVER:
    def __init__(self):
        self.browser = GulliverBrowserWrapper()
        self.driver = self.browser.get_driver(
            "https://www.gulliver.co.il/")  # You can change to other browser drivers as needed
        self.driver.maximize_window()  # Maximize the browser window

    def navigate_to_homepage(self):
        self.driver.get("https://www.gulliver.co.il/")

    def get_title(self):
        return self.driver.title

    def search_for_flights(self, origin, destination, date):
        # Example logic for searching for flights
        origin_input = self.driver.find_element(By.ID, "origin-input")
        destination_input = self.driver.find_element(By.ID, "destination-input")
        date_input = self.driver.find_element(By.ID, "date-input")
        search_button = self.driver.find_element(By.ID, "search-button")

        origin_input.clear()
        origin_input.send_keys(origin)
        time.sleep(1)  # Add a short delay to allow suggestions to load
        origin_input.send_keys(Keys.RETURN)

        destination_input.clear()
        destination_input.send_keys(destination)
        time.sleep(1)
        destination_input.send_keys(Keys.RETURN)

        date_input.clear()
        date_input.send_keys(date)

        search_button.click()

    def select_first_flight(self):
        # Example logic for selecting the first flight in the search results
        first_flight = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='flight-result']"))
        )
        first_flight.click()

    def click_login_button(self):
        # Example logic for clicking the login button
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

    def click_register_button(self):
        # Example logic for clicking the register button
        register_button = self.driver.find_element(By.ID, "register-button")
        register_button.click()

    def click_special_deals_link(self):
        # Example logic for clicking the special deals link
        special_deals_link = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Special Deals')]")
        special_deals_link.click()

    def click_on_tuor_link(self):
        # Example logic for clicking the contact us link
        tour_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/glv-header-v3/div/div[3]/div[1]/a[3]"))
        )
        tour_link.click()
    def click_contact_us_link_organized(self):

        self.click_login_button()
        # Wait for an element that indicates the page is fully loaded
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'טיולים מאורגנים')]"))
        )

    def click_and_complete_package_tour(self):

        # Click on the "טיסות" link in the navigation menu
        flights_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/glv-header-v3/div/div[3]/div[1]/a[1]"))
        )
        flights_link.click()

        # Click on the "כרתים" destination
        eilat_destination = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'כרתים')]"))
        )
        eilat_destination.click()
        time.sleep(5)

        # Click on the "הזמן טיסה" button - updated XPath
        complete_reserve_button = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//*[@id='packages-results']/div[2]/div[2]/div[2]/div/generic-deals-group[1]/div[2]/generic-deal[1]/div/div[1]/div[2]/div[3]/div[6]/a"))
        )

    def close(self):
        self.driver.quit()
