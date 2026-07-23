import sqlite3
from datetime import datetime


DB = "database.db"


def connect():
    return sqlite3.connect(DB)


# ساخت جدول ها
def init_db():

    db = connect()
    cursor = db.cursor()


    # کاربران
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        balance INTEGER DEFAULT 0,
        join_date TEXT
    )
    """)


    # محصولات
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price INTEGER,
        stock INTEGER DEFAULT 0
    )
    """)


    # سفارشات
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


    # ووچرها
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vouchers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT,
        product TEXT,
        used INTEGER DEFAULT 0
    )
    """)


    db.commit()
    db.close()



# اضافه کردن کاربر
def add_user(user_id, username):

    db = connect()
    cursor = db.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO users
    VALUES(?,?,?,?)
    """,
    (
        user_id,
        username,
        0,
        datetime.now().strftime("%Y-%m-%d")
    ))

    db.commit()
    db.close()



# گرفتن موجودی کاربر
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



# افزایش موجودی
def add_balance(user_id, amount):

    db = connect()
    cursor = db.cursor()

    cursor.execute("""
    UPDATE users
    SET balance = balance + ?
    WHERE user_id=?
    """,
    (amount,user_id))


    db.commit()
    db.close()



# ثبت سفارش
def add_order(user_id, product, price):

    db = connect()
    cursor = db.cursor()

    cursor.execute("""
    INSERT INTO orders
    VALUES(NULL,?,?,?,?,?)
    """,
    (
        user_id,
        product,
        price,
        "pending",
        datetime.now().strftime("%Y-%m-%d %H:%M")
    ))

    db.commit()
    db.close()



# اضافه کردن ووچر
def add_voucher(code, product):

    db = connect()
    cursor = db.cursor()

    cursor.execute("""
    INSERT INTO vouchers
    VALUES(NULL,?,?,0)
    """,
    (
        code,
        product
    ))

    db.commit()
    db.close()



# گرفتن ووچر سالم
def get_voucher(product):

    db = connect()
    cursor = db.cursor()

    cursor.execute("""
    SELECT id,code 
    FROM vouchers
    WHERE product=? AND used=0
    LIMIT 1
    """,
    (product,))


    data = cursor.fetchone()


    if data:

        cursor.execute("""
        UPDATE vouchers
        SET used=1
        WHERE id=?
        """,
        (data[0],))


        db.commit()


    db.close()


    if data:
        return data[1]

    return None



# آمار کاربران
def users_count():

    db = connect()
    cursor=db.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )

    x=cursor.fetchone()[0]

    db.close()

    return x



# آمار سفارش
def orders_count():

    db = connect()
    cursor=db.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM orders"
    )

    x=cursor.fetchone()[0]

    db.close()

    return x
