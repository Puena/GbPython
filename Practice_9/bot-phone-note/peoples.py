import database
from datetime import datetime


def people_to_string(people: dict):
    # print(type(people["birthdate"]))
    return "{} | {} | {} | {} | {:%Y-%m-%d} | {}".format(
        people["id"],
        people["name"],
        people["lastname"],
        people["thirdname"],
        datetime.strptime(people["birthdate"], "%Y-%m-%d %H:%M:%S"),
        people["phone"],
    )


def findAll():
    conn = database.connect()
    cursor = conn.cursor()
    query = """select * from peoples"""
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    return list(map(lambda e: {"id": e[0],
                               "name": e[1],
                               "lastname": e[2],
                               "thirdname": e[3],
                               "birthdate": e[4],
                               "phone": e[5]}, records))


def find(phone: str):
    conn = database.connect()
    cursor = conn.cursor()
    query = """select * from peoples where phone = ?"""
    cursor.execute(query, (phone,))
    records = cursor.fetchall()
    conn.close()
    return list(map(lambda e: {"id": e[0],
                               "name": e[1],
                               "lastname": e[2],
                               "thirdname": e[3],
                               "birthdate": e[4],
                               "phone": e[5]}, records))


def insert(data: dict):
    conn = database.connect()
    cursor = conn.cursor()
    query = """insert into peoples (
            name, lastname, thirdname, birthdate, phone)
            values(?, ?, ?, ?, ?)"""
    cursor.execute(query, (data["name"], data["lastname"],
                   data["thirdname"], data["birthdate"],
        data["phone"]))
    conn.commit()
    conn.close()


def updatePhone(old_phone: str, phone: str):
    conn = database.connect()
    cursor = conn.cursor()
    query = """update peoples set phone = ? where phone = ?"""
    cursor.execute(query, (phone, old_phone))
    conn.commit()
    conn.close()


def delete(id: int):
    conn = database.connect()
    cursor = conn.cursor()
    query = """delete from peoples where id = ?"""
    cursor.execute(query, (id))
    conn.commit()
    conn.close()
