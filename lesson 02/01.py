# 1. Необходимо написать программу, которая получает два числа на входе,
# и первой строчкой выводит результат их суммы в целочисленном представлении.
# Вторая строчка выводит разницу двух чисел. Третья строка - выводит сумму двух чисел.
# Также программа должна включать в себя обработчик ошибок, если ей переданы в качестве аргументов переданы какие-то другие параметры.
try:
    a = int(input('input the number'))
    b = int(input('put the number'))
    print(a + b)
    print(a - b)
    print(float(a) + float(b))
except ValueError:
    print("That key does not exist!")