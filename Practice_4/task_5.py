from collections import Counter
import re
from numpy import sign




def separate_string(string):
    split_signs = ["-", "+"]
    splitted = list()
    temp_string = list()
    list_string = list(string)
    for i, c in enumerate(list_string):
        if c == "=":
            if len(temp_string) > 0:
                splitted.append("".join(temp_string))
                temp_string = list()
            return splitted
        if c in split_signs and list_string[i+1] == " ":
            if c == "-":
                splitted.append("".join(temp_string))
                temp_string = list(c)
            else:            
                splitted.append("".join(temp_string))
                temp_string = list()
        elif c != " ":
            temp_string.append(c)
    return splitted

def parse_poly(string_array):
    poly = Counter()
    for expr in string_array:
        if "x" in expr:
            matched = re.search(r"([\-\d]+)?x[\^]?([\d])?", expr)
            if matched:
                m = matched.group(1) or 1
                k = matched.group(2) or 1
                
                poly[int(k)] = int(m)
        else:
            matched = re.search(r"([\-\d]+)", expr)
            if matched: 
                k = 0
                m = int(matched.group(1))
                poly[k] = m
            
    return poly
            

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

def add_poly(dest: Counter, source: Counter):
    for k,m in source.items():
        if k in dest:
            dest[k] += m
        else:
            dest[k] = m
            
f = open("polynomial.txt", "r")
line = f.readline()
poly_sum = Counter()
while (line != ""):
    poly = parse_poly(separate_string(line))
    add_poly(poly_sum, poly)
    line = f.readline()

f.close()

f = open("polynomial_sum.txt", "w")
f.write(pring_poly(poly_sum) + "\n")
f.close()
