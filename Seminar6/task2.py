# Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def mult_lst(lst):
    elem = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(elem)]
    print(new_lst)


lst = [2, 3, 5, 6, 8, 9, 3, 4]
mult_lst(lst)