from appium.options.android import UiAutomator2Options
from selenium import webdriver


class BrowserWrapper:
    capabilities = dict(
        platformName="Android",
        deviceName="emulator-5554",
        platformVersion="11.0",
        automationName="UiAutomator2",
        appPackage="com.claudivan.taskagenda",
        appActivity=".Activities.MainActivity t36"
    )

    def __init__(self):
        self.driver = None
        print("test start")
        self.appium_server_url = 'http://localhost:4723'
        print(self.capabilities)
        self.capabilities_options = UiAutomator2Options().load_capabilities(self.capabilities)

    def get_driver(self):
        return webdriver.Remote(
            command_executor=self.appium_server_url,
            options=self.capabilities_options
        )
