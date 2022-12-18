# Задайте список из n чисел последовательности (1 + 1/n)**n, выведите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

import math
n = int(input('Введите число: '))
result = []

for i in range(1,n+1):
    result.append(round((1+1/i)**i,2))
print(result)
print(math.fsum(result))