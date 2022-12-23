# Дан список случайных чисел. Оставьте только те, сумма цифр которых четна


from random import randint

lst = [randint(0, 100) for i in range(5)]
print(lst)
sum = 0
new_lst = []

for i in lst:
    if ((lst[i] % 2 + lst[i]//2) % 2 == 0):
        new_lst.append(lst[i])
print(new_lst)

