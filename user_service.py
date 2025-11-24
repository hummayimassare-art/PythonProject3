# services/user_service.py
import bcrypt
import sqlite3
from db import connect_database

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def migrate_users_from_file(filepath="users.txt"):
    conn = connect_database()
    cursor = conn.cursor()

    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line or ":" not in line:
                continue
            username, password, role = line.split(":")
            role = role.strip() if role else "user"
            password_hash = hash_password(password)

            try:
                cursor.execute(
                    "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                    (username, password_hash, role)
                )
            except sqlite3.IntegrityError:
                print(f"User {username} already exists, skipping.")

    conn.commit()
    conn.close()
    print("User migration completed.")