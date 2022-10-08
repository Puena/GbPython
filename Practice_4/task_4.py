# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from collections import Counter
import random
from re import S




def pring_poly(poly: Counter):
    string = ""
    count = 0
    for k,m in poly.items():
        if count == 0 and m < 0:
            string += "-"
        elif count > 0 and m < 0:
            string += " - "
        elif count > 0 and m > 0:
            string += " + "
        
        if k == 0 and m != 0:
            string += str(abs(m))
        elif abs(m) > 1:
            string += str(abs(m))
            
        if k != 0:
            if k == abs(1):
                string += "x"
            else:
                string += "{0}^{1}".format("x", str(k))
                
        count += 1
    
    string += " = 0"
    return string
            

def generate_poly(k: int):
    from_n = -10
    to_n = 10
    
    result = Counter({k: random.randint(from_n,to_n)})
    k -= 1
    
    while k >= 0:
        rand = random.randint(from_n,to_n)
        if (rand != 0):
            result[k] = rand
        k -= 1
    
    return result

def add_poly(dest: Counter, source: Counter):
    for k,m in source.items():
        if k in dest:
            dest[k] += m
        else:
            dest[k] = m
    

poly = generate_poly(2)
print(poly)
poly2 = generate_poly(2)
print(poly2)
poly3 = Counter()
add_poly(poly3, poly)
add_poly(poly3, poly2)

f = open("polynomial.txt", "w")
f.write(pring_poly(poly) + "\n")
f.write(pring_poly(poly2) + "\n")
f.close()