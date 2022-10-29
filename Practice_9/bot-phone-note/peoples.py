import database


def findAll():
    conn = database.connect()
    cursor = conn.cursor()
    query = """select * from peoples"""
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    return list(map(lambda p: {""}, records))
