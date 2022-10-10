# Представлен список чисел. Необходимо вывести элементы
# исходного списка, значения которых больще предыдущего элемента.
import random


user_input = input("Введите максимальное число элементов ")

random_list = [random.randint(-d, d) for d in range(int(user_input))]

print(random_list)
print([random_list[i+1] for i in range(len(random_list) - 1) if random_list[i+1] > random_list[i]])
