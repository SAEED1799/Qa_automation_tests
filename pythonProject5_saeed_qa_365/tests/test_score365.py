import unittest
from selenium import webdriver
from logic.website_interactions import WebsiteInteractions


class TestScore365(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.browser = BrowserWrapper()
        self.driver.maximize_window()

    def test_homepage_title(self):
        website = WebsiteInteractions(self.driver)
        website.navigate_to_homepage()
        website.wait_for_title()
        actual_title = website.get_title()
        print("Actual title:", actual_title)
        expected_title = "365Scores - תוצאות לייב, סטטיסטיקות וחדשות"
        self.assertIn(expected_title, actual_title)

    def test_search_for_team(self):
        website = WebsiteInteractions(self.driver)
        website.navigate_to_homepage()
        website.search_for_team("ריאל מדריד")

    def test_check_popular_events_exist(self):
        website = WebsiteInteractions(self.driver)
        website.navigate_to_homepage()
        popular_events_exist = website.check_popular_events_exist()
        self.assertFalse(popular_events_exist, "Popular events not found on homepage")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
