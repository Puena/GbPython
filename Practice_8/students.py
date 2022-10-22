import database


def find(id: int):
    conn = database.connect()
    cursor = conn.cursor()
    query = """select * from students where id = ?"""
    cursor.execute(query, (id))
    records = cursor.fetchall()
    conn.close()
    return list(map(lambda r: {
        "id": r[0],
        "name": r[1],
        "lastname": r[2],
        "birthdate": r[3]
    }, records))


def findAll():
    conn = database.connect()
    cursor = conn.cursor()
    query = """select * from students"""
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    return list(map(lambda r:
                    {"id": r[0],
                     "name": r[1],
                     "lastname": r[2],
                     "birthdate": r[3]}, records))


def insert(name, lastname, birthdate):
    conn = database.connect()
    cursor = conn.cursor()
    query = """INSERT INTO students (name, lastname, birthdate)
                            VALUES (?, ?, ?)"""
    cursor.execute(query, (name, lastname, birthdate))
    conn.commit()
    conn.close()


def update(id: int, name: str, lastname: str, birthdate):
    conn = database.connect()
    cursor = conn.cursor()
    query = """UPDATE students set name = ?, lastname = ?, birthdate = ?
                                where id = ?"""
    cursor.execute(query, (name, lastname, birthdate, id))
    conn.commit()
    conn.close()


def delete(id: int):
    conn = database.connect()
    cursor = conn.cursor()
    query = """delete from students where id = ?"""
    cursor.execute(query, (id))
    conn.commit()
    conn.close()
