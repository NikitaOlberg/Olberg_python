# Составить программу, в которой функция построит изображение, в котором в первой
# строке 1 звездочка, во второй - 2, в третьей -3, ..., в строке с номером m - m звездочек.

def amount(k):
    t = 1
    while t <= k:
        print('*'*t)
        t += 1

number = input("Введи целое число от 1 до m: ")

while type(number) != int: # обработка исключений
    try:
        number = int(number)
    except ValueError:
        print("Неправильно ввели!")
        number = input("Введите целое число: ")

amount(number)