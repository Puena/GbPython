import database


def find(id: int):
    conn = database.connect()
    cursor = conn.cursor()
    query = """select * from students where id = ?"""
    cursor.execute(query, (id))
    records = cursor.fetchall()
    return {
        "id": records[0][0],
        "name": records[0][1],
        "lastname": records[0][2],
        "birthdate": records[0][3]
    }


def findAll():
    conn = database.connect()
    cursor = conn.cursor()
    query = """select * from students"""
    cursor.execute(query)
    records = cursor.fetchall()
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
    cursor.close()


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
    query = """DELETE students where id = ?"""
    cursor.execute(query, (id))
    conn.commit()
    conn.close()
