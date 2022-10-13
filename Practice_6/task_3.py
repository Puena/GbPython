# Написать функцию, аргументы имена сотрудников , возвращает словарь первая буква ключ, значения это список содержащий имена на эту букву
from collections import Counter

input_names = ["Иван", "Мария", "Петр", "Илья",
               "Марина", "Петр", "Алина", "Бибочка"]


def sort_names(names: list):
    name_book = Counter()
    for name in names:
        if name[0] in name_book:
            name_book[name[0]].append(name)
        else:
            name_book[name[0]] = [name]
    return name_book


print(sort_names(input_names))
