import unittest
from Logic.task_agent import Agenda


class TestAgenda(unittest.TestCase):

    def setUp(self) -> None:
        self.wrapper = BrowserWrapper()
        self.driver = self.wrapper.get_driver()
        self.week_page = weekPage(self.driver)
        self.agenda = Agenda()

    def test_add_event(self):
        self.agenda.add_event("Meeting", "Discuss project", "2024-02-25")
        self.assertEqual(len(self.agenda.events), 1)
        self.assertEqual(self.agenda.events[0]["title"], "Meeting")

    def test_delete_event(self):
        self.agenda.add_event("Meeting", "Discuss project", "2024-02-25")
        self.agenda.delete_event("Meeting")
        self.assertEqual(len(self.agenda.events), 0)

    def test_edit_event(self):
        self.agenda.add_event("Meeting", "Discuss project", "2024-02-25")
        self.agenda.edit_event("Meeting", "Updated Meeting", "Discuss project updated", "2024-02-26")
        event = self.agenda.get_event_details("Updated Meeting")
        self.assertEqual(event["description"], "Discuss project updated")
        self.assertEqual(event["date"], "2024-02-26")

    def test_get_event_details(self):
        self.agenda.add_event("Meeting", "Discuss project", "2024-02-25")
        event = self.agenda.get_event_details("Meeting")
        self.assertEqual(event["description"], "Discuss project")
        self.assertEqual(event["date"], "2024-02-25")

    def test_search_event(self):
        self.agenda.add_event("Meeting", "Discuss project", "2024-02-25")
        self.agenda.add_event("Interview", "Job interview", "2024-02-26")
        results = self.agenda.search_event("Discuss")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Meeting")
