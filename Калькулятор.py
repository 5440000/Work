# ДЕБИЛЬНЫЙ КАЛЬКУЛЯТОР НОМЕР 1

what = input("что делаем ? (+ -): " )
a = float(input("первое число"))
b = float(input("second number"))

if what == "+":
    c = a + b
    print("Total:" + str(c))
elif what == "-":
    c = a - b
    print("Total:" + str(c))
else:
    print("error ")

