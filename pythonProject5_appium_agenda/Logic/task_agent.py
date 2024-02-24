from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy

class takeAhent():
    def __init__(self,driver):
         self.driver=driver

        #

    def init_final_result(self):
         self.result_button=self.driver.find_element(by=AppiumBy.ID, value=self.RESULT)


    def add_function(self,num_one,num_two):
        self.click_on_number(num_one)
        self.add_button.click()
        self.click_on_number(num_two)
        self.equal_button.click()
        self.init_final_result()
        return self.result_button.text

    def substract_function(self,num_one,num_two):
        self.click_on_number(num_one)
        self.subtract_button.click()
        self.click_on_number(num_two)
        self.equal_button.click()
        self.init_final_result()
        return self.result_button.text
    def click_on_number(self,number):
        self._driver.find_element(by=AppiumBy.ID, value=f'com.google.android.calculator:id/digit_{number}').click()
    def multiply_function(self,num_one,num_two):
        self.click_on_number(num_one)
        self.mult_button.click()
        self.click_on_number(num_two)
        self.equal_button.click()
        self.init_final_result()
        return self.result_button.text


    def divid_function(self,num_one,num_two):
        self.click_on_number(num_one)
        self.div_button.click()
        self.click_on_number(num_two)
        self.equal_button.click()
        self.init_final_result()
        return self.result_button.text
