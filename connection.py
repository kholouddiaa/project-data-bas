import sqlite3

def connect_db():
    conn = sqlite3.connect("Uni_management.db")
    cursor = conn.cursor()
    with open('uni.sql', 'r') as file:
        schema = file.read()
        cursor.executescript(schema)
        conn.commit()

    return conn

def execute_query(query, params=()):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        conn.commit()
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()