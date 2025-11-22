# app/data/schema.py
# FIXED VERSION – works when run directly OR imported

import sys
from pathlib import Path

# Add the project root to Python path so imports work when running this file directly
sys.path.append(str(Path(__file__).parent.parent.parent))

# Now we can import normally (no dot!)
from app.data.db import connect_database

def create_tables():
    conn = connect_database()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'user'
        )
    """)

    # Cyber Incidents table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cyber_incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            severity TEXT NOT NULL,
            status TEXT DEFAULT 'open',
            date TEXT
        )
    """)

    # Datasets Metadata table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS datasets_metadata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            source TEXT,
            category TEXT,
            size INTEGER
        )
    """)

    # IT Tickets table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS it_tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT DEFAULT 'open',
            created_date TEXT
        )
    """)

    conn.commit()
    conn.close()
    print("All tables created successfully.")

# This allows you to run schema.py directly for testing
if __name__ == "__main__":
    create_tables()