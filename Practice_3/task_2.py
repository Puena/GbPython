# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def my_func(list):
    my_list = []
    
    _array_lenght = int(len(list) / 2 + len(list) % 2)
    
    for i in range(_array_lenght):
        my_list.append(list[i] * list[len(list)-1-i])
        
    return my_list

print(my_func([2, 3, 4, 5, 6]))
print(my_func([2, 3, 5, 6]))