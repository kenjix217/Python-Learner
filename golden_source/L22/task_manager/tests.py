"""
Unit tests for Task Manager.
"""
import unittest
import os
from models import Task
from database import Database

class TestTaskManager(unittest.TestCase):
    
    def setUp(self):
        """Use a temporary database for testing."""
        self.test_db = 'test_tasks.db'
        self.db = Database(self.test_db)
        # Clear table
        conn = self.db.get_connection()
        conn.execute("DELETE FROM tasks")
        conn.commit()
        conn.close()

    def tearDown(self):
        """Clean up database file."""
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_task_model(self):
        """Test Task model creation."""
        t = Task("Test", "Desc")
        self.assertEqual(t.title, "Test")
        self.assertFalse(t.completed)
        t.mark_complete()
        self.assertTrue(t.completed)

    def test_database_add_get(self):
        """Test adding and retrieving tasks."""
        t = Task("Buy Milk", "Groceries")
        self.db.add_task(t)
        
        tasks = self.db.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Buy Milk")

    def test_database_delete(self):
        """Test deleting a task."""
        t = Task("Delete Me", "...")
        t_id = self.db.add_task(t)
        
        self.db.delete_task(t_id)
        tasks = self.db.get_all_tasks()
        self.assertEqual(len(tasks), 0)

if __name__ == '__main__':
    unittest.main()
