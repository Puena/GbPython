book = dict()

KEY_NAME = "name"
KEY_LASTNAME = "lastname"
KEY_PHONE = "phone"
KEY_DESCRIPTION = "description"


def init():
    global book
    book = dict()


def add_row(name, lastname, phone, description):
    # { Dow John: { name: John, lastname: Dow, phone: +74995013435}
    key = f'{name} {lastname}'
    if key not in book:
        book[key] = {KEY_NAME: name, KEY_LASTNAME: lastname,
                     KEY_PHONE: phone, KEY_DESCRIPTION: description}


def group_by_first_lastname_letter():
    new_book = dict()
    for _, val in book.items():
        first_letter = val[KEY_LASTNAME][0]
        if first_letter not in new_book:
            new_book[first_letter] = [val]
        else:
            new_book[first_letter].append(val)
    return new_book


def to_list():
    n_list = list()
    for _, v in book.items():
        print(v)
        n_list.append([v[KEY_NAME], v[KEY_LASTNAME],
                       v[KEY_PHONE], v[KEY_DESCRIPTION]])
    return n_list


def to_json():
    return list(book.values())
