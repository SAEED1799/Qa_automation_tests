import time

from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy

from Logic.clock_page import clockPage


class newEventPage():
    EVENT_NAME= "com.claudivan.taskagenda:id/etTitulo"
    SAVE_EVENT = "com.claudivan.taskagenda:id/item_salvar"
    TIME_FIELD = "com.claudivan.taskagenda:id/btHora"
    TASK_TYPE = "com.claudivan.taskagenda:id/tvTipo"
    DESCRIPTION = "com.claudivan.taskagenda:id/etDescricao"
    ADD_REMINDER = "com.claudivan.taskagenda:id/btAdicionarNotificacao"
    IMPORTANT_EVENT = "//android.widget.ListView[@resource-id='android:id/select_dialog_listview']/android.widget.RelativeLayout[1]"
    TASK_EVENT = "//android.widget.ListView[@resource-id='android:id/select_dialog_listview']/android.widget.RelativeLayout[2]"
    NOT_FORGET_EVENT="//android.widget.ListView[@resource-id='android:id/select_dialog_listview']/android.widget.RelativeLayout[3]"
    DATE_FIELD ="//android.widget.TextView[@resource-id='com.claudivan.taskagenda:id/btData']"
    DATE_YEAR = "android:id/date_picker_header_year"





    def __init__(self,driver):
        self.driver=driver
        self.init_elements()

    def init_elements(self):
        self.event_name = self.driver.find_element(by=AppiumBy.ID, value=self.EVENT_NAME)
        self.save_event = self.driver.find_element(by=AppiumBy.ID, value=self.SAVE_EVENT)
        self.time_field = self.driver.find_element(by=AppiumBy.ID, value=self.TIME_FIELD)
        self.task_type = self.driver.find_element(by=AppiumBy.ID, value=self.TASK_TYPE)
        self.description =self.driver.find_element(by=AppiumBy.ID, value=self.DESCRIPTION)
        self.add_reminder =self.driver.find_element(by=AppiumBy.ID, value=self.ADD_REMINDER)
        self.date_field =self.driver.find_element(by=AppiumBy.XPATH, value=self.DATE_FIELD)



    def click_add_event_button(self):
        self.add_event_button.click()


    def init_time_fiels(self):
        self.time_field = self.driver.find_element(by=AppiumBy.ID, value=self.TIME_FIELD)

    def fill_description(self,text):
        self.description.send_keys(text)
    def fill_name(self,text):
        self.event_name.send_keys(text)
    def fill_date(self,date):
        pass
    def click_time(self):
        self.time_field.click()


    def choose_year(self,year):
        pass

    def choose_event_type(self,type):
        #type should be "Important", "Task" or "Not forgot"
        if type.lower() != 'not forgot' and type.lower() != 'important' and type.lower() != 'task':
            raise ValueError('invalid event type')
        if type.lower() == 'not forgot':
            self.event_type = self.driver.find_element(by=AppiumBy.XPATH, value=self.NOT_FORGET_EVENT).click()
        if type.lower() == 'important':
            self.event_type = self.driver.find_element(by=AppiumBy.XPATH, value=self.IMPORTANT_EVENT).click()
        if type.lower() == 'task':
            self.event_type = self.driver.find_element(by=AppiumBy.XPATH, value=self.TASK_EVENT).click()



    def create_event(self,event_name,hour,minute,type,description):
        self.event_name.send_keys(event_name)
        self.click_time()
        time_page = clockPage(self.driver)
        time_page.fill_time(hour,minute)
        time.sleep(1)
        self.task_type.click()

        self.choose_event_type(type)
        self.description.click()
        self.fill_description(description)
        self.save_event.click()


    def choose_time(self,hour,minute):

        self.click_time()
        time_page = clockPage(self.driver)
        time_page.fill_time(hour,minute)
        time.sleep(1)
        self.init_time_fiels()

    def get_time_field_text(self):
        return self.time_field.text


    def get_date_field_text(self):
        return self.date_field.text
