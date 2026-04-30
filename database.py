import sqlite3



       

def get_db():
    conn = sqlite3.connect("database.db")
    # conn = sqlite3.connect("foods.db")
    conn.row_factory = sqlite3.Row
    return conn

# def get_foods_db():
#     conn = sqlite3.connect("foods.db")
#     conn.row_factory = sqlite3.Row
#     return conn

def init_db():
    conn = get_db()
    # e_conn = get_foods_db()
    # Add your new table between lines 15 & 16.
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS foods (
            Food TEXT PRIMARY KEY,
            user TEXT,
            type TEXT,
            FOREIGN KEY (user) REFERENCES users(username)
        )
    """)    
    conn.commit()
    conn.close()