# Даны положительные числа A и B (A > Б). На отрезке длины A размещено
# максимально возможное количество отрезков длины Б (без наложений). Не
# используя операции умножения и деления, найти длину незанятой части отрезка A.


a = input("Введите первое положительное число: ")
b = input("Введите второе положительное число, которое меньше первого: ")

while type(a) != int: # обработка исключений
 try:
     a = int(a)
 except ValueError:
     print("Неправильно ввели!")
     a = input("Введите первое число: ")
while type(b) != int: # обработка исключений
 try:
     b = int(b)
     if b >= a:
         print("Неправильно ввели!")
         b = input("Введите второе число ещё раз: ")
 except ValueError:
     print("Неправильно ввели!")
     b = input("Введите второе число: ")

while a >= b:
    a -= b
print(f"Длина незанятой части отрезка A: {a}")
