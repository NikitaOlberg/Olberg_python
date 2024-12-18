# Дан список A ненулевых целых чисел размера 10. Вывести значение первого из тех
# его элементов AK, которые удовлетворяют неравенству AK < A10. Если таких
# элементов нет, то вывести 0.

import random

list = []
t = 0
while t < 10:
    list.append(random.randint(1, 100))
    t += 1

print(list)


for i in range(len(list)):
    if list[i] <  list[-1]:
        print(list[i])
        break
else:
    print(0)