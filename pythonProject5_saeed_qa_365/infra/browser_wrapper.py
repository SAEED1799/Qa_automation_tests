import os

import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


class BrowserWrapper:
    # def __init__(self):
    #     try:
    #         with open('infra/config.json') as f:
    #             self.config = json.load(f)
    #     except FileNotFoundError:
    #         print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
    #         raise  # Raise the error to halt execution if the file is essential for the script to run
    #     self.browser_name = None
    #     self.driver = None
    def __init__(self):
        config_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'config.json'))
        try:
            with open(config_file_path) as f:
                self.config = json.load(f)
        except FileNotFoundError:
            print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
            raise  # Raise the error to halt execution if the file is essential for the script to run
        self.browser_name = None
        self.driver = None

    def start_browser(self):
        self.browser_name = self.config.get("browser_name")
        if self.browser_name.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif self.browser_name.lower() == 'firefox':
            self.driver = webdriver.Firefox(service=FirefoxService(executable_path="/path/to/geckodriver"))
        elif self.browser_name.lower() == 'edge':
            self.driver = webdriver.Edge(service=EdgeService(executable_path="/path/to/msedgedriver"))
        else:
            raise ValueError("Invalid browser specified")

    def get_driver(self, browser):
        browser_wrapper = self.config["browser_name"]
        if self.config.get("grid"):
            options = self.set_up_capabilities(browser)
            self.driver = webdriver.Remote(command_executor=self.config["hub"], options=options)
        else:
            if browser_wrapper.lower() == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser_wrapper.lower() == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser_wrapper.lower() == 'edge':
                self.driver = webdriver.Edge()
        url = self.config["url"]
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(4)
        return self.driver

    def close_browser(self):
        if self.driver:
            self.driver.quit()
