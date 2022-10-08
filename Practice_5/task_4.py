# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

from collections import Counter


def add_or_increment(data: dict, key: str):
    if key in data:
        data[key] += 1
    else:
        data[key] = 1

def dict_to_string(data: dict):
    string = ""
    for letter, count in data.items():
        string += str(count)
        string += letter
    return string

def rle(string: str):
    # SORT !!!
    hash_table = Counter(list(string))
    print(hash_table)
    
def rle2(string: str):
    temp = dict()
    for s in string:
        add_or_increment(temp, s)
    
    return dict_to_string(temp)
        



print(rle2("wwwwwwwwwasdaklsjdkljhqiuhkajsdasduqwdasdasda"))