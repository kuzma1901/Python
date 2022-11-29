# 2 - Напишите программу, которая принимает на вход число N
# и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

num_n = int(input('Введите число: '))
list_mult = []
num_mult = 1
for i in range(1, num_n + 1):
    list_mult.append((num_mult) * i)
    list_mult = list_mult * i
print(list_mult)
