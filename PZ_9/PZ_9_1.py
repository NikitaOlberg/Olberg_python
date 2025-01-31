# Дан словарь на 6 персон, найти и вывести их средний возраст. (Пример,
# {"Андрей": 32, "Виктор": 29, "Максим": 18, ...}, среднее 26,33).
dictage = dict(Андрей=32, Виктор=29, Максим=18, Пётр=60, Михаил=27, Алексей=17)
average = 0
counter = 0
for i in dictage:
    average += dictage[i]
    counter += 1
print(dictage)
print(average/counter)

