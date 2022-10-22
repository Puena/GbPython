import database
import students


def main():
    database.init()
    students.insert("Ivan", "Fedorov", "14-10-2003")
    result = students.findAll()
    print(result)


main()
