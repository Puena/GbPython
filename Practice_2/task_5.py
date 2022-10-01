# Реализуйте алгоритм перемешивание списка без модуля shuffle из модуля ramdom.

import random

def my_shuffle(list):
    for i in reversed(range(len(list))):
        j = random.randint(0, i)
        list[i], list[j] = list[j], list[i]
        


list_size = int(input("Введите размер списка: "))
created_list = [random.randrange(-(list_size*10), (list_size+1)*10, 1) for e in range(list_size)]
print(created_list)
my_shuffle(created_list)
print(created_list)