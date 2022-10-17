import sqlite3
from sqlite3 import Error


def connect(db_name: str):
    try:
        con = sqlite3.connect(db_name)
        print(f'Connected to database {db_name}')
        return con
    except Error:
        print(Error)
        raise Error
