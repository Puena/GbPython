'''
    Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

    Пример:

    - 6 -> да
    - 7 -> да
    - 1 -> нет
'''
dayNumber = int(input("Введите номер дня недели от 1 до 7: "))
if dayNumber == 6 or dayNumber == 7:
    print("Yes")
else:
    print("No")