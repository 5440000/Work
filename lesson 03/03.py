#3. Написать программу, которая принимает на входе число n и выводит на экран n + nn - nnn * nnnn, пример: число 5
#5 + 55 - 555 * 5555 = -3082965

x = input("Введите число")
a = int(x)
b = int(x + x)
c = int(x + x + x)
d = int(x + x + x + x)
y = (a + b - c * d)
print(f"{x} + {x + x} - {x + x + x} * {x + x + x + x} = {y}")