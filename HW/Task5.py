# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
#  Формула нахождения расстояния между двумя точками AB = √(xb - xa)2 + (yb - ya)2

x1 = int(input("Введите координату Х первой точки: "))
y1 = int(input("Введите координату Y первой точки: "))
x2 = int(input("Введите координату Х второй точки: "))
y2 = int(input("Введите координату Y второй точки: "))

import math
d = math.sqrt((x2 - x1)**(2) + (y2-y1)**(2))
print(f"Расстояние между точками равно {d}")
