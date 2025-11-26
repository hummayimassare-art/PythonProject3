# users.py
import sqlite3   # FIX: You forgot this import
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(conn, username, password, role):
    cursor = conn.cursor()
    password_hash = generate_password_hash(password)

    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
            (username, password_hash, role)
        )
        conn.commit()
        print(f"User '{username}' created successfully.")

    except sqlite3.IntegrityError:
        print(f"[ERROR] User '{username}' already exists. UNIQUE constraint failed.")

def get_all_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()
