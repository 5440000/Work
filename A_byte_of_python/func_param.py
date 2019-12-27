def printMax(a, b): # a, b назваются параметрами функции
    if a > b:
        print(a, 'maximalno')
    elif a == b:
        print(a, "ravno", b)
    else:
        print(b, "maksimalno")

printMax(3, 4) # прямая передача занчений#
x = 5
y = 7
printMax(x, y) # передача переменных в качестве аргументов