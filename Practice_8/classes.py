import database


def find(title: str):
    conn = database.connect()
    cursor = conn.cursor()
    query = """select * from classes wheter title = ?"""
    cursor.execute(query, (title))
    result = cursor.fetchall()
    conn.close()
    return list(map(lambda r: {"id": r[0], "title": r[1]}, result))


def findAll():
    conn = database.connect()
    cursor = conn.cursor()
    query = """select * from classes"""
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return list(map(lambda r: {"id": r[0], "title": r[1]}, result))


def insert(title: str):
    conn = database.connect()
    cursor = conn.cursor()
    query = """insert into classes (title) values (?)"""
    cursor.execute(query, (title))
    conn.commit()
    conn.close()


def update(id: int, title: str):
    conn = database.connect()
    cursor = conn.cursor()
    query = """update classes set title = ? where id = ?"""
    cursor.execute(query, (title, id))
    conn.commit()
    conn.close()


def delete(id: int):
    conn = database.connect()
    cursor = conn.cursor()
    query = """delete classes where id = ?"""
    cursor.execute(query, (id))
    conn.commit()
    conn.close()
