# main.py
from app.data.schema import create_tables
from services.user_service import migrate_users_from_file
from app.data.db import connect_database
from app.data import users, incidents

def main():
    print("Creating database and tables...")
    create_tables()

    print("\nMigrating users from users.txt...")
    migrate_users_from_file()

    print("\nLoading CSV files with Pandas...")
    # Add the load_csv_to_table calls here as above

    conn = connect_database()

    print("\nTesting CRUD Operations:")

    # Test User CRUD
    users.create_user(conn, "bob", "secret123", "admin")
    print("All users:", [dict(u) for u in users.get_all_users(conn)])

    # Test Incident CRUD
    incidents.insert_incident(conn, "Ransomware Attack", "Critical", "Critical")
    print("Incidents:", [dict(i) for i in incidents.get_all_incidents(conn)])

    conn.close()
    print("\nWeek 8 tasks completed successfully!")

if __name__ == "__main__":
    main()