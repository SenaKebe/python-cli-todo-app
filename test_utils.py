import unittest
from utils import get_next_id, filter_today_tasks
from task import Task
from datetime import date

class TestUtils(unittest.TestCase):

    def test_get_next_id_with_tasks(self):
        tasks = [Task(1, "Test1", "Desc1", "2025-06-18"), Task(2, "Test2", "Desc2", "2025-06-19")]
        self.assertEqual(get_next_id(tasks), 3)

    def test_get_next_id_empty(self):
        self.assertEqual(get_next_id([]), 1)

    def test_filter_today_tasks(self):
        today_str = date.today().isoformat()
        tasks = [
            Task(1, "Task 1", "Today Task", today_str),
            Task(2, "Task 2", "Future Task", "2099-01-01")
        ]
        filtered = filter_today_tasks(tasks)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "Task 1")

if __name__ == "__main__":
    unittest.main()
