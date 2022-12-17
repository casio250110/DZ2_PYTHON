# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int

import random
my_list=[]
for i in range(10):
    my_list.append(random.randint(0,100))
print(my_list)
for i in range(len(my_list)-1, 0, -1):
    j = random.randint(0, i + 1) 
    my_list[i], my_list[j] = my_list[j], my_list[i]
print(my_list)