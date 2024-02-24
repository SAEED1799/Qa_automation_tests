from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from infra.base_page import BasePage


class Youtube_Page_Youtube_Icon_To_Home_Page(BasePage):
    SEARCH_INPUT_YOUTUBE_ICON_HOME_PAGE = "//ytd-masthead[./div[./div[./ytd-topbar-logo-renderer[./a[./div" \
                   "[./ytd-logo[./*[@id='logo-icon']]]]]]]]"

    def __int__(self, driver):
        super().__init__(driver)
        self.search_input_youtube_icon_home_page = self.driver.find_element(By.XPATH, self.SEARCH_INPUT_YOUTUBE_ICON_HOME_PAGE)  # logic


    def click_youtube(self):
        try:
            self.search_input_subscription = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.SEARCH_INPUT_YOUTUBE_ICON_HOME_PAGE)))  # logic
            self.search_input_youtube_icon_home_page.click()
            WebDriverWait(self._driver, 5).until(EC.alert_is_present())

        except Exception as e:
            print("ok")
