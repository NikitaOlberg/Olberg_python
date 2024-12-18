# Дан список размера N. Найти номера двух ближайших элементов из этого списка (то
# есть элементов с наименьшим модулем разности) и вывести эти номера в порядке
# возрастания.
import random

number = input("Введи размер списка: ")

while type(number) != int: # обработка исключений
    try:
        number = int(number)
    except ValueError:
        print("Неправильно ввели!")
        number = input("Введите целое число: ")

list = []
count = 0
while count < number:
    list.append(random.randint(1, 100))
    count += 1
print(list)
result = []
k = 10000
for i in range(len(list)-1):
    if abs(list[i]-list[i + 1]) < k:
        k = abs(list[i]-list[i + 1])
        result.clear()
        result.append(list[i])
        result.append(list[i+1])
result.sort(key = None, reverse = False)
print(result)