#Задания:
# 1: Написать программу, которая в качестве аргумента принимает объект данных datettime,
# необходимо найти сколько времени с времени переданного объекта в днях, часах, минутах.

import datetime


date = datetime.datetime(2019, 12, 12)
now = datetime.datetime.now()
delta = now - date
y = (delta.total_seconds())
m = int(y/60)
h = int(m/60)
d = int(h/24)
print(f"Дней:{d} Часов:{h} Минут:{m}")

# 2: Написать программу, которая будет принимать в качестве аргумента список целых числе
# и выводить в качестве рузльтата максимальное количество возможных уникальных комбинаций, например:
#[2, 5, 8] -> (2, 5), (2, 8), (5, 8)
#[72, 586, 12] -> (72, 586), (72, 12), (586, 12)
from random import shuffle
lst=[]
lst.append(int(input()))
lst.append(int(input()))
lst.append(int(input()))

shuffle(lst)
print(lst)
[[i,i+1] for i in lst]
print(lst)
# a = []  # заводим пустой список
# n = int(input())  # считываем количество элемент в списке
# for i in range(n):
#     new_element = int(input())  # считываем очередной элемент
#     a.append(new_element)  # добавляем его в список
#     # последние две строки можно было заменить одной:
#     # a.append(int(input()))
# print(aaa)


# >> [[i,i+1 ] for i in lst]
#
# print(i)

# 4: Написать программу, которая будет выводить все числа в диапазоне от 0 до 1000, которые делять на 7 без остатка.
i=1

for i in range(1000):
    i = i + 1
    if i % 7 == 0:
        print(int(i))