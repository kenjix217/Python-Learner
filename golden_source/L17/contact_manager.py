"""
Lesson 17: Working with Databases
Golden Source Solution: Contact Manager

This script demonstrates basic database operations using SQLite:
1. Creating a database and table
2. Inserting data
3. Querying data
4. Updating records
5. Deleting records
""",
import sqlite3
import os

DB_NAME = 'contacts.db'

def create_connection():
    """Create a database connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """Create the contacts table if it doesn't exist."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT,
        email TEXT
    );
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("Table 'contacts' created successfully.")
    except sqlite3.Error as e:
        print(e)

def add_contact(conn, contact):
    """Insert a new contact into the contacts table."""
    sql = '''INSERT INTO contacts(name, phone, email)
              VALUES(?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, contact)
    conn.commit()
    return cur.lastrowid

def get_all_contacts(conn):
    """Query all rows in the contacts table."""
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    print("\n--- All Contacts ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}")
    return rows

def find_contact_by_name(conn, name):
    """Query tasks by name."""
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE name=?", (name,))
    rows = cur.fetchall()
    print(f"\n--- Search Result for '{name}' ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}")
    return rows

def update_contact_phone(conn, id, new_phone):
    """Update priority of a task"""
    sql = ''' UPDATE contacts
              SET phone = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (new_phone, id))
    conn.commit()
    print(f"\nUpdated contact ID {id} with new phone: {new_phone}")

def delete_contact(conn, id):
    """Delete a task by task id"""
    sql = 'DELETE FROM contacts WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    print(f"\nDeleted contact ID {id}")

def main():
    # Clean up previous run
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

    conn = create_connection()

    if conn is not None:
        create_table(conn)

        # 1. Insert at least 5 contacts
        contacts = [
            ('Alice Smith', '555-0101', 'alice@example.com'),
            ('Bob Jones', '555-0102', 'bob@example.com'),
            ('Charlie Brown', '555-0103', 'charlie@example.com'),
            ('Diana Prince', '555-0104', 'diana@example.com'),
            ('Evan Wright', '555-0105', 'evan@example.com')
        ]
        
        print("\nAdding contacts...")
        for contact in contacts:
            add_contact(conn, contact)

        # 2. Query to find all contacts
        get_all_contacts(conn)

        # 3. Query to search by name
        find_contact_by_name(conn, 'Charlie Brown')

        # 4. Update a contact's phone (Let's update Bob, who should have ID 2)
        update_contact_phone(conn, 2, '555-9999')
        
        # Verify update
        find_contact_by_name(conn, 'Bob Jones')

        # 5. Delete a contact (Let's delete Evan, who should have ID 5)
        delete_contact(conn, 5)

        # Final verification
        get_all_contacts(conn)

        conn.close()
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
