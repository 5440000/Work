# # 4. Написать программу, которая принимает два аргумента: месяц и год в формате целых чисел,
# а на выходе возвращает календарь для переданных данных, например: 2019, 12 (декабрь 19-го года):
# #    December 2019
# # Mo Tu We Th Fr Sa Su
# #                    1
# #  2  3  4  5  6  7  8
# #  9 10 11 12 13 14 15
# # 16 17 18 19 20 21 22
# # 23 24 25 26 27 28 29
# # 30 31
theyear = int(input('Введите год'))
themonth = int(input('Введите месяц'))
import calendar
c = calendar.LocaleTextCalendar()
print(c.formatmonth(theyear, themonth))