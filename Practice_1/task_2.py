'''
    Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''
X = 1
Y = 2
Z = 3
left_part = not(X or Y or Z)
right_part = (not X) and (not Y) and (not Z)
print(left_part == right_part)