import database


def find(number: int):
    conn = database.connect()
    cursor = conn.cursor()
    query = """select * from classrooms where id = ?"""
    cursor.execute(query, (number))
    resutlt = cursor.fetchall()
    conn.close()
    return list(map(lambda r: {"number": r[0]}), resutlt)


def findAll():
    conn = database.connect()
    cursor = conn.cursor()
    query = """select * from classrooms where id = ?"""
    cursor.execute(query)
    resutlt = cursor.fetchall()
    conn.close()
    return list(map(lambda r: {"number": r[0]}), resutlt)


def insert(number: int):
    conn = database.connect()
    cursor = conn.cursor()
    query = """insert into classrooms (numbers) values (?)"""
    cursor.execute(query, (number))
    conn.commit()
    conn.close()
    return number


def update(number: int):
    conn = database.connect()
    cursor = conn.cursor()
    query = """update classrooms set number = ? where number = ?"""
    cursor.execute(query, (number, number))
    conn.commit()
    conn.close()


def delete(number: int):
    conn = database.connect()
    cursor = conn.cursor()
    query = """delete classrooms where number = ?"""
    cursor.execute(query, (number))
    conn.commit()
    conn.close()
