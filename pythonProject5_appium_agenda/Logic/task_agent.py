from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy


class Agenda:
    def __init__(self):
        self.events = []

    def add_event(self, title, description, date):
        event = {"title": title, "description": description, "date": date}
        self.events.append(event)

    def delete_event(self, title):
        for event in self.events:
            if event["title"] == title:
                self.events.remove(event)

    def edit_event(self, title, new_title, new_description, new_date):
        for event in self.events:
            if event["title"] == title:
                event["title"] = new_title
                event["description"] = new_description
                event["date"] = new_date

    def get_event_details(self, title):
        for event in self.events:
            if event["title"] == title:
                return event

    def search_event(self, query):
        results = []
        for event in self.events:
            if query.lower() in event["title"].lower() or query.lower() in event["description"].lower():
                results.append(event)
        return results

