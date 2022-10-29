
import sqlite3
from sqlite3 import Error


DB_NAME = "phone-note.db"


def connect():
    try:
        con = sqlite3.connect(DB_NAME)
        return con
    except Error:
        print(Error)
        raise Error


def init():
    conn = connect()
    print(f"Connecte to {DB_NAME}")

    peoplesTable = """CREATE TABLE IF NOT EXISTS peoples(
            id INTEGER primary key autoincrement,
            name text not null,
            lastname text not null,
            thirdname text,
            birthdate date not null,
            phone text not null UNIQUE
            )"""
    conn.execute(peoplesTable)
    conn.commit()
    conn.close()
