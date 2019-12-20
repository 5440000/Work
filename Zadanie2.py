# Необходимо написать программу, которая получает на  входе число и выводит слово "Odd" если число четное.
# Если число четное и в диапазоне от 2 до 27,
# то выводит "In first range", если число нечетное и в диапазоне от 29 до 53,
# то выводит "In second range",
# во всех других случаях "It's something""It's something".
number = int(input('Put the number :'))
if number % 2 == 0:
    print('Odd')
    if number in range(2,27):
        print('In first range')
else:
    if number in range(29,53):
        print('In second range')
    else:
        print("It's something")
