# 1: Написать функцию, которая возвращает первое слово из строки используя методы строки
# и отдельно регулярные выражения.
import re
a = 'Hello word'

print(a.split()[0])

import re

result = re.search(r'Hello', 'Hello world')
print(result.group(0))