# 1 - Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# (-0.56) -> 11

# def num_int(float_num):
#     while round(float_num, 9) % 10 != 0:
#         float_num = round(float_num, 9) * 10
#     num_n = int(float_num)
#     return num_n // 10


# def sum_digit(num_summa):
#     sum = 0
#     while num_summa > 0:
#         sum += num_summa % 10
#         num_summa //= 10
#     return num_summa


# try:
#     num_n = float(input('введите вещественное число: '))
#     number_float = abs(num_n)
#     print(f'{num_int(num_n)}')
#     print(f'сумма = {sum_digit(num_int(num_n))}')

# except ValueError:
#     print('Введено некорреткное значение')


#  Альтернативный код

number = input('Введите вещественное число: ')
num_1 = number.replace('.', '').replace('-', '').replace(',', '')

result = round(sum(int(i) for i in num_1))
print(result)
