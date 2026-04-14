import sqlite3


def seed_database():
    """Add sample users to the database"""
    conn = get_db()
    # Add sample users here if needed
     sample_users = [
        ("alice", "Password123!"),
        ("bob", "SecurePass456@"),
        ("charlie", "MyPassword789#"),
    ]
       

def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    # Add your new table between lines 15 & 16.
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()