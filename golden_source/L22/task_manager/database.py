"""
Database abstraction layer for Task Manager.
"""
import sqlite3
from models import Task

class Database:
    def __init__(self, db_name='tasks.db'):
        self.db_name = db_name
        self.create_table()

    def get_connection(self):
        """Create a database connection."""
        return sqlite3.connect(self.db_name)

    def create_table(self):
        """Create tasks table if not exists."""
        sql = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            completed BOOLEAN DEFAULT 0,
            created_at TEXT
        );
        """
        conn = self.get_connection()
        conn.execute(sql)
        conn.commit()
        conn.close()

    def add_task(self, task):
        """Add a new task."""
        sql = "INSERT INTO tasks (title, description, due_date, completed, created_at) VALUES (?, ?, ?, ?, ?)"
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute(sql, (task.title, task.description, task.due_date, task.completed, task.created_at))
        conn.commit()
        task.id = cur.lastrowid
        conn.close()
        return task.id

    def get_all_tasks(self):
        """Retrieve all tasks."""
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks")
        rows = cur.fetchall()
        conn.close()
        
        tasks = []
        for row in rows:
            # row: id, title, desc, due, completed, created
            t = Task(row[1], row[2], row[3], bool(row[4]), row[0])
            tasks.append(t)
        return tasks

    def update_task_status(self, task_id, completed):
        """Update completion status."""
        sql = "UPDATE tasks SET completed = ? WHERE id = ?"
        conn = self.get_connection()
        conn.execute(sql, (completed, task_id))
        conn.commit()
        conn.close()
    
    def delete_task(self, task_id):
        """Delete a task."""
        sql = "DELETE FROM tasks WHERE id = ?"
        conn = self.get_connection()
        conn.execute(sql, (task_id,))
        conn.commit()
        conn.close()
