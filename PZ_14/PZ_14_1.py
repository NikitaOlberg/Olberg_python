# Из исходного текстового файла (experience.txt) выбрать стаж работы. Посчитать
# количество полученных элементов.

import re
#s = '<a href="#10">10: CamelCase -> under_score</a>;'
#p = re.compile(r"<a.*>(.*?)</a>", re.S)
#print(p.findall(s))

f1 = open('experience.txt')
lst = f1.readlines()
st = "".join(lst)
f1.close()
print(st)
p = re.compile(r".*?\s([0-9]+\s.*?)\s([0-9]*\s.*?)\s", re.S)
print(p.findall(st), len(p.findall(st)))
