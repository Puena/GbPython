# Напишите программу которая на вход принимает два числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N]

nubmer_of_elements = int(input("Введите количество элементов. "))
list_of_elements = [e for e in range(-nubmer_of_elements, nubmer_of_elements + 1)]
print(list_of_elements)
print("Введите индексы элементов которые необходимо перемножить!")
first_position = int(input("Введите первый индекс ")) - 1
second_postition = int(input("Введите второй индекс ")) - 1
if (first_position >= 0 and first_position < len(list_of_elements)
    and second_postition >= 0 and second_postition < len(list_of_elements)):
    print("Произведение равно: ", list_of_elements[first_position] * list_of_elements[second_postition])
else:
    print("Недопустимый индекс!")