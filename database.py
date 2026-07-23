import sqlite3
from datetime import datetime


DB = "database.db"



def connect():

    return sqlite3.connect(DB)



def init_db():

    db = connect()
    cursor = db.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        user_id INTEGER PRIMARY KEY,
        username TEXT,
        balance INTEGER DEFAULT 0,
        join_date TEXT

    )
    """)



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product TEXT,
        price INTEGER,
        status TEXT,
        date TEXT

    )
    """)



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount INTEGER,
        authority TEXT,
        status TEXT,
        date TEXT

    )
    """)



    db.commit()
    db.close()




def add_user(user_id, username):

    db = connect()
    cursor = db.cursor()


    cursor.execute(
        """
        INSERT OR IGNORE INTO users
        VALUES(?,?,?,?)
        """,
        (
            user_id,
            username,
            0,
            datetime.now().strftime("%Y-%m-%d")
        )
    )


    db.commit()
    db.close()





def get_balance(user_id):

    db = connect()
    cursor = db.cursor()


    cursor.execute(
        "SELECT balance FROM users WHERE user_id=?",
        (user_id,)
    )


    data = cursor.fetchone()

    db.close()


    if data:
        return data[0]

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





def add_transaction(
        user_id,
        amount,
        authority
):

    db = connect()
    cursor = db.cursor()


    cursor.execute(
        """
        INSERT INTO transactions
        VALUES(NULL,?,?,?,?,?)
        """,
        (
            user_id,
            amount,
            authority,
            "pending",
            datetime.now().strftime("%Y-%m-%d %H:%M")
        )
    )


    db.commit()
    db.close()





def complete_transaction(authority):

    db = connect()
    cursor = db.cursor()


    cursor.execute(
        """
        UPDATE transactions
        SET status='success'
        WHERE authority=?
        """,
        (authority,)
    )


    db.commit()
    db.close()
