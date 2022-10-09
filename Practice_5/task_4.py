# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

from collections import Counter
from curses.ascii import isdigit

def unzip(compressed_string:str):
    new_string = ""
    for i in range(len(compressed_string)):
        if compressed_string[i].isdigit():
            new_string += compressed_string[i+1] * int(compressed_string[i])
            
    return new_string
        
    
def rle2(string: str):
    new_string = ""
    last_symmbol = string[0]
    count = 1
    
    for i in range(1, len(string)):
        if string[i] == last_symmbol:
            count += 1
            continue
        else:
            new_string += f"{count}{last_symmbol}"
            last_symmbol = string[i]
            count = 1
            
    new_string += f"{count}{last_symmbol}"
    
    return new_string

in_string = "wwwwwwwwwasdasdasdasdasdasdoooooooqweqwadaaaaaaaa"
print(in_string)
compressed = rle2(in_string)
print(compressed)
unpack = unzip(compressed)
print(unpack)
print(unpack == in_string)

