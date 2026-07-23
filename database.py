import sqlite3
from datetime import datetime


DB_NAME = "premium.db"


def connect():
    return sqlite3.connect(DB_NAME)



def create_tables():

    db = connect()
    cur = db.cursor()


    # کاربران
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        balance INTEGER DEFAULT 0,
        created_at TEXT
    )
    """)


    # ووچرها
    cur.execute("""
    CREATE TABLE IF NOT EXISTS vouchers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT UNIQUE,
        amount INTEGER,
        used INTEGER DEFAULT 0,
        created_at TEXT
    )
    """)


    db.commit()
    db.close()



def add_user(user_id, username):

    db = connect()
    cur = db.cursor()

    cur.execute("""
    INSERT OR IGNORE INTO users
    (user_id, username, created_at)
    VALUES (?, ?, ?)
    """,
    (
        user_id,
        username,
        str(datetime.now())
    ))

    db.commit()
    db.close()



def users_count():

    db = connect()
    cur = db.cursor()

    cur.execute(
        "SELECT COUNT(*) FROM users"
    )

    result = cur.fetchone()[0]

    db.close()

    return result



def add_voucher(code, amount):

    db = connect()
    cur = db.cursor()

    cur.execute("""
    INSERT INTO vouchers
    (code, amount, created_at)
    VALUES (?, ?, ?)
    """,
    (
        code,
        amount,
        str(datetime.now())
    ))

    db.commit()
    db.close()
