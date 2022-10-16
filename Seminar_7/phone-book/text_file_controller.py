import book
import text_file_handler
import json_file_handler


def text_file_controller(path: str):
    book.init()
    text_file_handler.init(iseparator="**")
    text_file_handler.read(path, book.add_row)
    print(book.group_by_first_lastname_letter())
    data = book.to_json()
    json_file_handler.write(path + "_out.json", data)
