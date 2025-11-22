# app/data/incidents.py

def get_all_incidents(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cyber_incidents")
    return cursor.fetchall()

def insert_incident(conn, title: str, severity: str, status: str = "open", date: str = None):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO cyber_incidents (title, severity, status, date) VALUES (?, ?, ?, ?)",
        (title, severity, status, date)
    )
    conn.commit()
    return cursor.lastrowid

def update_incident_status(conn, incident_id: int, new_status: str):
    cursor = conn.cursor()
    cursor.execute("UPDATE cyber_incidents SET status = ? WHERE id = ?", (new_status, incident_id))
    conn.commit()

def delete_incident(conn, incident_id: int):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cyber_incidents WHERE id = ?", (incident_id,))
    conn.commit()