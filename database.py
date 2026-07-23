import sqlite3
from datetime import datetime


DATABASE = "premium_bot.db"



def connect():

    return sqlite3.connect(DATABASE)



def create_tables():

    db = connect()
    cursor = db.cursor()


    # کاربران
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        user_id INTEGER PRIMARY KEY,

        username TEXT,

        balance INTEGER DEFAULT 0,

        status TEXT DEFAULT 'active',

        created_at TEXT

    )
    """)



    # ووچرها
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vouchers(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        code TEXT UNIQUE,

        amount INTEGER,

        used INTEGER DEFAULT 0,

        created_at TEXT

    )
    """)



    # سفارش‌ها
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        amount INTEGER,

        status TEXT,

        voucher TEXT,

        created_at TEXT

    )
    """)


    db.commit()
    db.close()





def add_user(user_id, username):

    db = connect()
    cursor = db.cursor()


    cursor.execute("""
    INSERT OR IGNORE INTO users
    (
        user_id,
        username,
        created_at
    )

    VALUES(?,?,?)

    """,

    (
        user_id,
        username,
        str(datetime.now())
    ))


    db.commit()
    db.close()





def get_balance(user_id):

    db = connect()
    cursor = db.cursor()


    cursor.execute(
        "SELECT balance FROM users WHERE user_id=?",
        (user_id,)
    )


    result = cursor.fetchone()

    db.close()


    if result:
        return result[0]

    return 0





def add_balance(user_id, amount):

    db = connect()
    cursor = db.cursor()


    cursor.execute(
        """
        UPDATE users

        SET balance = balance + ?

        WHERE user_id=?

        """,

        (
            amount,
            user_id
        )
    )


    db.commit()
    db.close()





def users_count():

    db = connect()
    cursor = db.cursor()


    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )


    count = cursor.fetchone()[0]


    db.close()

    return count





def add_voucher(code, amount):

    db = connect()
    cursor = db.cursor()


    cursor.execute(
        """
        INSERT INTO vouchers
        (
            code,
            amount,
            created_at
        )

        VALUES(?,?,?)

        """,

        (
            code,
            amount,
            str(datetime.now())
        )
    )


    db.commit()
    db.close()





def vouchers_count():

    db = connect()
    cursor = db.cursor()


    cursor.execute(
        "SELECT COUNT(*) FROM vouchers"
    )


    count = cursor.fetchone()[0]


    db.close()

    return count
