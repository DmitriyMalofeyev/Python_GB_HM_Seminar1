# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input("Введите номер четверти координат: "))

if a == 1:
    print("Диапазоны значений: x>0, y>0")
elif a == 2:
    print("Диапазоны значений: x<0, y>0")
elif a == 3:
    print("Диапазоны значений: x<0, y<0")
elif a == 4:
    print("Диапазоны значений: x>0, y<0")
else:
    print("Введите число от 1 до 4")

