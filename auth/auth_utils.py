import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

DB_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "database",
    "attendance.db"
)

def create_admin(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    hashed_password = generate_password_hash(password)

    cursor.execute("""
        INSERT INTO admin (username, password)
        VALUES (?, ?)
    """, (username, hashed_password))

    conn.commit()
    conn.close()


def verify_admin(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT password FROM admin WHERE username = ?
    """, (username,))

    result = cursor.fetchone()
    conn.close()

    if result is None:
        return False

    return check_password_hash(result[0], password)