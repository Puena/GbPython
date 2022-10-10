# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import math


def primefactors(n):
    while n % 2 == 0:
        print(2),
        n = int(n / 2)

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while (n % i == 0):
            print(i)
            n = int(n / i)

    if n == 1:
        print(n)
    elif n > 2:
        print(n)


natural_number = int(input("Enter number: "))
primefactors(natural_number)
