# Ввести 2 числа. Если их произведение отрицательно, умножить его на 8, в противном
# случае увеличить его в 1.5 раза.

first_n = int(input('Введите первое число: '))
second_n = int(input('Введите второе число: '))
third_n = second_n * first_n
if third_n < 0:
    third_n *= 8
else:
    third_n *= 1.5
print(third_n)