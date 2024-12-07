# Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2.

first_n = int(input('Введите первое число: '))
second_n = int(input('Введите второе число: '))
third_n = second_n + first_n

if third_n % 5 == 0:
    first_n += 1
    second_n += 1
else:
    first_n -= 2
    second_n -= 2
print(first_n, second_n)