# Описать функцию PowerA3(A, B), вычисляющую третью степень числа A и
# возвращающую ее в переменную B (A — входной, B — выходной параметр; оба
# параметра являются вещественными). С помощью этой функции найти третьи
# степени пяти данных чисел.

def PowerA3(a, b = 3):
    b = a ** b
    return a, b

def count(c = 5):
    t = 1
    while t <= c:
        number = input('Введите число: ')
        while type(number) != float:  # обработка исключений
            try:
                number = float(number)
            except ValueError:
                print("Неправильно ввели!")
                number = input("Введите ещё раз: ")
        print(PowerA3(number))
        t += 1
count()

#    for arg in args:
#        print(PowerA3(arg))

#nm1, nm2, nm3, nm4, nm5 = float(input('Введите 5 чисел: \n')),  float(input()), float(input()), float(input()), float(input())

#print(arguments(nm1, nm2, nm3, nm4, nm5))
