# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Подумайте, как это можно решить с помощью рекурсии.


def binary(num, result=""):
    if num != 0:
        result += binary(num // 2, result) + str(num % 2)
    return result


num = int(input('Введите десятичное число: '))

result = binary(num)
print(result)
