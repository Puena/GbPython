import book
import json_file_handler
import text_file_handler


def json_file_controller(path: str):
    book.init()
    json_file_handler.read(path, book.add_row)
    print(book.group_by_first_lastname_letter())
    data = book.to_list()
    text_file_handler.init(iseparator="**")
    text_file_handler.write(path + "_out", data)
