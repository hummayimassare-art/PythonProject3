# app/data/db.py
import sqlite3
from pathlib import Path

DATABASE_PATH = Path("trial/intelligence_platform.db")

def connect_database():
    """Return a connection to the SQLite database"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # Allows column access by name
    return conn