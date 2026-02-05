"""
Main entry point for the Task Manager Application.
"""
import sys
from models import Task
from database import Database

def print_menu():
    print("\n=== Task Manager ===")
    print("1. List Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

def list_tasks(db):
    tasks = db.get_all_tasks()
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nYour Tasks:")
        for t in tasks:
            print(t)

def add_task(db):
    title = input("Title: ")
    desc = input("Description: ")
    due = input("Due Date (optional): ")
    task = Task(title, desc, due)
    db.add_task(task)
    print("Task added successfully.")

def complete_task(db):
    try:
        task_id = int(input("Task ID to complete: "))
        db.update_task_status(task_id, True)
        print("Task updated.")
    except ValueError:
        print("Invalid ID.")

def delete_task(db):
    try:
        task_id = int(input("Task ID to delete: "))
        db.delete_task(task_id)
        print("Task deleted.")
    except ValueError:
        print("Invalid ID.")

def main():
    db = Database('my_tasks.db')
    
    while True:
        print_menu()
        choice = input("Select an option: ")
        
        if choice == '1':
            list_tasks(db)
        elif choice == '2':
            add_task(db)
        elif choice == '3':
            complete_task(db)
        elif choice == '4':
            delete_task(db)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()
