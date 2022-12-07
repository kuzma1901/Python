# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
randlist = []

for i in range(5):
    n = random.randint(5, 30)
    randlist.append(n)
print(randlist)

sum_odd = 0
for i in range(1, len(randlist), 2):
    sum_odd += randlist[i]
print(sum_odd)
