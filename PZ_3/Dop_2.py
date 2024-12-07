# Ввести число. Если оно четное, разделить его на 4, если нечетное - умножить на 5.

number = int(input'Введите число: ')

if number % 2 == 0:
    number = number // 4
else:
    number = number * 5
print(number)