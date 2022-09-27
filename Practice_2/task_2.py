# Напишите программу которая принимает на вход число N и выдает набор произведений числе от 1 до N

input = int(input("Введите число: "))

res = 1
for n in range(1, input+1):
    res = res * n
    print(res, end=' ')