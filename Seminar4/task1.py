# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]


num_n = int(input("Введите число: "))
lst = []
num_d = 2
num_m = num_n
while num_d * num_d <= num_n:
    if num_n % num_d == 0:
        lst.append(num_d)
        num_n //= num_d
    else:
        num_d += 1
lst.append(num_n)
print(lst)
