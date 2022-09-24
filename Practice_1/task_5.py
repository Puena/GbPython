'''
    Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

    Пример:

    A (3,6); B (2,1) -> 5,09
    A (7,-5); B (1,-1) -> 7,21
'''

from cmath import sqrt
from collections import namedtuple
import math


Point = namedtuple("Point", ["x", "y"])

print("Enter point A coords")
a = Point(int(input("Enter x coord: ")), int(input("Enter y coord: ")))
print("Enter point B coords")
b = Point(int(input("Enter x coord: ")), int(input("Enter y coord: ")))

distance = ((b.x - a.x)**2 +(b.y - a.y)**2)**0.5
print("A {0}; B {1} -> {2}".format(str(a), str(b), math.floor(distance * 10 ** 2) / 10 ** 2))