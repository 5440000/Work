#1. Написать программу, которая будет выводить первый и последний элемент списка:
list = ['Email:', 'SSN:','Address:','Home Phone:','Mobile Phone: ','DOB:','Date of Surgery:','Date of Service:','Facility of Service:','Clinic Number:','Employer:','Work Phone: ','Fax: ','Type:','IPA:','Health Plan:','ID #:','Claims Address:','Group #:','Claim # / PO #:','Phone:','Fax:','Contact','Adjuster Email','Util Review Phone','Util Review Fax','Doctor:','NPI #: ','Date of Injury: ','Body Parts:','Body Part Side:','Gender:','Diagnosis:','Diagnosis 2:','Procedure:']
print(list[0] + list[-1])

#2. Написать программу, которая будет выводить предпоследний элемент списка:
lis = ['Email:', 'SSN:','Address:','Home Phone:','Mobile Phone: ','DOB:','Date of Surgery:','Date of Service:','Facility of Service:','Clinic Number:','Employer:','Work Phone: ','Fax: ','Type:','IPA:','Health Plan:','ID #:','Claims Address:','Group #:','Claim # / PO #:','Phone:','Fax:','Contact','Adjuster Email','Util Review Phone','Util Review Fax','Doctor:','NPI #: ','Date of Injury: ','Body Parts:','Body Part Side:','Gender:','Diagnosis:','Diagnosis 2:','Procedure:']
print(list[-2])

#3. Написать программу, которая принимает на входе число n и выводит на экран n + nn - nnn * nnnn, пример: число 5
#5 + 55 - 555 * 5555 = -3082965

x = input("Введите число")
a = int(x)
b = int(x+x)
c = int(x+x+x)
d = int(x+x+x+x)
y = (a+b-c*d)
print(f"{x} + {x+x} - {x+x+x} * {x+x+x+x} = {y}")

#4. Написать программу, которая принимает два аргумента:
# месяц и год в формате целых чисел, а на выходе возвращает календарь для переданных данных,
# например: 2019, 12 (декабрь 19-го года):
#   December 2019
#Mo Tu We Th Fr Sa Su

#                   1
# 2  3  4  5  6  7  8
# 9 10 11 12 13 14 15
#16 17 18 19 20 21 22
#23 24 25 26 27 28 29
#30 31
#подсказка datetime.datetime.now


#year = input("Введите год формате целых чисел")
#month = input("Введите месяц формате целых чисел ")
#print()
#import calendar
#print(calendar.weekheader(2))



