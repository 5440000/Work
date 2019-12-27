number = 23
running = True
while running:
    guess = int(input('введите целое число'))

    if guess == number:
        print('Поздравляю вы угадали ')
        running = False
    elif guess < number:
        print('нет загаданное число немного больше этого')
    else:
        print('загаданное число немного меньше')
else:
    print('цикл вайл закончен')

print("завершение")