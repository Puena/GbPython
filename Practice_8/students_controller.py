import students
import re
import logger


def help_info():
    print("For find student with id 2, type: get student 2")
    print("For find all students, type: get students")
    print("For insert student, type: insert student Alexander Ivanov 19-10-2003")
    print("For update student, type: update student 2 set Alexander Ivanov 19-10-2003")
    print("For delete student with id 4, type: delete student 4")


def handle(input: str):
    logger.init("students.log")
    insert_pattern = "insert student\\s+([а-яА-Я\\w]+)\\s+([а-яА-Я\\w]+)\\s+(\\d{1,2}-\\d{1,2}-\\d{2,4})"
    update_pattern = "update student\\s+(\\d+)\\s+set\\s+([а-яА-Я\\w]+)\\s+([а-яА-Я\\w]+)\\s+(\\d{1,2}-\\d{1,2}-\\d{2,4})"
    find_pattern = "get student (\\d+)"
    find_all_pattern = "get students"
    delete_pattern = "delete student (\\d+)"
    is_insert = re.match(insert_pattern, input)
    is_update = re.match(update_pattern, input)
    is_find = re.match(find_pattern, input)
    is_find_all = re.match(find_all_pattern, input)
    is_delete = re.match(delete_pattern, input)
    if is_insert:
        students.insert(
            is_insert.group(1),
            is_insert.group(2),
            is_insert.group(3))
        print("Student added")
        logger.log_info(
            f'isert into student user input: {input}')
    elif is_update:
        students.update(
            is_update.group(1),
            is_update.group(2),
            is_update.group(3),
            is_update.group(4))
        print("Student updated")
        logger.log_info(f'update student user input: {input}')
    elif is_find:
        result = students.find(is_find.group(1))
        print(result)
        logger.log_info(f'find student user input: {input}')
    elif is_find_all:
        result = students.findAll()
        print(result)
        logger.log_info(f'find all students user input: {input}')
    elif is_delete:
        students.delete(is_delete.group(1))
        print("Student deleted")
        logger.log_info(f'delete student user input: {input}')
