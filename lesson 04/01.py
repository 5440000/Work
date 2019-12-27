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