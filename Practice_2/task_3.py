# Задайте список из N чисел заполенный по формуле (1+1/n) ** n и выведите на экран их сумму

input = int(input("Введите число: "))

sum = 0
lst = list()
for n in range(1,input+1):
    res = round((1+1/n)**n)
    lst.append(res)
    sum += res
    
print(lst, end=" -> ")
print(sum)