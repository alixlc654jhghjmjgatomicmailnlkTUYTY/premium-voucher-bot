import sqlite3
from datetime import datetime


DB = "database.db"



def connect():
    return sqlite3.connect(DB)



def init_db():

    db = connect()
    cur = db.cursor()


    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        balance INTEGER DEFAULT 0,
        join_date TEXT
    )
    """)



    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product TEXT,
        price INTEGER,
        voucher TEXT,
        status TEXT,
        date TEXT
    )
    """)



    cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount INTEGER,
        authority TEXT,
        status TEXT,
        date TEXT
    )
    """)



    # سرویس های ووچر

    cur.execute("""
    CREATE TABLE IF NOT EXISTS services(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        url TEXT,
        api_key TEXT,
        api_secret TEXT,
        status TEXT DEFAULT 'active'

    )
    """)



    db.commit()
    db.close()





# =====================
# کاربران
# =====================


def add_user(user_id, username):

    db = connect()
    cur = db.cursor()


    cur.execute("""
    INSERT OR IGNORE INTO users
    (user_id,username,balance,join_date)

    VALUES (?,?,?,?)
    """,
    (
        user_id,
        username,
        0,
        datetime.now().strftime("%Y-%m-%d")
    ))


    db.commit()
    db.close()





def get_balance(user_id):

    db = connect()
    cur = db.cursor()


    cur.execute(
        "SELECT balance FROM users WHERE user_id=?",
        (user_id,)
    )


    result = cur.fetchone()

    db.close()


    return result[0] if result else 0





def add_balance(user_id, amount):

    db = connect()
    cur = db.cursor()


    cur.execute("""
    UPDATE users
    SET balance = balance + ?
    WHERE user_id=?
    """,
    (
        amount,
        user_id
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





# =====================
# سفارشات
# =====================


def add_order(user_id, product, price, voucher=""):

    db = connect()
    cur = db.cursor()


    cur.execute("""
    INSERT INTO orders
    (user_id,product,price,voucher,status,date)

    VALUES (?,?,?,?,?,?)
    """,
    (
        user_id,
        product,
        price,
        voucher,
        "completed",
        datetime.now().strftime("%Y-%m-%d %H:%M")
    ))


    db.commit()
    db.close()





def orders_count():

    db = connect()
    cur = db.cursor()


    cur.execute(
        "SELECT COUNT(*) FROM orders"
    )


    result = cur.fetchone()[0]

    db.close()

    return result





# =====================
# پرداخت
# =====================


def add_transaction(user_id,amount,authority):

    db = connect()
    cur = db.cursor()


    cur.execute("""
    INSERT INTO transactions
    (user_id,amount,authority,status,date)

    VALUES (?,?,?,?,?)
    """,
    (
        user_id,
        amount,
        authority,
        "pending",
        datetime.now().strftime("%Y-%m-%d %H:%M")
    ))


    db.commit()
    db.close()





def complete_transaction(authority):

    db = connect()
    cur = db.cursor()


    cur.execute("""
    UPDATE transactions
    SET status='success'
    WHERE authority=?
    """,
    (authority,))


    db.commit()
    db.close()





# =====================
# اتصال سایت ووچر
# =====================


def add_service(
    name,
    url,
    api_key,
    api_secret=""
):

    db = connect()
    cur = db.cursor()


    cur.execute("""
    INSERT INTO services
    (name,url,api_key,api_secret,status)

    VALUES (?,?,?,?,?)
    """,
    (
        name,
        url,
        api_key,
        api_secret,
        "active"
    ))


    db.commit()
    db.close()





def get_services():

    db = connect()
    cur = db.cursor()


    cur.execute(
        "SELECT * FROM services"
    )


    data = cur.fetchall()

    db.close()

    return data





def get_active_service():

    db = connect()
    cur = db.cursor()


    cur.execute("""
    SELECT *
    FROM services
    WHERE status='active'
    LIMIT 1
    """)


    data = cur.fetchone()

    db.close()

    return data





def delete_service(service_id):

    db = connect()
    cur = db.cursor()


    cur.execute(
        "DELETE FROM services WHERE id=?",
        (service_id,)
    )


    db.commit()
    db.close()
