#  Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


from decimal import Decimal

d = float(input("Введите число: "))
a = Decimal(d)
a = a.quantize(Decimal(input("Введите точность: ")))
print(a)