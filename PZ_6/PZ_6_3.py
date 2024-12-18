# Дан список A размера N и целое число K (1 < K < 4, K < N ). Осуществить
# циклический сдвиг элементов списка влево на K позиций (при этом A N перейдет в
# AN_K, AN-1 — в AN-K-1, ..., A1 — в AN-K+1). Допускается использовать вспомогательный
# список из 4 элементов.

import random

k = input("Введи целое число 'К' от 1 до 4: ")

while type(k) != int: # обработка исключений
    try:
        k = int(k)
        if k <= 1 or k >= 4:
            print("Неправильно ввели!")
            k = input("Введите число от 1 до 4: ")
    except ValueError:
        print("Неправильно ввели!")
        k = input("Введите целое число: ")

number = input("Введи размер списка: ")

while type(number) != int: # обработка исключений
    try:
        number = int(number)
        if number <= k:
            print("Неправильно ввели!")
            k = input("Введите число больше К: ")
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
for i in range(k, len(list)):
    result.insert(i-k, list[i])

for i in range(0, k):
    result.insert(i + number + 1 - k, list[i])

print(result)