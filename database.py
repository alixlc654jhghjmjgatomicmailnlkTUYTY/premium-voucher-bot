import sqlite3


db = sqlite3.connect("bot.db")
cursor = db.cursor()


def create_tables():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT,
        balance INTEGER DEFAULT 0
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vouchers(
        code TEXT PRIMARY KEY,
        value INTEGER,
        used INTEGER DEFAULT 0
    )
    """)

    db.commit()



def add_user(user_id, username):

    cursor.execute(
        "INSERT OR IGNORE INTO users(id,username) VALUES(?,?)",
        (user_id, username)
    )

    db.commit()



def get_users():

    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )

    return cursor.fetchone()[0]
