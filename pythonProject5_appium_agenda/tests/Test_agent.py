import unittest
from time import sleep

from appium.webdriver import webdriver

from infra.browser_wrapper import BrowserWrapper


class TestAgent(unittest.TestCase):
    def setUp(self):
        desired_caps = dict(
            platformName="Android",
            deviceName="emulator-5554",
            platformVersion="11.0",
            automationName="UiAutomator2",
            appPackage="com.claudivan.taskagenda",
            appActivity=".Activities.MainActivity t36"
        )
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()
        sleep(5)  # Allow time for the app to launch

    def test_create_event(self):
        self.driver.find_element_by_id("button_add_event").click()
        self.driver.find_element_by_id("editText_event_title").send_keys("Meeting")
        self.driver.find_element_by_id("editText_event_description").send_keys("Discuss project")
        self.driver.find_element_by_id("button_save_event").click()

    def test_delete_event(self):
        # Test deleting an existing event
        # Assuming there's a list of events and each event has a delete button with id "button_delete_event"
        # Assuming there's an event named "Meeting" that we want to delete
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Meeting"))')
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Meeting")').click()
        self.driver.find_element_by_id("button_delete_event").click()
        # Add assertions to verify event deletion, for example:
        # assert "Meeting" not in self.driver.page_source

    def test_edit_event(self):
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Meeting"))')
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Meeting")').click()
        self.driver.find_element_by_id("editText_event_title").clear()
        self.driver.find_element_by_id("editText_event_title").send_keys("Updated Meeting")
        self.driver.find_element_by_id("button_save_event").click()

    def test_view_event_details(self):
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Meeting"))')
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Meeting")').click()

    def test_search_event(self):
        self.driver.find_element_by_id("search_event").send_keys("Meeting")
        # Assuming there's a search button with id "button_search"
        self.driver.find_element_by_id("button_search").click()

    def tearDown(self):
        self.driver.quit()
