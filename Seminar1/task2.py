# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.

print('X Y Z')
for X in range(2):
    for Y in range(2):
        for Z in range(2):
            if (not (X) and Y and Z) or (not (X) and not (Y) and Z) or (not (X) and not (Y) and not (Z)) == 1:
                print(X, Y, Z)
