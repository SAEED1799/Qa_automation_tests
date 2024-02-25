from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebsiteInteractions:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_homepage(self):
        self.driver.get("https://www.365scores.com/he")

    def wait_for_title(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, "title")))

    def get_title(self):
        return self.driver.title

    def is_element_present(self, element_id):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, element_id))
            )
            return True
        except TimeoutException:
            return False

    def search_for_team(self, team_name):
        try:
            search_input = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@class='search']")))
            search_input.clear()
            search_input.send_keys(team_name)
            search_input.send_keys(Keys.ENTER)
        except TimeoutException:
            print("Timeout: Search input field not found.")

    def is_team_found(self):
        try:
            team_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='search-result']//div[@class='team-name']")))
            return True
        except:
            return False

    def check_popular_events_exist(self):
        try:
            popular_events_section = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='popular-events']")))
            return True
        except:
            return False