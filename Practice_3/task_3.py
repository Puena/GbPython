# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math


def get_after_point(f):
    return (f - int(f)) % 1

def my_func(list):
    max = get_after_point(list[0])
    min = get_after_point(list[0])
    
    for e in list:
        val = get_after_point(e)
        if val > max:
            max = val
        elif val < min:
          min = val
    return max - min

print(math.floor(my_func([1.1, 1.2, 3.1, 5, 10.01]) * 10 ** 2) / 10 ** 2)
