import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(
    os.path.dirname(__file__),
    "attendance.db"
)

def init_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def mark_attendance_db(name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    today = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        SELECT * FROM attendance
        WHERE name = ? AND date = ?
    """, (name, today))

    result = cursor.fetchone()

    if result is None:
        time_now = datetime.now().strftime("%H:%M:%S")

        cursor.execute("""
            INSERT INTO attendance (name, date, time)
            VALUES (?, ?, ?)
        """, (name, today, time_now))

        conn.commit()
        print(f"Attendance saved in DB: {name} at {time_now}")

    conn.close()

def get_all_attendance():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attendance")
    records = cursor.fetchall()

    conn.close()
    return records

def clear_attendance():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM attendance")
    conn.commit()
    conn.close()

def init_admin_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()