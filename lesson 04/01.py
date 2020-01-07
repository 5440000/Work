# 1: Написать программу, которая в качестве аргумента принимает объект данных datettime,
# необходимо найти сколько времени с времени переданного объекта в днях, часах, минутах.

import datetime

date = datetime.datetime(2019, 12, 12)
now = datetime.datetime.now()
delta = now - date
total_seconds = (delta.total_seconds())
minutes = int(total_seconds/60)
hours = int(minutes/60)
days = int(hours/24)
print(f"Дней:{days} Часов:{hours} Минут:{minutes}")