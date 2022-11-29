# 3 - Дан массив размера N. После каждого отрицательного элемента массива
# вставьте элемент с нулевым значением.

# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

import random

num_n = int(input('Введите число N: '))
count = 0
rand_list = []
for i in range(num_n):
    rand_list.append(random.randint(-10, 10))
print(f'Исходный массив: {rand_list}')

for i in range(num_n):
    if rand_list[i] < 0:
        rand_list.insert(i + 1, count)
if rand_list[-1] < 0:
    rand_list.append(0)
print(f'Получившися массив - {rand_list}')