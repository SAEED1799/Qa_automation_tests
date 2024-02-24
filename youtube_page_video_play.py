from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class Youtube_Page_Video_Play(BasePage):
    SEARCH_PLAY_VIDEO = "//a[@id='video-title']"

    def __init__(self, driver):
        self.driver = driver

    def search_flow(self, search_term):
        search_box = self.driver.find_element(By.NAME, "search_query")
        search_box.clear()
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)

        # Wait until the search results are loaded
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.SEARCH_PLAY_VIDEO))
        )

    def select_video(self):
        video_element = self.driver.find_element(By.XPATH, self.SEARCH_PLAY_VIDEO)

        video_element.click()

        # Wait for the video to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".html5-video-player"))
        )

    def play_video(self):
        try:
            # Wait for the play button to be clickable
            play_button = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH,self.SEARCH_PLAY_VIDEO))
            )
            # Click the play button
            play_button.click()
        except TimeoutException:
            print("Timeout: Play button not found or clickable within 30 seconds.")
            # You can choose to handle the error gracefully or raise it for the caller to handle.
            raise

    def is_video_playing(self):
        # Check if the video is playing
        video_player = self.driver.find_element(By.XPATH, self.SEARCH_PLAY_VIDEO)
        return video_player.get_attribute("aria-busy") == "false"
