# Есть список случайных чисел в промежутке от 1 до 200, количеством 200. 
# Создайте список кортежей, первый элемент которого - индекс элемента, а второй - сам элемент,
#  при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]

from random import randint

lst = [randint(1, 200) for i in range(200)]
print(type(lst))

print(lst)
[randint(1, 200) for i in range(200)]
tpl = tuple(lst)
print(type(tpl))

print(tpl)
(randint(1, 200) for i in range(200))
