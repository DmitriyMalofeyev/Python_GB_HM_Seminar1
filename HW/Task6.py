# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

# Требуется найти N-е число Фибоначчи.

n = int(input("Введите число N: "))
a0 = 0
a1 = 1
i = 0
while i < n - 2:
    an = a0 + a1
    a0 = a1
    a1 = an
    i = i + 1
print(f"N -ное число Фибоначчи равно {a1}")

