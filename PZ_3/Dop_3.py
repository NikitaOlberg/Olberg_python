# Ввести двухзначное число. Если сумма цифр числа четная, то увеличить число на 2,
# в противном случае уменьшить на 2.

number = int(input('Введите двузначное число: '))
while number < 10 or number > 99:
    print('Неправильно ввели!')
    number = int(input('Введите двузначное число: '))

digit_1 = number % 10
digit_2 = number // 10

if (digit_1 + digit_2) % 2 == 0:
    number += 2
else:
    number -= 2
print(number)