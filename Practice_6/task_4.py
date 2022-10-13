# Функция принимает строки "Имя Фамилия" возвращает словарь, где ключ первая буква фамилии, затем первая буква имени и массив имён соответсвующий первым буквам
input_names = ["Иван Сергеев", "Мария Серова", "Петр Алексеев", "Илья Иванов",
               "Марина Савельева", "Петр Анисимов", "Алина Ветрякова", "Бибочка Аркадьева"]


def handle_lastname(fullname: str, note: dict):
    splitted = fullname.split()
    last_name = splitted[1]

    if last_name[0] not in note:
        note[last_name[0]] = dict()
    handle_firstname(fullname, note[last_name[0]])


def handle_firstname(fullname: str, note: dict):
    if fullname[0] not in note:
        note[fullname[0]] = list()
    note[fullname[0]].append(fullname)


book = dict()
for name in input_names:
    handle_lastname(name, book)
print(book)
