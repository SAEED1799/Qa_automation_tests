import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from infra.browser_wrapper import BrowserWrapper
from logic.youtube_page import YouTubePage
from logic.youtube_page_history import Youtube_Page_History
from logic.youtube_page_search_subscription import Youtube_Page_Search_Subscription
from logic.youtube_page_search_live_cannel import Youtube_Page_Search_live_Channel
from logic.youtube_page_youtube_icon_to_home_page import Youtube_Page_Youtube_Icon_To_Home_Page
from logic.youtube_page_search_short_channel import Youtube_Page_Search_short_Channel
from logic.youtube_page_video_play import Youtube_Page_Video_Play
# from logic.youtube_page_test_speed_video import Youtube_Page_Test_Speed_Video
from logic.youtube_page_mute_video import Mute_Video_Page
from logic.youtube_page_screen_video import Screen_Video_Page

class Youtube_Page_Test(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://www.youtube.com")
    def test_check_title_for_search(self):
        self.youtube_page = YouTubePage(self.driver)
        self.youtube_page.search_flow("Python programming")
        time.sleep(10)# we need to use Explicit Wait insted
        self.assertIn("Python programming",self.youtube_page.get_page_title(),"the title not show")#test/logic

    def test_check_seach_history_aycon(self):
        self.youtube_page = Youtube_Page_History(self.driver)
        self.youtube_page.click_btn()

    def test_check_seach_subscribtion_aycon(self):
        self.youtube_page = Youtube_Page_Search_Subscription(self.driver)
        self.youtube_page.click_subscription()

    def test_check_seach_live_channel(self):
        self.youtube_page = Youtube_Page_Search_live_Channel(self.driver)
        self.youtube_page.click_channel()

    def test_check_youtube_aycon_to_home_page(self):
        self.youtube_page = Youtube_Page_Youtube_Icon_To_Home_Page(self.driver)
        self.youtube_page.click_youtube()

    def test_check_search_short_channel(self):
        self.youtube_page = Youtube_Page_Search_short_Channel(self.driver)
        self.youtube_page.click_short_channel()

    def test_video_playback(self):
        # Search for a video
        self.youtube_page = Youtube_Page_Video_Play(self.driver)
        search_term = "xiaomi car"
        time.sleep(10)
        self.youtube_page.search_flow(search_term)
        time.sleep(10)
        # # Select the first video from the search results
        self.youtube_page.select_video()

        #Play the video
        self.youtube_page.play_video()

        # # Check if the video is playing
        is_playing = self.youtube_page.is_video_playing()
        #
        # # Verify that the video is playing
        # self.assertIn(is_playing, f"The video '{search_term}' is not playing")

    def test_mute_video(self):
        self.video_page = Mute_Video_Page(self.driver)
        # Navigate to video page
        self.video_page.go_to_video("https://www.youtube.com/watch?v=hVnTYxNzP80")

        # Mute the video
        self.video_page.mute_video()

        # Check if the video is muted
        self.assertTrue(self.video_page.is_video_muted(), "Video is not muted.")

    def test_screen_video(self):
        self.video_page = Screen_Video_Page(self.driver)
        # Navigate to video page
        self.video_page.go_to_video("https://www.youtube.com/watch?v=hVnTYxNzP80")

        # Mute the video
        self.video_page.screen_video()

        # Check if the video is muted
        self.assertTrue(self.video_page.is_video_screened(), "Video is not screened.")

    def tearDown(self):
        self.driver.close()


