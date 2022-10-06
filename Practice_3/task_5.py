# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input("Enter k: "))


def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

positive_fib = [fib(e) for e in range(k+1)]
    
    
def neg_fib(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    return neg_fib(n+2) - neg_fib(n+1)

negative_fib = [neg_fib(-e) for e in reversed(range(1, k+1))]
print(negative_fib)

result = negative_fib + positive_fib

print(result)