import sqlite3

def create_table():

    conn = sqlite3.connect("users.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS password_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password TEXT,
        score INTEGER,
        strength TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_result(password, score, strength):

    conn = sqlite3.connect("users.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO password_history
    (password, score, strength)
    VALUES (?, ?, ?)
    """, (password, score, strength))

    conn.commit()
    conn.close()