import database


def find(id: int):
    conn = database.connect()
    cursor = conn.cursor()
    query = """select * from places where id = ?"""
    cursor.execute(query, (id))
    result = cursor.fetchall()
    conn.close()
    return list(map(lambda r: {
        "id": r[0],
        "row": r[1],
        "cell": r[2],
        "variant": r[3],
        "classroom_number": r[4]
    }, result))


def findAll():
    conn = database.connect()
    cursor = conn.cursor()
    query = """select * from places where id = ?"""
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return list(map(lambda r: {
        "id": r[0],
        "row": r[1],
        "cell": r[2],
        "variant": r[3],
        "classroom_number": r[4]
    }, result))


def insert(row: int, cell: int, variant: int, classroom_number: int):
    conn = database.connect()
    cursor = conn.cursor()
    query = """insert into places (row, cell, variant, classroom_number)
    values(?, ?, ?, ?)"""
    cursor.execute(query, (row, cell, variant, classroom_number))
    conn.commit()
    conn.close()


def update(row: int, cell: int, variant: int):
    conn = database.connect()
    cursor = conn.cursor()
    query = """update places set row = ?, cell = ?, variant = ?"""
    cursor.execute(query, (row, cell, variant))
    conn.commit()
    conn.close()


def delete(id: int):
    conn = database.connect()
    cursor = conn.cursor()
    query = """delete places where id = ?"""
    cursor.execute(query, (id))
    conn.commit()
    conn.close()
